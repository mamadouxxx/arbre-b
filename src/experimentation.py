#import unittest
from Node import Node
from util import *
from Visualization import Visualization
from BTree import Btree


class experimentation:
    def __init__(self, exp):
        if exp == "1":
            self.experimentationInsert1()
        elif exp == "2":
            self.experimentationSuppr1()
        elif exp == "3" :
            self.experimentationInsert2()
        
    def experimentationInsert1(self):
        self.btree = Btree(2, Node([]))
        for n in [2, 4, 5] + list(range(6, 37, 2)) + [7, 9, 11, 13]:
            self.btree.insertion(n)
        
            
        Visualization(self.btree).render()
        print("est un arbreB : " + str(self.btree.isBalance()))
        print(self.btree)
    
    def experimentationSuppr1(self):
        self.btree = Btree(2, Node([]))
        #non fonctionnel
        print("Non fonctionnel")
        for n in [2, 4, 5] + list(range(6, 37, 2)) + [7, 9, 11, 13]:
            self.btree.insertion(n)
        

        self.btree.suppr(20,2)
        Visualization(self.btree).render()
        #for n in [14,10,20,18,16,24,6]
        
        
        print(self.btree)
        
    def experimentationInsert2(self):
        self.btree = Btree(10, Node([]))
        for n in list(range(100000)):
            self.btree.insertion(n)
            
        #Visualization(self.btree).render()
        print("est un arbreB : " + str(self.btree.isBalance()))
        print(self.btree)
       
       
if __name__ == "__main__":
    response = input("Quelle expérimentation voulez vous (1: insertion1 / 2: suppression1 / 3: insertion3 )")
    experiment = experimentation(response)