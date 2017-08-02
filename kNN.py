from numpy import *
import operator
def createDataSet():
    group = array([[ 1.0, 1.1],[ 1.0, 1.0],[ 0, 0],[ 0, 0.1]])
    labels = ['A',' A',' B',' B']
    print(group)
    print(labels)
    return group, labels

def classify0( inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    aa= tile(inX,(dataSetSize,1))
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    aa=2**0.5
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range( k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount. get(voteIlabel, 0) + 1
    classCount.items()
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse= True)
    cc=sortedClassCount[0][0]
    return sortedClassCount[0][0]

print(classify0([100,1000],array([[ 1.0, 1.1],[ 1.0, 1.0],[ 0, 0],[ 0, 0.1]]),['A',' A',' B',' B'],3))