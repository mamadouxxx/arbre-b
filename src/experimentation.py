#import unittest
from Node import Node
from util import *
from Visualization import Visualization
from BTree import Btree


class experimentation:
    def __init__(self):
        self.btree = Btree(2, Node([]))
        self.experimentationInsert1()
        
    def experimentationInsert1(self):
        #self.btree.insertion(2)
        #self.isCorrect(Btree(2,Node([2])))
        
        #self.btree.insertion(4)
        #self.isCorrect(Btree(2,Node([2,4])))
        
        for n in [2, 4, 5] + list(range(6, 37, 2)) + [7, 9, 11, 13]:
            self.btree.insertion(n)
            
        #Visualization(self.btree).render()
            
        
        print(self.btree)
        
       
       
       
       
       
       
    def isCorrect(self, BTreeTest):
        if (self.btree.equals(BTreeTest)):
            print("Correct")
        else:
            print("error")












if __name__ == "__main__":
    experiment = experimentation()





# if __name__ == "__main__":
#     import sys
#     sys.path.insert(1, './src')
#     sys.path.insert(2, '../src')
#     from Node import *
# 
#     unittest.main()
#     import doctest
#     doctest.testmod(verbose=False)