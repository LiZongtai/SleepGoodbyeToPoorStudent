year=50
tcoef=0.1
# fish
# herring
f1 = [[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[-1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,9,1,1,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,5,1,1,5,1,1,1,7,1,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,7,9,1,1,1,1,1,0,0],
[0,0,0,0,0,0,1,1,1,1,1,9,2,1,0,1,5,1,0,0],
[0,0,0,0,0,0,1,7,3,1,1,1,1,1,1,1,1,1,0,0],
[0,0,0,-1,-1,1,1,5,2,3,1,1,3,4,2,1,1,2,1,1],
[-1,-1,-1,-1,-1,3,1,1,1,1,1,2,2,1,1,1,1,2,2,1],
[0,-1,-1,0,1,1,1,2,3,1,1,5,1,2,1,1,5,1,1,-1],
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

# markrel
f2=[[-1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
[-1,0,0,0,0,0,0,1,1,3,3,3,1,2,1,1,1,0,0,0],
[1,1,0,1,1,1,1,1,2,3,5,8,2,3,2,3,1,1,0,0],
[2,1,1,1,3,1,1,2,1,1,3,2,3,1,2,3,2,1,0,0],
[6,2,3,3,1,1,1,2,1,1,1,1,3,3,3,2,2,1,0,0],
[2,1,2,2,1,5,1,2,1,2,1,1,2,1,1,2,2,1,1,0],
[1,1,2,2,1,1,3,1,3,2,1,1,5,2,2,1,2,3,1,1],
[0,1,5,-1,-1,3,3,3,1,1,2,2,3,3,1,7,2,7,3,3],
[-1,-1,-1,-1,-1,6,1,1,3,2,1,1,1,2,3,2,1,8,3,9],
[0,-1,-1,1,2,2,1,3,1,3,1,1,3,2,8,3,3,5,6,-1],
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
# temp
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
