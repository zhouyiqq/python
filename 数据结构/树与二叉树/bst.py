# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/11 22:44
import random

class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None#左孩子
        self.rchild = None#右孩子
class BST:#二叉搜索树
    def __init__(self,li = None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
    def insert(self,node,val):#递归
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild,val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild,val)
            node.rchild.parent = node
        else:
            pass
        return node
    def insert_no_rec(self,val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)#空树
            return 0
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return 0
            elif val>p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return  0
            else:
                return 0
    def query(self,node,val):
        if not node:
            return None
        elif node.data<val:
            return self.query(node.rchild,val)
        elif node.data>val:
            return self.query(node.lchild,val)
        else:
            return node
    def query_no_rec(self,val):
        p = self.root
        while p:
            if p.data<val:
                p = p.rchild
            elif p.data>val:
                p = p.lchild
            else:
                return p
        else:
            return None

    # 前序遍历，先自己，递归左子树，再递归右子树
    def pre_order(self,root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
    # 中序遍历，递归左子树，自己，再递归右子树
    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")
if __name__ =="__main__":
    # tree = BST([4,6,7,9,2,1,3,5,8])
    # tree.pre_order(tree.root)
    # print("\n")
    # tree.in_order(tree.root)#中序序列有序
    # print("\n")
    # tree.post_order(tree.root)
    li = list(range(0,500,2))
    random.shuffle(li)
    tree = BST(li)
    # print(tree.query(tree.root,5).data)
    print(tree.query_no_rec(4))
