import random
import numpy


class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):

        self.root = None


    # BST insert
    def insert(self, data):
        if not self.root:
            self.root = Node(data)

        else:
            self.insertNode(data, self.root)


    def insertNode(self, data,node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data)


        # BST find
    def find(self, data):
        if not self.root:
            return False
        else:
            return self.findNode(data, self.root)


    def findNode(self, data, node):
        if not node:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self.findNode(data, node.left)
        if data > node.data:
            return self.findNode(data, node.right)
        # BST traverse

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)


    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        print(node.data)

        if node.right:
            self.traverseInOrder(node.right)


        # BST remove
    def remove(self, data):
        if self.root:
            self.removeNode(data, self.root)


    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)

        else:
        # check no children case
            if not node.left and not node.right:
                print("removing a leaf node ...")
                del node
                return None
            # remove node with single child
            if not node.left:  # remove node with single right child
                print("removing a node with a single right child ...")
                tempnode = node.right
                del node
                return tempnode

            elif not node.right:  # remove node with single ledt child
                print("removing a node with a single left child ...")
                tempnode = node.left
                del node
                return tempnode
            # remove node with two children
        print("removing a node with two children...")
        tempnode = self.getPredecessor(node.left)
        node.data = tempnode.data
        node.left = self.removeNode(tempnode.data, node.left)
        return node


    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node
        # BST get min val

    def getMinVal(self):
        if self.root:
            return self.getMin(self.root)


    def getMin(self, node):
        if node.left:
            return self.getMin(node.left)
        return node.data

    def getMaxVal(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.right:
            return self.getMax(node.right)
        return node.data

def main():

    #Instantiating and inserting 14 values in binary tree and traversing.
    BST=BSTree()
    BST.insert(7)
    BST.insert(14)
    BST.insert(2)
    BST.insert(4)
    BST.insert(20)
    BST.insert(3)
    BST.insert(8)
    BST.insert(25)
    BST.insert(19)
    BST.insert(12)
    BST.insert(10)
    BST.insert(18)
    BST.insert(17)
    BST.insert(5)

    BST.traverse()

    print('Maximum value of Binary Tree : ')
    print(BST.getMaxVal())

    print('Second BST Tree')

    #second instantiation and insertion with traversing
    BST1=BSTree()
    BST1.insert(20)
    BST1.insert(18)
    BST1.insert(17)
    BST1.insert(14)
    BST1.insert(12)
    BST1.insert(10)
    BST1.insert(9)
    BST1.insert(8)
    BST1.insert(7)
    BST1.insert(6)
    BST1.insert(5)
    BST1.insert(4)
    BST1.insert(3)
    BST1.insert(2)

    BST1.traverse()

    print('Maximum value of Binary Tree : ')
    print(BST1.getMaxVal())


main()