#import Node as Bnode
from node import *


class Btree() :
    
    def __init__(self, k, root=None) :
        self.root = root
        self.k = k
        
    def search(self, value):
        return self.root.search(value)

# incomplet
#     def insertion(self, value):
#         
#         if (self.root == None):
#             self.root = Bnode.Node(self.k)
#             self.root.keys[0] = value
#         else :
#             if ( len(self.root) ==  self.k):
#                 new_root = Bnode.Node(self.k)
#                 new_root.childs[0] = self.root
#                 
#                 if (self) :
#                     ##TODO
#                     return None
#             else:
#                 self.root.insert_not_full(value)
#

    def insertion(self,value):
        """
        >>> Node([5,25]).insertion(10)
        Node([5,10,25])
        >>> Node([]).insertion(1)
        Node([1])
        >>> Node([5,25]).insertion(50)
        Node([5,25,50])
        """
        
        
        
            
        
        
                
            
    
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
    doctest.testmod(verbose=True)