from PIL import Image
import numpy as np
import random as rd
import math
import pandas as pd
import data as dt
heat = np.loadtxt("testCA/heatData.txt")
# suitable temperature
SUIT_TEMP=8
# temperature coefficient dicides the temperature sensibility
TEMP_COEF=2.3
n=100
h=np.ones((100,100))
h_l=np.ones((100,100))
f=dt.f_sb
f_l=dt.f_sb
m=dt.mp
t=[]
t_l=[]
color_table = [(25,25,112),(0,0,255),(0,180,255),(0,250,154),(0,255,0),(173,255,47),(255,255,0),(255,165,0),(255,69,0),(255,0,0)]

def visual(data,n):

    img = Image.new('RGB', (1000,1000), (255, 255, 255))
    img_array = np.array(img)
    
    block_size = int(1000/n)
    width = 1000
    height = 1000

    max_width = width + block_size
    max_height = height + block_size
    
    for x in range(0, max_width - block_size , block_size):
        for y in range(0, max_height - block_size , block_size):
            for px in range(x,x + block_size):
                for py in range(y,y + block_size):
                    if(data[ int(x/block_size) ][ int(y/block_size) ] == -1):
                        img_array[px, py] = (96,96,96)
                    else:
                        img_array[px, py] = color_table[ data[ int(x/block_size) ][ int(y/block_size) ]  ]

    img = Image.fromarray(img_array)
    img.show()


def hsi():
    for x in range(n):
        for y in range(n):
            if(m[x][y]!=-1):
                h_l[x][y]=h[x][y]
                POPULATION=f[x][y]
                POPULATION_L=f_l[x][y]
                OFFSHORE=m[x][y]
                TEMPERATURE=t[x][y]
                # TEMPERATURE_L=t_l[x][y]
                # CONGESTION=congestion(x,y)

                # population varible
                acc_pop=(POPULATION-POPULATION_L)/POPULATION_L

                if(OFFSHORE!=0):
                    index_offs=(OFFSHORE/80)**(1/40)
                elif(OFFSHORE==0):
                    index_offs=0.85
                # if((POPULATION<(CONGESTION/9))
                index_pop=math.exp(-1*acc_pop)
                index_temp=TEMP_COEF/((abs(TEMPERATURE-SUIT_TEMP)+SUIT_TEMP)/SUIT_TEMP+1)
                h[x][y]=index_pop*index_temp*index_offs
    return
    
def congestion(x,y):
    fsum=0
    for nx in range(x-1,x+1):
        for ny in range(y-1,y+1):
            if(m[nx][ny] != -1):
                fsum = fsum + f[nx][ny]
    return fsum


#visual(f)
def fishCAMain(year):
    # myf=np.array(f)
    n=20
    for i in range(year):
        for x in range(n):
            for y in range(n):
                f_l[x][y]=f[x][y]
                if (m[x][y]!=-1): 
                    f[x][y]=round(f[x][y]*h[x][y])
        hsi()

# def color():
#     max_v=0
#     for x in range(n):
#         for y in range(n):
#             if(f[x][y]>max_v):
#                 max_v=f[x][y]
          
def init():
    for x in range(n):
        for y in range(n):
            if(m[x][y]!=-1):
                f_l[x][y]=round(f[x][y]*(1+0.04*rd.randint(-2,2)))
            elif(m[x][y]==-1):
                f[x][y]=-1
    hsi()

# init()
# fishCAMain(50)

