#-*- coding:utf-8 -*-
import numpy as np

class TreeNode:
    def __init__(self):
        self.parent = None
        self.child = []
        self.data = []
    def addChild(self, node):
        self.child.append(node)
        node.parent = self
    def removeChild(self, node):
        self.child.remove(node)
        node.parent = None

class DecisionTreeNode(TreeNode):
    # data中第一个值保存的为对应label
    # child有值时，data第二个值表示处理的是第几个feature
    # child的个数为处理feature的取值个数
    # train_data表示该节点上的训练数据
    # label表示该节点上训练数据对应的标签

    def __init__(self):
        TreeNode.__init__(self)
        self.train_data = np.array([])
        self.label = np.array([])
    def predict(self, feature):
        if len(self.child) > 0:
            return self.child[feature[self.data[1]]].predict(feature)
        return self.data[0]
    def visualize(self):
        nodes = [self]
        while(nodes != []):
            if nodes[0].child != []:
                print('选择特征：%s'%(str(nodes[0].data[1])))
                nodes += nodes[0].child
            nodes.remove(nodes[0])

class RegressionTreeNode(TreeNode):
    def __init__(self):
        TreeNode.__init__(self)
        