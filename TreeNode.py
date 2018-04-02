#-*- coding:utf-8 -*-

class TreeNode:
    def __init__(self):
        self.parent = None
        self.child = []
        self.data = None

class DecisionTreeNode(TreeNode):
    # 当child为空时，data中保存的为对应label
    # child有值时，data表示处理的是第几个feature
    # child的个数为处理feature的取值个数

    def __init__(self):
        TreeNode.__init__(self)
    def predict(self, feature):
        if len(self.child) > 0:
            return self.child[feature[self.data].predict(feature)
        return self.data
