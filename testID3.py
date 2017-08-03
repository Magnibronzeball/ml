import ID3
import treePlotter

if __name__ == '__main__':
    pass

myDat,labels = ID3.createDataSetFromTXT("dataset.txt")

shan = ID3.calcShannonEnt(myDat)
print(shan)

col = ID3.chooseBestFeatureToSplit(myDat)
print(col)

Tree = ID3.createTree(myDat, labels)
print(Tree)

treePlotter.createPlot(Tree)