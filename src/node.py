import util

class node() :
    
    def __init__(self, k, kmin, kmax) :
        self.keys = []
        self.childs = []
        self.kmin = kmin
        self.kmax = kmax
        
    def search(self, Key):
        return util.recherche_dichotomique(key, self.childs)
            
    def getSize(self) :
        return len(Keys)
    
    def addKey(self) :
        
        
    def dicho(self, listKeys,key) :
        t=len(listKeys)-1
        d, f = 0, t        
        while (f>= d) :
            m=(d+f)//2
            
            if (listKeys[m]==key) :
                return m
            if (listKeys[m]>key):
                f=m - 1
                #if ( f< t and listKeys[f] == key) :
                 #   return True,f
            else :
                d=m + 1
                #if (d < t and listKeys[d] == key) :
                 #   return True, d           
            
        return -1
    
        
    #def getSizeNode() :
    #def getPos() :
    #def setNewChild() :
    #def removeChild() :    
    
    #def isLeaf() :