#import unittest
from Node import Node
from util import *
from Visualization import Visualization
from BTree import Btree


class experimentation:
    def __init__(self, exp):
        self.btree = Btree(2, Node([]))
        if exp == "1":
            self.experimentationInsert1()
        elif "2":
            self.experimentationSuppr1()
        else :
            None 
        
    def experimentationInsert1(self):        
        for n in [2, 4, 5] + list(range(6, 37, 2)) + [7, 9, 11, 13]:
            self.btree.insertion(n)
            
        Visualization(self.btree).render()
            
        print(self.btree)
    
    def experimentationSuppr1(self):
        for n in [2, 4, 5] + list(range(6, 37, 2)) + [7, 9, 11, 13]:
            self.btree.insertion(n)
        

        #for n in [14,10,20,18,16,24,6]
        
       
       
       
       
       
# fonction temporaire pour tester la correspondance des arbres de manière automatique et simple visuellement
#     def isCorrect(self, BTreeTest):
#         if (self.btree.equals(BTreeTest)):
#             print("Correct")
#         else:
#             print("error")












if __name__ == "__main__":
    response = input("Quelle expérimentation voulez vous (1 ou 2)")
    experiment = experimentation(response)






# if __name__ == "__main__":
#     import sys
#     sys.path.insert(1, './src')
#     sys.path.insert(2, '../src')
#     from Node import *
# 
#     unittest.main()
#     import doctest
#     doctest.testmod(verbose=False)