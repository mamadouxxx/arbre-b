#import Node as Bnode
from Node import Node
#from Visualization import Visualization


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
#         >>> a =Btree(2, Node([12, 42], [Node([2, 3]), Node([25]), Node([50])]))
#         >>> a.insertion(1)
#         True
#         >>> a.search(1)
#         (Node([1]), 0)
#         >>> b= Btree(3, Node([12,25,50], [Node([1,11]), Node([20]), Node([100])]))
#         >>> b.insertion(10)
#         True
#         >>> b.search(10)
#         (Node([1, 10, 11]), 1)
#         >>> Btree(2, Node([4, 10], [Node([1, 3]), Node([25]), Node([50])])).insertion(4)
#         True
        >>> c = Btree(2,Node([1, 10]))
        >>> print(c.insertion(15))

        """
        print(self.root)
        fini, milieu, g, d = self.root.insert(value, self.k)
        if (not fini):
            new_root = Node([milieu], [g, d])
            self.root = new_root
        print(self.root)
        return True
    
    
    def linearisation(self):
        """
        Exemple(s):
        >>> a =Btree(2, Node([12, 42], [Node([2, 3]), Node([25]), Node([50])]))
        >>> a.linearisation()
        [2, 3, 12, 25, 42, 50]
        """
        return self.root.linearisation()
            
    def isBalance(self):
        """
        Exemple(s) :
        >>> b= Btree(3, Node([12,25,50], [Node([1,11]), Node([20]), Node([30]), Node([100])]))
        >>> b.isBalance()
        True
        """
        (ok, _, _, _) = self.root.is_ArbreB(self.k, True)
        return ok
    
    def equals(self, otherObject):
        if not isinstance(otherObject, Btree):     
            return False
        return (self.root.keys == otherObject.root.keys and self.k == otherObject.k)
            
    def __repr__(self) :
        return f"Btree({self.root})"
                
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)