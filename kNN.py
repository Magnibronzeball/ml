from numpy import *
import operator
def createDataSet():
    group = array([[ 1.0, 1.1],[ 1.0, 1.0],[ 0, 0],[ 0, 0.1]])
    labels = ['A',' A',' B',' B']
    print(group)
    print(labels)
    return group, labels

#分类
def classify0( inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range( k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount. get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse= True)
    cc=sortedClassCount[0][0]
    return sortedClassCount[0][0]

#从文件得到矩阵
def file2matrix( filename):
    fr = open( filename)
    arrayOlines= fr.readlines()
    numberOfLines = len( arrayOlines)
    returnMat = zeros(( numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOlines:
        line = line. strip()
        listFromLine = line.split('\t')
        returnMat[ index,:] = listFromLine[ 0: 3]
        classLabelVector. append( int( listFromLine[- 1]))
        index += 1
    return returnMat, classLabelVector



#print(classify0([100,1000],array([[ 1.0, 1.1],[ 1.0, 1.0],[ 0, 0],[ 0, 0.1]]),['A',' A',' B',' B'],3))