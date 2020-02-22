'''
Builds a balanced Binary Search Tree from any list
'''

from enum import Enum

class Traversal(Enum):
    """
    Enumeration for more readable code.

    Represent the four possible Binary Tree Traversals.
    """
    IN = 1
    PRE = 2
    POST = 3
    LEVEL = 4
    
class TreeNode:
    """
    Reference based Binary Tree Node.
    """
    def __init__(self, key, data, leftPtr = None, rightPtr = None):
        """
        [key] and [data] are expected.
        """
        self.key = key
        self.data = data
        self.leftT = leftPtr
        self.rightT = rightPtr
    
    def toString(self):
        return "[K:%d|D%s | left at %d |right at %d]"%(self.key, self.data, self.leftT, self.rightT)

class BSTMod:
    """
    Simplified BST ADT implemented with reference
    """
    def __init__(self):
        """
        Returns an empty BST
        """
        self._root = None
        self._size = 0  
        
    def size(self):
        """
        Return size of the BST, i.e. number of datas in BST.
        """
        return len(self._size)

    def _insert(self, T, key, data ):
        """
        Internal recursive method that carries out the insertion algorithm.
        """
        if T == None:
            return TreeNode( key, data )
        
        if T.key == key:
            raise KeyError("Duplicate Key [%s]!"%(key))
        elif T.key < key:
            T.rightT = self._insert( T.rightT, key, data )
        else:
            T.leftT  = self._insert( T.leftT, key, data )
        
        return T

    def insert(self, key, data):
        """
        Insert (key, data) into BST.

        [key] is used to determine the location of the insertion.
        """
        self._root = self._insert(self._root, key, data)
        self._size += 1

    #Note deletion is not supported in this simplified implementation
    
    def _preorder(self, T):
        """
        Internal recursive method to perform Pre-Order Traversal.
        """
        if T == None:
            return []
        return [T.key] + self._preorder(T.leftT) + self._preorder(T.rightT)

    def _inorder(self, T):
        """
        Internal recursive method to perform In-Order Traversal.
        """
        if T == None:
            return []
        return  self._inorder(T.leftT) + [T.key] + self._inorder(T.rightT)

    def _postorder(self, T):
        """
        Internal recursive method to perform Post-Order Traversal.
        """
        if T == None:
            return []
        return  self._postorder(T.leftT) + self._postorder(T.rightT) + [T.key]

    def traversal(self, which):
        """
        Return specified traversal of the BST as a list.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        if which == Traversal.PRE:
            return self._preorder(self._root) 
        elif which == Traversal.IN:
            return self._inorder(self._root)
        elif which == Traversal.POST:
            return self._postorder(self._root)

    def _findRightRoot(self, lst):
        root = lst[0]
        i = 1
        while i < len(lst):
            if lst[i] >= root:
                break
            i += 1
##            print('i is:', i, 'and lst[i] is', lst[i])
        return i
    
    def _buildBSTfromPreorder(self, L ):
        """ 
        [L] is a list of number organized as a pre-order traversal of a BST. 
        
        Rebuild and return the BST from [L]. 
        """
        if L == []:
            return None
        root = TreeNode(L[0], L[0])
        rightRootIdx = self._findRightRoot(L)
        root.leftT = self._buildBSTfromPreorder(L[1: rightRootIdx])

        return root

    
    def buildBSTfromPreorder(self, L ):
        """ 
        Just a wrapper to call the actual recursive implementation. 
        
        Note: Calling this method destroy current content of BST.
        """
        self._root = self._buildBSTfromPreorder(L)
        self._size = len(L)

        
    def _buildBSTfromSortedList(self, L):
        """
        Internal helper method to build a BST from sorted list
        """
        if L == []:
            return None
        rootIdx = len(L)//2
        root = TreeNode(L[rootIdx], str(L[rootIdx]))
        root.leftT = self._buildBSTfromSortedList(L[: rootIdx])

        root.rightT = self._buildBSTfromSortedList(L[rootIdx+1: ])
        self._root = root
        
        return self._root   #modify accordingly

    def buildBalancedBST( self,  L ):
        """ 
        [L] is a list of numbers in random order. 
        
        Build and return a balanced BST from [L]. 
        """
        if L == []:
            return None  
        for i in range (len(L)):  #insert items into BST
            self.insert(L[i], str(L[i]))
        sortedList = self.traversal(Traversal.IN) #created sorted list
        newRoot = (self._buildBSTfromSortedList(sortedList))
        
        return newRoot
        

def main():

    bt = BSTMod()

    # Part A test below
   bt.buildBSTfromPreorder([5, 3, 1, 2, 4, 8, 6, 7, 9])

    bt.buildBalancedBST([2, 4, 7, 8, 1, 5, 6, 3, 9])

    print(bt.traversal(Traversal.PRE))

if __name__ == "__main__":
    main()
