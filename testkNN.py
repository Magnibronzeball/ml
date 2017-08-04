import kNN
from numpy import *
import matplotlib
import matplotlib. pyplot as plt
#获取训练数据
datingDataMat, datingLabels=kNN.file2matrix('datingTestSet2.txt')
print('zz')
print(datingLabels)
#获取[68607,9.661909,0.350772]的分类，K=3
print(kNN.classify0([1,9.661909,0.350772],datingDataMat,datingLabels,3))

#生成图形（矩阵的第一列为横轴和第二列为纵轴）
fig = plt. figure()
ax = fig. add_subplot( 111)
#ax. scatter( datingDataMat[:, 0], datingDataMat[:, 1], 15.0* array( datingLabels), 1000.0* array( datingLabels))
ax. scatter( datingDataMat[:, 0], datingDataMat[:, 1], c=1.0*array( datingLabels),s=15.0* array( datingLabels),marker="v")
plt. show()