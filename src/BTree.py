#import Node as Bnode
from node import *


class Btree() :
    
    def __init__(self, k, root=None) :
        self.root = root
        self.k = k
        
    def search(self, value):
        """
        Exemple(s):
        >>> Btree(2, Node([5,25])).search(25)
        (Node([5, 25]), 1)
        >>> Btree(2, Node([12, 42], [Node([1]), Node([25]), Node([50])])).search(1)
        (Node([1]), 0)
        >>> Btree(2, Node([12, 42], [Node([1]), Node([25]), Node([50])])).search(2)
        """
        return self.root.search(value)

    def insertion(self, value):
        """
        Exemple(s):
        >>> Btree(2, Node([12, 42], [Node([2, 3]), Node([25]), Node([50])])).insertion(1)
        True
        >>> Btree(3, Node([12,25,50], [Node([1,11]), Node([20]), Node([100])])).insertion(10)
        True
        >>> Btree(2, Node([4, 10], [Node([1, 3]), Node([25]), Node([50])])).insertion(4)
        True
        """
        fini, milieu, g, d = self.root.insert(value)
        if (not fini):
            new_root = Node([milieu], [g, d])
            self.root = new_root
        return True
        
            
        
        
                
            
    
    #def search() :
    #def insertion():
    #def createNode() :
    #def delete() :
    #def linear() :
    #def createTree() :
    #def height() :
    #def isArbre() :
    #def getNbKeys () :
    #def getSize () :
    #def changeRoot() :
    #def isEqual() :
                
                
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)