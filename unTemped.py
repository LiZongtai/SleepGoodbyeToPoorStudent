from PIL import Image
import numpy as np
import random as rd

n = 20
year = 50
temp_bar=40

t = [[-1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,3,3,3],
[-1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,3,3,4,5],
[0,0,0,0,1,1,1,1,1,1,1,1,1,2,5,5,5,5,5,5],
[0,0,0,1,1,1,1,1,1,1,2,2,5,6,7,6,5,5,6,7],
[0,0,1,1,1,2,3,3,3,3,4,5,5,5,5,7,7,7,7,7],
[0,1,1,1,1,1,2,3,3,5,5,6,7,6,5,5,5,7,7,7],
[4,3,3,3,2,2,1,1,2,5,5,5,6,6,7,7,7,8,8,7],
[5,5,1,-1,-1,3,3,3,3,4,5,6,7,7,9,7,7,9,8,7],
[-1,-1,-1,-1,-1,5,5,6,5,5,5,5,6,7,7,7,9,8,7,8],
[7,-1,-1,7,9,9,8,7,6,5,5,5,6,7,7,8,8,7,8,-1],
[9,9,9,9,9,9,9,9,9,8,7,7,7,7,8,8,8,-1,-1,-1],
[9,9,9,9,9,9,9,9,9,8,9,9,9,9,9,7,-1,-1,-1,-1],
[9,9,9,9,9,9,9,9,9,9,9,9,9,8,9,7,-1,-1,-1,-1],
[9,9,9,9,9,9,12,12,12,9,9,9,9,7,7,7,8,-1,-1,8],
[9,9,9,9,11,9,12,12,9,9,-1,-1,9,7,7,7,7,7,7,7],
[9,9,9,9,9,11,12,12,9,9,-1,-1,7,7,7,7,7,7,-1,5],
[9,9,9,9,9,12,12,11,9,9,9,-2,8,7,7,7,7,6,-1,5],
[10,11,12,12,12,12,11,9,-1,-1,7,9,-1,9,7,7,8,9,-1,-1],
[11,12,12,12,12,12,11,9,-1,-1,9,-1,-1,-1,8,8,-1,-1,-1,-1],
[12,12,12,12,12,12,12,-1,8,7,8,-1,-1,-1,9,-1,-1,-1,-1,-1]]
# temp


color_table = [(25,25,112),(0,0,112),(0,0,255),(0,60,255),(0,120,255),(0,180,255),(0,255,255),(0,255,200),(0,255,160),(0,255,60),(0,255,0),(60,255,0),(173,255,0),(200,255,0),(255,255,0),(255,200,0),(255,165,0),(255,100,0),(255,90,0),(255,69,0),(255,30,0),(255,15,0),(255,0,0)]


def visual_gif(data,cur_y):

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
                        img_array[px, py] = (140,140,140)
                    elif(data[ int(x/block_size) ][ int(y/block_size) ] == -2):
                        img_array[px, py] = (255,255,255)
                    else:
                        img_array[px, py] = color_table[ int( data[ int(x/block_size) ][ int(y/block_size) ] ) ]

    img = Image.fromarray(img_array)
    img.save('img/tmp/'+str(cur_y)+'.jpg')


def visual(data):

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
                        img_array[px, py] = (140,140,140)
                    elif(data[ int(x/block_size) ][ int(y/block_size) ] == -2):
                        img_array[px, py] = (255,255,255)
                    else:
                        img_array[px, py] = color_table[ int( data[ int(x/block_size) ][ int(y/block_size) ] ) ]

    img = Image.fromarray(img_array)
    img.show()
    
            
#visual(t)

s = 0.01
for i in range(year):
    for x in range(n):
        for y in range(n):
            if(t[x][y]!=-1 and t[x][y]!=-2):
                tsum = 0
                for nx in range(x-1,x+1):
                    for ny in range(y-1,y+1):
                    # Let me take a look around
                        if(t[nx][ny] != -1):
                        # I am not Columbus 
                            tsum = tsum + t[nx][ny]
                            # Hi,bro
                        else:
                            tsum=tsum+1
                tsum = tsum-t[x][y]
                # print(tsum)
                if(tsum > t[x][y]):
                    t[nx][ny] = t[nx][ny] + 0.1
                    if(t[nx][ny]>20):
                        t[nx][ny] = t[nx][ny]=20
                # # Food, food! Ahhhhhhhh RIP
                #     for nx in range(x-1,x+1):
                #         for ny in range(y-1,y+1):
                #         # You wanna live? Over my dead body!
                #             if(t[nx][ny] >0 ):
                #             # Only big fish hava food problem 
                #                 t[nx][ny] = t[nx][ny] + rd.random()
                #                 # Go down with me!
                
    visual_gif(t,i)
# visual(t)