import numpy as np
import math
import matplotlib.pyplot as plt

# fish distribution begin state
f_bg=np.array ([
[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
[0,0,0,0,0,0,0,-1,0,0,0,-1,-1,-1,0,-1,-1,-1,-1,-1]])
# end state
f_ed=np.array ([
    [-1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [-1, 7, 8, 5, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 3, 0, 0, 0, 0], 
    [6, 2, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 0, 6, 0, 0, 0, 0], 
    [1, 8, 1, 5, 0, 0, 0, 0, 4, 0, 0, 5, 1, 0, 0, 0, 0, 0, 0, 0], 
    [7, 1, 5, 0, 5, 2, 0, 0, 5, 0, 1, 5, 5, 1, 0, 0, 0, 0, 0, 0], 
    [8, 0, 4, 5, 0, 7, 5, 5, 5, 0, 1, 2, 0, 0, 0, 0, 7, 0, 0, 0], 
    [0, 0, 3, 0, 2, 3, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 5, 1, 5, 0, 4, 5, 5, 5, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [9, 1, 1, 6, 5, 5, 4, 1, 4, 1, 0, 5, 2, 5, 1, 0, 0, 0, 0, 0], 
    [0, 7, 8, 0, 0, 0, 0, 1, 3, 1, 1, 4, 0, 2, 1, 0, 0, 0, 0, -1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 5, 0, 0, 0, -1, -1, -1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1], 
    [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1, -1, -1, 0, 0, -1, -1, -1, -1], 
    [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1]])

def trans2coordinate(f):
    la_bg=52.5
    lo_bg=-5.0
    mydata=np.array([[0.,0.,0.]])
    la_num,lo_num=f.shape
    for i in range(la_num):
        for j in range(lo_num):
            if(f[i][j]>0):
                # print([[la_bg+i*0.5,lo_bg+j*0.5,f[i][j]]])
                mydata=np.append(mydata,[[la_bg+i*0.5,lo_bg+j*0.5,f[i][j]]],axis=0)
    mydata=np.delete(mydata, 0, 0)
    return mydata 

# calculate distance
def euclDistance(vector1, vector2):
    return np.sqrt(sum((vector2 - vector1) ** 2))
# initiate centroids
def initCentroids(data, k):
    numSamples, dim = data.shape
    # k centroids
    centroids = np.zeros((k, dim))
    # random centroids
    for i in range(k):
        # random index from Samples
        index = int(np.random.uniform(0, numSamples))
        # initial centroid
        centroids[i, :] = data[index, :]
    return centroids

# read data set and k-value
def kmeans(data, k):
    # calculate nums of samples
    numSamples = data.shape[0]
    clusterData = np.array(np.zeros((numSamples, 2)))
    # decide whether change the centroids
    clusterChanged = True
    # initiate centroids
    centroids = initCentroids(data, k)
    while clusterChanged:
        clusterChanged = False
        for i in range(numSamples):
            minDist = 100000.0
            minIndex = 0
            for j in range(k):
                distance = euclDistance(centroids[j, :], data[i, :])
                if distance < minDist:
                    minDist = distance
                    # reflash the index
                    minIndex = j
            if clusterData[i, 0] != minIndex:
                clusterChanged = True
                clusterData[i, 0] = minIndex
        for j in range(k):
            cluster_index = np.nonzero(clusterData[:, 0] == j)
            pointsInCluster = data[cluster_index]
            centroids[j, :] = np.mean(pointsInCluster, axis=0)
    return centroids, clusterData
    
# # visible
# def showCluster(data, k, centroids, clusterData):
#     numSamples, dim = data.shape
#     if dim != 2:
#         print('dimension of your data is not 2!')
#         return 1
#     mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'dr', '<r', 'pr']
#     if k > len(mark):
#         print('your k is too large!')
#         return 1
#     for i in range(numSamples):
#         markIndex = int(clusterData[i, 0])
#         plt.plot(data[i, 0], data[i, 1], mark[markIndex])
#     mark = ['*r', '*b', '*g', '*k', '^b', '+b', 'sb', 'db', '<b', 'pb']
#     for i in range(k):
#         plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=20)
#     plt.show()

# calculate real distance (km)
EARTH_REDIUS = 6378.137
def rad(d):
    return d * math.pi / 180.0
def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s
# select centroids - value maximum
def selectCent(cents,k):
    max_v=0
    max_i=0
    for i in range(k):
        if(cents[i][2]>=max_v):
            max_v=cents[i][2]
            max_i=i
    oneCent=[cents[max_i][0],cents[max_i][1],cents[max_i][2]]
    return oneCent

k = 1
centroids1, clusterData1 = kmeans(trans2coordinate(f_bg), k)
centroids2, clusterData2 = kmeans(trans2coordinate(f_ed), k)
oneCent1=selectCent(centroids1,k)
oneCent2=selectCent(centroids2,k)
bg2ed=getDistance(oneCent1[0],oneCent1[1],oneCent2[0],oneCent2[1])
bg2p=getDistance(oneCent1[0],oneCent1[1],54,0.5)
ed2p=getDistance(oneCent2[0],oneCent2[1],54,0.5)
percent=oneCent2[2]/oneCent1[2]
pos_bg=[centroids1[0][0],centroids1[0][1]]
pos_ed=[centroids2[0][0],centroids2[0][1]]
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

# showCluster(f, k, centroids, clusterData)
# print(trans2coordinate(f))