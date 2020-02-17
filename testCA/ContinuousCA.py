from PIL import Image
import numpy as np
import random as rd
import math
import pandas as pd
import data as dt
import scipy.io as io
import kMeans as km
def flip180(arr):
    new_arr = arr.reshape(arr.size)
    new_arr = new_arr[::-1]
    new_arr = new_arr.reshape(arr.shape)
    return new_arr
def trans2matrix(data):
    la_bg=15.0
    lo_bg=-20.0
    res=np.zeros((100,100))
    # print(res.shape)
    for i in range(725):
        v=data[i][2]
        x=data[i][0]
        y=data[i][1]
        if(x>=64.5):
            # print(x)
            xn=99
        else:
            xn=int((x-la_bg)/0.5)
        if(y>=9.7):
            yn=99
        else:
            yn=round((y-lo_bg)/0.3)
        if(v>500):
            v=500
        res[xn][yn]=v
    return res 

# heat = np.loadtxt("testCA/heatData.txt")
# suitable temperature
SUIT_TEMP=5
# temperature coefficient dicides the temperature sensibility
TEMP_COEF=0.05
k = 8
years=50
n=100
h=np.ones((100,100))
h_l=np.ones((100,100))
f=trans2matrix(dt.f_sb)
f_l=trans2matrix(dt.f_sb)
m=np.array(dt.mp)
t=dt.t
# f=flip180(f)
# m=flip180(m)
m=np.flipud(m)
t=np.array(t)
print(t)
# t=np.flipud(t)
# t=np.flipud(t)
print(t)
# t=flip180(t)
# t_l=[]
color_table = [(25,25,112),(0,0,255),(0,180,255),(0,250,154),(0,255,0),(173,255,47),(255,255,0),(255,165,0),(255,69,0),(255,0,0)]
def fishGenerator():
    for x in range(n):
        for y in range(n):
            CON,max_d=congestion(x,y,25)
            if(f[x][y]>0 and m[x][y]!=-1 and f[x][y]<100):
                f[x][y]=int(f[x][y]+CON*h[x][y]*(1/max_d))
# def fishGenerator(coef):
#     flag=np.zeros((100,100))
#     for x in range(n):
#         for y in range(n):

#             if(f[x][y]>0):
#                 for nx in range(x-coef,x+coef):
#                     for ny in range(y-coef,y+coef):
#                         # print(nx,ny)
#                         if(nx<0 or nx>99 or ny<0 or ny>99 or flag[nx][ny]==-1):
#                             pass
#                         else:
#                             diff=abs(nx-x)+abs(ny-y)
#                             if(nx==x and ny==y):
#                                 None
#                             else:
#                                 if(m[nx][ny]!=-1 and f[nx][ny]<1000):
#                                     # print([nx,ny])
#                                     f[nx][ny]=int(f[nx][ny]+(1/diff*diff)*f[x][y])
#                                     flag[nx][ny]=-1


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
                CONGESTION,MAXD=congestion(x,y,1)
                t[x][y]=t[x][y]+2.5/years
                # population varible
                if(POPULATION!=0):
                    acc_pop=(POPULATION-POPULATION_L)/POPULATION
                else:
                    acc_pop=0

                if(OFFSHORE!=0):
                    index_offs=(OFFSHORE/80)**(1/40)
                elif(OFFSHORE==0):
                    index_offs=0.85
                # if((POPULATION<(CONGESTION/9))
                # index_pop=math.exp(-1*acc_pop)-(POPULATION-CONGESTION/9)/2
                index_pop=(POPULATION-CONGESTION/9)/2
                diff=TEMPERATURE-SUIT_TEMP
                if(diff<3):
                    index_temp=1+abs(diff)*TEMP_COEF*0.5
                else:
                    index_temp=1-abs(diff)*TEMP_COEF*0.5
                index=index_offs*index_temp
                if(index>1.2):
                    h[x][y]=1.4
                elif(index<0.8):
                    h[x][y]=0.6
                else:
                    h[x][y]=index

    return
    
def congestion(x,y,coef):
    fsum=0
    max_v=0
    max_d=0.5
    for nx in range(x-coef,x+coef):
        for ny in range(y-coef,y+coef):
            if(nx>99 or nx<0 or ny<0 or ny>99):
                None
            else:
                if(m[nx][ny] != -1):
                    fsum = fsum + f[nx][ny]
                if(f[nx][ny]>max_v):
                    max_d=abs(nx-x)+abs(ny-y)+0.5
    return fsum,max_d


#visual(f)
def fishCAMain(year):
    # myf=np.array(f)
    fishGenerator()
    n=100
    for i in range(year):
        for x in range(n):
            for y in range(n):
                f_l[x][y]=f[x][y]
                if (m[x][y]!=-1): 
                    f[x][y]=round(f[x][y]*h[x][y])
                    # print("to be or not to be")
                if(f[x][y]>500):
                    f[x][y]=500
        hsi()
        # print(i,"year")

    

# def color():
#     max_v=0
#     for x in range(n):
#         for y in range(n):
#             if(f[x][y]>max_v):
#                 max_v=f[x][y]


#           
def init():
    # hsi()
    # fishGenerator(20)
    
    for x in range(n):
        for y in range(n):
            if(m[x][y]!=-1):
                f_l[x][y]=round(f[x][y]*(1+rd.random()/10*(-1)**(rd.randint(-1,0))))
            else:
                f[x][y]=-500
                h[x][y]=-500
    # hsi()



# t=flip180(t)
init()
f_bg=f
centroids1, clusterData1 = km.kmeans(km.trans2coordinate(f_bg), k)
mat_path = 'startCAData.mat'
io.savemat(mat_path, {'name': f_bg})
fishCAMain(years)
print(f)
f_ed=f
mat_path = 'finalCAData.mat'
io.savemat(mat_path, {'name': f_ed})
mat_path = 'hdata.mat'
io.savemat(mat_path, {'name': h})
mat_path = 'mdata.mat'
io.savemat(mat_path, {'name': m})
mat_path = 'fldata.mat'
io.savemat(mat_path, {'name': f_l})
mat_path = 'tfldata.mat'
io.savemat(mat_path, {'name': t})


centroids1, clusterData1 = km.kmeans(km.trans2coordinate(f_bg), k)
centroids2, clusterData2 = km.kmeans(km.trans2coordinate(f_ed), k)
oneCent1=km.selectCentVM(centroids1,k)
oneCent2=km.selectCentVM(centroids2,k)
bg2ed=km.getDistance(oneCent1[0],oneCent1[1],oneCent2[0],oneCent2[1])
bg2p=km.getDistance(oneCent1[0],oneCent1[1],57,2.3)
ed2p=km.getDistance(oneCent2[0],oneCent2[1],57,2.3)
percent=oneCent2[2]/oneCent1[2]
# pos_bg=[centroids1[0][0],centroids1[0][1]]
# pos_ed=[centroids2[0][0],centroids2[0][1]]
if np.isnan(centroids1).any() and np.isnan(centroids2).any():
    print('Error')
else:
    print("k =",k)
    print(centroids1)
    print(centroids2)
    print("Distance_bg2ed =",bg2ed)
    print("Distance_bg2port =",bg2p)
    print("Distance_ed2port =",ed2p)
    print("harvest percent =",percent)
    print("min distance bg2port =",)
    print("min distance ed2port =",)
