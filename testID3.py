import ID3
import treePlotter

if __name__ == '__main__':
    pass

myDat,labels = ID3.createDataSetFromTXT("dataset.txt")

#计算香农熵
shan = ID3.calcShannonEnt(myDat)
print(shan)

col = ID3.chooseBestFeatureToSplit(myDat)
print(col)

#生成决策树
Tree = ID3.createTree(myDat, labels)
print(Tree)

#保存决策树
ID3.storeTree( Tree, "tree.txt")

#导入决策树
print(ID3.grabTree("tree.txt"))

#生成图形
treePlotter.createPlot(Tree)