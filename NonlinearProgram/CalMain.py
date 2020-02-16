import kMeans as km
import fishCA as ca
import fishData as dt
import numpy as np
import random as rd

# def TempHarvest(ft,k):
#     # t_p=np.array([[0,1]])
#     temp=0.02
#     for t in range(100):
#         percent_sum=0
#         for i in range(2):
#             while(1):
#                 f=ca.fishCAMain(ft,dt.t,dt.year,0.001)
#                 f_bg=np.array(ft)
#                 f_ed=np.array(f)
#                 centroids1, clusterData1 = km.kmeans(km.trans2coordinate(f_bg), k)
#                 centroids2, clusterData2 = km.kmeans(km.trans2coordinate(f_ed), k)
#                 oneCent1=km.selectCent(centroids1,k)
#                 oneCent2=km.selectCent(centroids2,k)
#                 bg2ed=km.getDistance(oneCent1[0],oneCent1[1],oneCent2[0],oneCent2[1])
#                 bg2p=km.getDistance(oneCent1[0],oneCent1[1],54,0.5)
#                 ed2p=km.getDistance(oneCent2[0],oneCent2[1],54,0.5)
#                 # percent=oneCent2[2]/10
#                 percent=oneCent2[2]/oneCent1[2]
#                 if( percent>=1 or bg2p>=ed2p or oneCent1[0]<oneCent2[0]):
#                     # print("err!")
#                     None
#                 else:
#                     # print("k =",k)
#                     # print("Distance_bg2ed =",bg2ed)
#                     # print("Distance_bg2port =",bg2p)
#                     # print("Distance_ed2port =",ed2p)
#                     # print("harvest percent =",percent)
#                     percent_sum=percent_sum+percent
#                     break
#         pm=percent_sum/2
#         print([temp,pm])
#         temp=temp+0.002
#     return [bg2ed,bg2p,ed2p,percent]

# def YearDist(ft,k):
#     # t_p=np.array([[0,1]])
#     dis_glb_max=50
#     for year in range(50):
#         dis_max=0
#         while(1):
#             f=ca.fishCAMain(ft,dt.t,dt.year,0.001)
#             f_bg=np.array(ft)
#             f_ed=np.array(f)
#             centroids1, clusterData1 = km.kmeans(km.trans2coordinate(f_bg), k)
#             centroids2, clusterData2 = km.kmeans(km.trans2coordinate(f_ed), k)
#             oneCent1=km.selectCent(centroids1,k)
#             oneCent2=km.selectCent(centroids2,k)
#             bg2p=km.getDistance(oneCent1[0],oneCent1[1],54,0.5)
#             ed2p=km.getDistance(oneCent2[0],oneCent2[1],54,0.5)
#             # oneCent2=km.selectCent(centroids2,k)
#             # oneCent2=centroids2[rd.randint(0,k-1)]
#             # ed2p=km.getDistance(oneCent2[0],oneCent2[1],54,0.5)
#             # print(dis)
#             if( dis>dis_glb_max and (dis-dis_glb_max)<=30):
#                 dis_glb_max=dis
#                 if(dis>dis_max):
#                     dis_max=dis
#                     break
#             else:
#                 None
#         print([year,dis_max])
    # return [bg2ed,bg2p,ed2p,percent]
def TempMove(ft,k):
    ms=0
    for i in range(100):
        while(1):
            f_bg=np.array(ft)
            f=ca.fishCAMain(ft,dt.t,dt.year,0.075)
            f_ed=np.array(f)
            centroids1, clusterData1 = km.kmeans(f_bg, k)
            centroids2, clusterData2 = km.kmeans(f_ed, k)
            oneCent1=km.selectCent(centroids1,k)
            oneCent2=km.selectCent(centroids2,k)
            dis1=km.getDistance(oneCent1[0],oneCent1[1],57,2.3)
            dis2=km.getDistance(oneCent2[0],oneCent2[1],57,2.3)
            if(dis2>dis1):
                ms=ms+dis2-dis1
                print(dis2-dis1)
                break
    ms=ms/100
    print("means of moving distance =",ms)
    return ms

k = 8
ft=dt.f1
TempMove(ft,k)
# YearDist(ft,k)
# f_end=ca.fishCAMain(ft,dt.t,dt.year,0.05)
# print(f_end)
# ca.visual(f_end,20)

# tempMove data:
# 0.05:91.47,97.82,96.3
# 0.03:88.2，81.53.
