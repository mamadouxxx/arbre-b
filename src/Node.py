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
        return len(self.keys)
    
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
    
    def insert(self, value):
        """
        Exemple(s):
        >>> node = Node([5])
        >>> node.insert(20)
        (True, None, None, None)
        >>> node.search(20)
        (Node([5, 20]), 1)
        >>> Node([5,15]).insert(12)
        (False, 12, Node([5]), Node([15]))
        >>> node.search(12)
        
        >>> node = Node([12, 42], [Node([3]), Node([25]), Node([50])])
        >>> node.insert(52)
        (True, None, None, None)
        >>> node.search(52)
        (Node([50, 52]), 1)
        >>> node = Node([12, 42], [Node([2, 3]), Node([25]), Node([50])])
        >>> node.insert(1)
        (False, 12, Node([2]), Node([42]))
        >>> node.search(1)
        (Node([1]), 0)
        >>> node = Node([12, 42], [Node([2, 4], [Node([0, 1]), Node([3]), Node([7, 8])]), Node([25]), Node([50])])
        >>> node.insert(6)
        (False, 12, Node([4]), Node([42]))
        
        >>> node = Node([12, 42], [Node([2, 3, 4]), Node([25]), Node([50])], 3)
        >>> node.insert(1)
        (True, None, None, None)
        
        """
        (found, index) = recherche_dichotomique(value, self.keys)
        if (not found) :
            if (self.isLeaf()):
                self.keys.insert(index, value)
                if ( len(self.keys) > self.k):
                    milieu, g, d = self.splitNode()
                    return False, milieu, g, d
                return True, None, None, None
            else:
                (fini, milieu, g, d) = self.childs[index].insert(value)
                if (not fini) :
                    self.keys.insert(index, milieu)
                    self.childs[index] = g
                    self.childs.insert(index+1, d)
                    if ( len(self.keys) > self.k) :
                        milieu, g, d = self.splitNode()
                        return False, milieu, g, d
                    else:
                        return True, None, None, None
                else :
                    return True, None, None, None
        else :
            return True, None, None, None
    
    def suppr(self,value) :
        """
        >>> a = Node([12, 42], [Node([3]), Node([25]), Node([50])])
        >>> a.suppr(11)
        False
        """
        found = self.search(value)
        if (found) :
            return None
        else :
            return False
        
        
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
        g = Node(self.keys[:milieu], self.childs[:milieu+1])
        d = Node(self.keys[milieu+1:], self.childs[milieu+1:])
        
        return (self.keys[milieu], g, d)
    
    def linearisation(self):
        """
        Exemple(s):
        >>> Node([12, 42], [Node([2, 3]), Node([13, 15]), Node([45])]).linearisation()
        [2, 3, 12, 13, 15, 42, 45]
        >>> Node([12, 42], [Node([2, 3]), Node([25]), Node([50])]).linearisation()
        [2, 3, 12, 25, 42, 50]
        """
        if (self.isLeaf()):
            res = self.keys
        else:
            res = []
            for i in range(0, len(self.keys)):
                res.extend(self.childs[i].linearisation())
                res.append(self.keys[i])
            res.extend(self.childs[len(self.childs)-1].linearisation())
        return res
        
    
    
    def __repr__(self) :
        return f"Node({self.keys})"
              
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)