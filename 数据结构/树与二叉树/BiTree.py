# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/10 22:25
from collections import deque


class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None#左孩子
        self.rchild = None#右孩子
    @staticmethod
    #前序遍历，先自己，递归左子树，再递归右子树
    def pre_order(root):
        if root:
            print(root.data,end=",")
            BiTreeNode.pre_order(root.lchild)
            BiTreeNode.pre_order(root.rchild)

    # 中序遍历，递归左子树，自己，再递归右子树
    @staticmethod
    def in_order(root):
        if root:
            BiTreeNode.in_order(root.lchild)
            print(root.data, end=",")
            BiTreeNode.in_order(root.rchild)
    #后序遍历
    @staticmethod
    def post_order(root):
        if root:
            BiTreeNode.post_order(root.lchild)
            BiTreeNode.post_order(root.rchild)
            print(root.data, end=",")

    # 层次遍历
    @staticmethod
    def level_order(root):
        queue = deque()#队列
        queue.append(root)
        while len(queue)>0:#只要队不空
            node = queue.popleft()
            print(node.data,end=",")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
    @staticmethod
    def create_tree_test():
        a = BiTreeNode("A")
        b = BiTreeNode("B")
        c = BiTreeNode("C")
        d = BiTreeNode("D")
        e = BiTreeNode("E")
        f = BiTreeNode("F")
        g = BiTreeNode("G")
        e.lchild = a
        e.rchild = g
        a.rchild = c
        c.lchild = b
        c.rchild = d
        g.rchild = f
        root = e
        return root
if __name__ == "__main__":
    #二叉树的遍历方式
    #前序遍历，中序遍历，后序遍历，层次遍历
    root = BiTreeNode.create_tree_test()
    BiTreeNode.pre_order(root)
    print("\n")
    BiTreeNode.in_order(root)
    print("\n")
    BiTreeNode.post_order(root)
    print("\n")
    BiTreeNode.level_order(root)