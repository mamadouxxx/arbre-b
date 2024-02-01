from util import recherche_dichotomique

class Node() :
    
    def __init__(self, keys, childs = [], k = 2) :
        self.keys = keys
        self.childs = childs
        self.k = k
        
    def isLeaf(self):
        """
        >>> Node([12, 42]).isLeaf()
        True
        >>> Node([12, 42], [Node([1]), Node([25]), Node([50])]).isLeaf()
        False
        """
        return (len(self.childs) == 0)
                    
    def getSize(self) :
        return len(Keys)
    
    def search(self, value):
        """
        Exemple(s):
        >>> Node([5,25]).search(5)
        (Node([5, 25]), 0)
        >>> Node([12, 42]).search(12)
        (Node([12, 42]), 0)
        >>> Node([12, 42]).search(1)
        >>> Node([12, 42], [Node([1]), Node([25]), Node([50])]).search(1)
        (Node([1]), 0)
        >>> Node([12, 42], [Node([1]), Node([25]), Node([50])]).search(2)
        """
        (found, index) = recherche_dichotomique(value, self.keys)
        if (found):
            return (self, index)
        elif ( self.isLeaf() ):
            return None
        else :
            return self.childs[index].search(value)
    
    def insert(self, value, k):
        """
        >>> Node([5,15]).insert(12, 3)
        Node([5,12,15])
        >>> Node([5,15]).insert(20, 4)
        Node([5,15,20])
        """
        (node, index) = self.search(value)
        if (node == None) :
            if (self.isLeaf()):
                self.keys.insert(index, value)
            else:
                (fini, milieu, g, d) = self.childs[index].insert(value, k)
                if (not fini) :
                    self.keys.insert(index, milieu)
                    self.childs[index] = g
                    self.childs.insert(index+1, d)
            
                    
            
                    
            
            
#         else :
#             (fini, milieu, g, d) = self.childs[index].insert(value, k)
#             if not fini:
#                 return None
#             #TODO
#         if (len(self.keys) > k) :
#             (m, g, d) = self.splitNode()
#             f = False
#         else:
#             return None
            #TODO
            


#     def splitNode(self) :
#         parent = Node(self.k)
#         m = self.keys[(len(self.node.keys))//2]

    def splitNode(self) :
        """
        >>> Node([10,20,25]).splitNode()
        (20, Node([10]), Node([25]))
        >>> Node([12, 20, 22, 40]).splitNode()
        (22, Node([12, 20]), Node([40]))
        >>> Node([3, 5]).splitNode()
        (5, Node([3]), Node([]))
        """
        milieu = len(self.keys) //2
        parent = self.keys[milieu]
        g = Node(self.keys[:milieu], self.childs[:milieu+1])
        d = Node(self.keys[milieu+1:], self.childs[milieu+1:])
        
        return (parent, g, d)
    
    
    
    def __repr__(self) :
        return f"Node({self.keys})"
            














        
            
            
        
    #def getSizeNode() :
    #def getPos() :
    #def setNewChild() :
    #def removeChild() :    
    
    #def isLeaf() :
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)