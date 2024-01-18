from util import recherche_dichotomique

class Node() :
    
    def __init__(self, k) :
        self.parent =
        self.keys = []
        self.childs = []
        self.k = k
        
    def isLeaf():
        return (len(self.childs) == 0)
                    
    def getSize(self) :
        return len(Keys)
    
    def serach(self, value):
        (found, index) = recherche_dichotomique(value, self.keys)
        if (found):
            return (node, index)
        elif ( node.isLeaf() ):
            return None
        else :
            self.childs[index].search(value)
    
    def insert_not_full(self, value):
        (found, index) = self.search(value)
        if (self.isLeaf()) :
            if (not found):
                self.keys.insert() = value
        else :
            if (len(self.childs[index]) == self.k) :
                self.childs[index].splitNode(index)
                if (value > self.keys[index]) :
                    index += 1
            self.childs[index].insert_not_full(value)

# j'ai pas encore bien compris comment m'y prendre
    def splitNode(self) :
        parent = Node(self.k)
        m = self.keys[(len(self.node.keys))//2]
        
        
            
            
        
    #def getSizeNode() :
    #def getPos() :
    #def setNewChild() :
    #def removeChild() :    
    
    #def isLeaf() :