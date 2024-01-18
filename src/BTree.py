import Node as Bnode


class Btree() :
    
    def __init__(self, k, root=None) :
        self.root = root
        self.k = k
        
    def search(self, value):
        return self.root.search(value)

# incomplet
    def insertion(self, value):
        if (self.root == None):
            self.root = Bnode.Node(self.k)
            self.root.keys[0] = value
        else :
            if ( len(self.root) ==  self.k):
                new_root = Bnode.Node(self.k)
                new_root.childs[0] = self.root
                
                if (self)
            else:
                self.root.insert_not_full(value)
            
        
        
                
            
    
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