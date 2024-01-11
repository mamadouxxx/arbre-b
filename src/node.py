class node() :
    
    def __init__(self,keys,child,kmin,kmax) :
        self.keys=keys
        self.child=child
        self.kmin=kmin
        self.kmax=kmax
    
    #def search(key) :
        
        
        
    def dicho(listKeys,key) :
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
        
    def getSize(listKey) :
        return len(listKey)
    
    
    #def isLeaf() :