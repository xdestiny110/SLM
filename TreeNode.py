#-*- coding:utf-8 -*-
import numpy as np

class TreeNode:
    def __init__(self):
        self.parent = None
        self.child = []
        self.data = []
        self.depth = 0
    def addChild(self, node):
        self.child.append(node)
        node.parent = self
        node.depth = self.depth+1
    def removeChild(self, node):
        self.child.remove(node)
        node.parent = None
        node.depth = 0

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
    # data中第一个值对应结果是多少
    # child有值时，data第二个值代表处理的是第几个feature，第三个值代表在该feature上的切分点是多少
    # 保证左子节点是小于切分点，大于切分店是在右子节点
    # child个数始终为2个
    # train_data表示该节点上的训练数据

    def __init__(self):
        TreeNode.__init__(self)
        self.train_data = np.array([])
        self.label = np.array([])
    def predict(self, feature):
        if len(self.child) > 0:
            if feature[self.data[1]] > self.data[2]:
                return self.child[1].predict(feature)
            else:
                return self.child[0].predict(feature)
        return self.label