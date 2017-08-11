#训练数据
def loadDataSet():
    postingList=[[' my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how',' to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1] #1 代表 侮辱性 文字， 0 代表 正常 言论
    return postingList, classVec

#对数据集进行排重，并返回
def createVocabList( dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set( document)
    return list( vocabSet)

def setOfWords2Vec( vocabList, inputSet):
    returnVec = [0]* len( vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[ vocabList. index( word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


listOPosts, listClasses = loadDataSet()
myVocabList=createVocabList( listOPosts)
print(myVocabList)
print( listOPosts[ 0])
print(setOfWords2Vec( myVocabList, listOPosts[ 0]))
print(setOfWords2Vec( myVocabList, listOPosts[ 3]))