# import numpy as np
# data = np.loadtxt("testCA/heatData.txt")   #将文件中数据加载到data数组里
# # print(data)

# def rotate(array):
#     temp = np.zeros_like(array.transpose())
#     for j in range(len(array)):
#         for i in range(len(array[0])):
#             temp[i][j] = array[j][len(array[0])-i-1]/100
#             if (temp[i][j]==-99.99):
#                 temp[i][j]=-1
#     return temp
# def cut(data):
#     for i in range(51):
#         data = np.delete(data,0,1)
#     for i in range(165):
#         data = np.delete(data,0,0)
#     # print(data)
#     # jd,wd=data.shape
#     # print(jd,wd)
#     for i in range(25,38):
#         data = np.delete(data,25,1)
#     for i in range(21,1991):
#         data = np.delete(data,21,0)
#     data=rotate(data)
#     return data
# print(cut(data))
