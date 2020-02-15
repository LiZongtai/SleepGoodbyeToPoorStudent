from PIL import Image
import numpy as np
import random as rd

n = 20
year = 50

f1 = [[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[-1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,9,1,1,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,5,1,1,5,1,1,1,7,1,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,7,9,1,1,1,1,1,0,0],
[0,0,0,0,0,0,1,1,1,1,1,9,2,1,0,1,5,1,0,0],
[0,0,0,0,0,0,1,7,3,1,1,1,1,1,1,1,1,1,0,0],
[0,0,0,0,1,1,1,5,2,3,1,1,3,4,2,1,1,2,1,1],
[0,0,0,0,1,3,1,1,1,1,1,2,2,1,1,1,1,2,2,1],
[0,0,0,0,1,1,1,2,3,1,1,5,1,2,1,1,5,1,1,-1],
[0,0,0,0,0,0,1,1,1,1,1,1,1,4,1,1,4,-1,-1,-1],
[0,0,0,0,0,0,0,0,0,1,6,4,1,2,1,0,-1,-1,-1,-1],
[0,0,0,0,0,0,0,0,0,1,2,1,1,1,1,0,-1,-1,-1,-1],
[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,-1,-1,0],
[0,0,0,0,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,0],
[1,1,1,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,-1,0],
[2,2,1,0,0,0,0,0,-1,-1,0,0,-1,0,0,0,0,0,-1,-1],
[1,1,1,0,0,0,0,0,-1,-1,0,-1,-1,-1,0,0,-1,-1,-1,-1],
[0,0,0,0,0,0,0,-1,0,0,0,-1,-1,-1,0,-1,-1,-1,-1,-1]]

f=[[-1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
[-1,0,0,0,0,0,0,1,1,3,3,3,1,2,1,1,1,0,0,0],
[1,1,0,1,1,1,1,1,2,3,5,8,2,3,2,3,1,1,0,0],
[2,1,1,1,3,1,1,2,1,1,3,2,3,1,2,3,2,1,0,0],
[6,2,3,3,1,1,1,2,1,1,1,1,3,3,3,2,2,1,0,0],
[2,1,2,2,1,5,1,2,1,2,1,1,2,1,1,2,2,1,1,0],
[1,1,2,2,1,1,3,1,3,2,1,1,5,2,2,1,2,3,1,1],
[0,1,5,2,1,3,3,3,1,1,2,2,3,3,1,7,2,7,3,3],
[0,1,1,1,1,6,1,1,3,2,1,1,1,2,3,2,1,8,3,9],
[0,0,0,1,2,2,1,3,1,3,1,1,3,2,8,3,3,5,6,-1],
[0,0,0,1,1,1,1,1,2,1,2,1,2,1,2,6,6,-1,-1,-1],
[0,0,0,0,0,1,1,1,1,2,1,2,1,1,2,9,-1,-1,-1,-1],
[0,0,0,0,0,1,2,3,1,2,2,2,2,2,2,3,-1,-1,-1,-1],
[0,0,0,0,0,1,1,1,3,1,2,3,1,1,1,2,2,-1,-1,1],
[1,1,1,1,1,0,0,1,2,1,-1,-1,1,1,1,4,2,7,3,2],
[2,1,1,3,1,0,0,1,1,1,-1,-1,3,1,2,4,1,3,-1,2],
[2,5,3,3,1,0,0,0,0,1,3,-1,2,3,1,2,1,4,-1,2],
[1,2,3,3,1,1,1,0,-1,-1,1,2,-1,4,1,1,3,4,-1,-1],
[0,1,2,2,2,2,1,1,-1,-1,1,-1,-1,-1,3,1,-1,-1,-1,-1],
[1,1,7,9,7,8,3,-1,1,5,8,-1,-1,-1,3,-1,-1,-1,-1,-1]]
# fish
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
[9,9,9,9,9,12,12,11,9,9,9,-1,8,7,7,7,7,6,-1,5],
[10,11,12,12,12,12,11,9,-1,-1,7,9,-1,9,7,7,8,9,-1,-1],
[11,12,12,12,12,12,11,9,-1,-1,9,-1,-1,-1,8,8,-1,-1,-1,-1],
[12,12,12,12,12,12,12,-1,8,7,8,-1,-1,-1,9,-1,-1,-1,-1,-1]]
# temp

dr = 0.2
#death rate large - die more

br = 0.3
#born rate  small - born less

starve_bar = 20
#too much fish, I die

stuffed_bar = 7
#all the food will be mine

color_table = [(25,25,112),(0,0,255),(0,180,255),(0,250,154),(0,255,0),(173,255,47),(255,255,0),(255,165,0),(255,69,0),(255,0,0)]


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
                        img_array[px, py] = (96,96,96)
                    else:
                        img_array[px, py] = color_table[ data[ int(x/block_size) ][ int(y/block_size) ]  ]

    img = Image.fromarray(img_array)
    img.save('img/'+str(cur_y)+'.jpg')


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
                        img_array[px, py] = (96,96,96)
                    else:
                        img_array[px, py] = color_table[ data[ int(x/block_size) ][ int(y/block_size) ]  ]

    img = Image.fromarray(img_array)
    img.show()
    
#visual(f)

for i in range(year):
    for x in range(n):
        for y in range(n):
            # Let us go through the map
            
            if(f[x][y] != -1):
            # If not continent, cuz I don't wanna be Columbus
                # if(rd.random() < br and f[x][y]!= 9 and f[x][y] > 0):
                if(f[x][y]!=9 and f[x][y]>0):
                # wake up, my fish
                    f[x][y] =  round(f[x][y]*(br+1))
                    if(f[x][y]>9):
                        f[x][y]=9
                    
                if( f[x][y]>0):
                # RIP: my fish
                    f[x][y] = f[x][y] - int(dr*t[x][y])
                    if(f[x][y]<0):
                        f[x][y]=0
                    
                fsum = 0
                for nx in range(x-1,x+1):
                    for ny in range(y-1,y+1):
                    # Let me take a look around
                        if(f[nx][ny] != -1):
                        # I am not Columbus 
                            fsum = fsum + f[nx][ny]
                            # Hi,bro
                        else:
                            fsum=fsum+1
                            
                if(fsum > starve_bar):
                # Food, food! Ahhhhhhhh RIP
                    for nx in range(x-1,x+1):
                        for ny in range(y-1,y+1):
                        # You wanna live? Over my dead body!
                            if(f[nx][ny] >2 ):
                            # Only big fish hava food problem 
                                f[nx][ny] = f[nx][ny] - rd.randint(0,3)
                                # Go down with me!
                                
                elif(fsum < stuffed_bar and fsum > 4):
                # RAP: I ate to much food, and I am now very full.
                    for nx in range(x-1,x+1):
                        for ny in range(y-1,y+1):
                        # Wanna share some food, haha.
                            if(f[nx][ny] != -1 and f[nx][ny] != 9 and rd.random() > br):
                            # Continents can't eat. Fat fish can't eat.
                                f[nx][ny] = f[nx][ny] + 1
                                # Be my guest
                
                
                                
        
                
    # Global warming, YEAH.
    for x in range(n):
        for y in range(n):
            # Let us go through the map
            if(t[x][y] != -1):
                # not Continent
                t[x][y] = t[x][y] + 0.1
                # Global warming coef need to be small
    # Scottish great catch
    for x in range(n):
        for y in range(n):
            # Let us go through the map
            if(f[x][y] >5):
                # not Continent
                f[x][y] = f[x][y] - rd.randint(0,2)
                # 
    visual_gif(f,i)


#visual(f)
         
            
'''
for x in range(n):
    for y in range(n):
        if(t[x][y]!=-1):
            t[x][y] = 9
visual(t)
'''
