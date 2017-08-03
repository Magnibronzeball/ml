from math import log
import operator
#计算香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[ currentLabel] = 0
        labelCounts[currentLabel]+= 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float( labelCounts[ key])/ numEntries
        shannonEnt -= prob*log( prob, 2)
    return shannonEnt

#划分结果集
def splitDataSet( dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend( featVec[axis+ 1:])
            retDataSet.append( reducedFeatVec)
    return retDataSet

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    #创建唯一的分类标签列表
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        #计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        #计算最好的信息增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


#创建决策树
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0] #类别完全相同则停止继续划分
    if len(dataSet[0]) == 1: #遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]  #得到列表包含的所有属性值
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

#创建数据集
def createDataSetFromTXT(filename):
    dataSet = []; labels = []
    fr = open(filename)
    linenumber=0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.strip().split()
        lineset = []
        for cel in listFromLine:
            lineset.append(cel)

        if(linenumber==0):
            labels=lineset
        else:
            dataSet.append(lineset)

        linenumber = linenumber+1
    return dataSet,labels

#计算香农熵
print(calcShannonEnt([[1,1,'yes'], [1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]))