import Node as Bnode


class Btree() :
    
    def __init__(self, k, root=None) :
        self.root = root
        self.k = k
        
    def search(self, value, node=self.root):
        (found, index) = node.search(value)
        if (found):
            return (node, index)
        elif ( node.isLeaf() ):
            return None
        else :
            self.search(value, node.childs[index])
            
    def insertion(self, value):
        if (self.root == None):
            self.root = Bnode.Node(self.k)
            self.root.keys[0] = value
        else :
            if ( len(self.root) ==  self.k):
                new_root = Bnode.Node(self.k)
                new_root.childs[0] = self.root
            
        
        
                
            
    
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