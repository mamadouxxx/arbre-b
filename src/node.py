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
        if (listKeys[f] == key) :
            return (True,f)
        elif (d < t and listKeys[d] == key) :
            return (True, d)
        
        while (f-d > 1) :
            m=(d+f)//2

            if (listKeys[m]>=key):
                f=m
                if ( f< t and listKeys[f] == key) :
                    return (True,f)
            else :
                d=m
                if (d < t and listKeys[d] == key) :
                    return (True, d)            
            
        return (False,0)
    
        
    #def getSizeNode() :
    #def getPos() :
    #def setNewChild() :
    #def removeChild() :
        
    def getSize(listKey) :
        return len(listKey)
    
    
    #def isLeaf() :