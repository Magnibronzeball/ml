import ID3
import treePlotter
#导入决策树
Tree=ID3.grabTree("tree.txt")
print(Tree)
#给labels=['T1','T5']，testVec=['0.75','0.25']进行分类
labels=['T1','T5']
print(ID3.classify(Tree,labels,['0.75','0.5']));
treePlotter.createPlot(Tree)
