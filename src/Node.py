from util import recherche_dichotomique

class Node() :
    
    def __init__(self, keys, childs = []) :
        self.keys = keys
        self.childs = childs
        
    def isLeaf(self):
        """
        verifie si un noeud est une feuille
        
        Return :
            bool : (true) si feuille, false sinon
        Exemple(s):
        >>> Node([12, 42]).isLeaf()
        True
        >>> Node([12, 42], [Node([1]), Node([25]), Node([50])]).isLeaf()
        False
        """
        return (len(self.childs) == 0)
                    
    
    def search(self, value):
        """
        Rechercher une valeur dans un noeud
        
        Params :
            value : (int), valeur à rechercher
            
        Return :
            (Node, index) : renvoie le noeud qui contient la valeur recherchée et son indice
                            dans ce noeud.
                            ne renvoie rien si valeur inéxistante
                            
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
        
        
    def is_ArbreB(self, k, is_root = False):
        """
        Verification de l'équilibrage d'un noeud
        • Toutes les feuilles ont la même profondeur, à savoir la hauteur h de l’arbre.
        • k/2 ≤ n ≤ k. Taux de remplissage min = 50%, et moyen 75%.
          n = nombre de clés contenus dans le nœud x
        • Si x n’est pas une feuille :
            • pour 2<=i<=n, pour toute clef x du fils i : cles[i] <= [x] <=cles[i+1]
            • Pour toute clef x du fils1 : x <= cles1
        • Si x n’est pas la racine, n est compris entre k/2 et k.
        • chaque noeud a exactement 0 ou k + 1 fils.
        
        Params :
            k => number of keys in node
        Return :
            (ok, height, mini, maxi)
        
        Exemple(s) :
        >>> Node([5]).is_ArbreB(2)
        (True, 0, 5, 5)
        >>> Node([5,25]).is_ArbreB(2)
        (True, 0, 5, 25)
        >>> node = Node([12, 42], [Node([2, 4], [Node([0, 1]), Node([3]), Node([7, 8])]), Node([25]), Node([50])])
        >>> node.is_ArbreB(2)
        (False, 2, 0, 50)
        >>> Node([5,25,3]).is_ArbreB(2)
        (False, 0, 5, 3)
        >>> Node([5, 25], [Node([0, 1, 2]), Node([3, 2, 5])]).is_ArbreB(2)
        (False, 1, 0, 5)
        >>> Node([5], [Node([0]), Node([7], [Node([6]), Node([8])])]).is_ArbreB(2)
        (False, 2, 0, 8)
        >>> Node([12,25,50], [Node([1,11]), Node([20]), Node([30]), Node([100])]).is_ArbreB(3)
        (True, 1, 1, 100)
        >>> Node([12,42], [Node([2,4]), Node([13])]).is_ArbreB(2)
        (False, 1, 2, 13)
        """
        ok = (is_root or (k//2) <= len(self.keys)) and len(self.keys) <= k
        ok = ok and all(self.keys[i] < self.keys[i+1] for i in range(len(self.keys) - 1))
        if(len(self.childs) !=0) : ok = ok and (len(self.childs) == len(self.keys) + 1)
        if (self.isLeaf()):
            height = 0
            mini, maxi = self.keys[0], self.keys[-1]
        else:
            results = [child.is_ArbreB( k, False ) for child in self.childs]
            mins = [mini for (_, _, mini, _) in results]
            maxs = [maxi for (_, _, _, maxi) in results]
            ok = ok and all(self.keys[i] > maxs[i] and self.keys[i] < mins[i+1] for i in range(len(self.keys) - 1))
            heights = [h for (_, h, _, _) in results]
            ok = ok and all(heights[i] == heights[i+1] for i in range(len(heights)-1))
            height = 1 + max(heights)
            mini = min(mins)
            maxi = max(maxs)
        return (ok, height, mini, maxi)
        
    
    def insert(self, value, k):
        """
        insérer une valeur dans un noeud
        
        Params :
            value : (int), valeur à insérer
            
        Return : (True, _,_,_) si insertion réussi où (true) si valeur déjà présente
                 (False, _,_,_) si l'insertion a été faite mais que l'arbre n'est pas équilibré,
                                 dans ce cas on délègue le travail restant au père.
        
        Exemple(s):
        >>> node = Node([])
        >>> node.insert(5,1)
        (True, None, None, None)
        >>> node.insert(20, 2)
        (True, None, None, None)
        >>> node.search(20)
        (Node([5, 20]), 1)
        >>> Node([5,15]).insert(12, 2)
        (False, 12, Node([5]), Node([15]))
        >>> node.search(12)
        
        >>> node = Node([12, 42], [Node([3]), Node([25]), Node([50])])
        >>> node.insert(52, 2)
        (True, None, None, None)
        >>> node.search(52)
        (Node([50, 52]), 1)
        >>> node = Node([12, 42], [Node([2, 3]), Node([25]), Node([50])])
        >>> node.insert(1, 2)
        (False, 12, Node([2], [Node([1]), Node([3])]), Node([42], [Node([25]), Node([50])]))
        >>> node.search(1)
        (Node([1]), 0)
        >>> node = Node([12, 42], [Node([2, 4], [Node([0, 1]), Node([3]), Node([7, 8])]), Node([25]), Node([50])])
        >>> node.insert(6, 2)
        (False, 12, Node([4], [Node([2], [Node([0, 1]), Node([3])]), Node([7], [Node([6]), Node([8])])]), Node([42], [Node([25]), Node([50])]))
        
        >>> node = Node([12, 42], [Node([2, 3, 4]), Node([25]), Node([50])])
        >>> node.insert(1, 3)
        (True, None, None, None)
        """
        (found, index) = recherche_dichotomique(value, self.keys)
        if (not found) :
            if (self.isLeaf()):
                self.keys.insert(index, value)
                if ( len(self.keys) > k):
                    milieu, g, d = self.splitNode()
                    return False, milieu, g, d
                return True, None, None, None
            else:
                (fini, milieu, g, d) = self.childs[index].insert(value, k)
                if (not fini) :
                    self.keys.insert(index, milieu)
                    self.childs[index] = g
                    self.childs.insert(index+1, d)
                    if ( len(self.keys) > k) :
                        milieu, g, d = self.splitNode()
                        return False, milieu, g, d
                    else:
                        return True, None, None, None
                else :
                    return True, None, None, None
        else :
            return True, None, None, None
        
    def suppression(self, value, k, is_root=False) :
        """
        supprime une valeur dans un noeud (cas d'un noeud feuille)
        
        :Params :
            value : (int) valeur à supprimer
            k : nombre de clés dans un noeud
            is_root : pour spécifier si le noeur est le root.
            
        :Return
            bool : (true) si la suppression fonctionne, false sinon
        Exemple(s):
        >>> node = Node([12, 42], [Node([3, 4]), Node([25, 26]), Node([50, 58])])
        >>> node.suppression(50, 2)
        True
        >>> node.search(50)
        >>> node = Node([12, 42], [Node([3, 4]), Node([25, 26]), Node([58])])
        >>> node.suppression(58, 2)
        True
        >>> node
        Node([12, 26], [Node([3, 4]), Node([25]), Node([42])])
        >>> node = Node([12, 42], [Node([3]), Node([25, 26]), Node([58])])
        >>> node.suppression(3, 2)
        True
        >>> node
        Node([12, 26], [Node([42]), Node([25]), Node([58])])
        >>> node = Node([14], [Node([6, 10], [Node([4], [Node([2]), Node([5])]), Node([8], [Node([7]), Node([9])]), Node([12], [Node([11]), Node([13])])]), Node([22, 30], [Node([18], [Node([16]), Node([20])]), Node([26], [Node([24]), Node([28])]), Node([34], [Node([32]), Node([36])])])])
        >>> node.suppression(20, 2)
        True
        >>> node
        Node([14], [Node([6, 10], [Node([4], [Node([2]), Node([5])]), Node([8], [Node([7]), Node([9])]), Node([12], [Node([11]), Node([13])])]), Node([22, 30], [Node([], [Node([16, 18])]), Node([26], [Node([24]), Node([28])]), Node([34], [Node([32]), Node([36])])])])
        """
        (found, index) = recherche_dichotomique(value, self.keys)
        if (self.isLeaf()) :
            removed = self.keys.pop(index)
            ok = is_root or k//2 <= len(self.keys)
        else:
            (ok) = self.childs[index].suppression(value, k, False)
            if (not ok):
                # left sibling lookup
                if(index - 1 >= 0 and (len(self.childs[index-1].keys) - 1 >= k//2)):
                    borrowed = self.childs[index-1].keys.pop()
                    replaced = self.keys.pop(index-1)
                    self.keys.insert(index-1, borrowed)
                    self.childs[index].keys.insert(index-1, replaced) #
                # right sibling lookup
                elif(index + 1 < len(self.childs) and (len(self.childs[index+1].keys) - 1 >= k//2)):
                    borrowed = self.childs[index+1].keys.pop(index-1)
                    replaced = self.keys.pop()
                    self.keys.insert(len(self.keys), borrowed)
                    self.childs[index].keys.insert(len(self.childs[index].keys), replaced) # len(self.childs)
                # when deletion of the key violates the property of the minimum number of keys
                # merge
                else:
                    # left sibling lookup
                    if(index-1 >= 0):
                        replaced = self.keys.pop(index-1)
                        borrowed = self.childs[index-1].keys.pop()
                        self.childs[index].keys.insert(len(self.childs[index].keys), replaced)
                        self.childs[index].keys.insert(index-1, borrowed)
                        del self.childs[index-1]
                    # rigth sibling lookup
                    elif(index + 1 < len(self.childs)):
                        replaced = self.keys.pop(index)
                        borrowed = self.childs[index+1].keys.pop()
                        self.childs[index].keys.insert(index, replaced)
                        self.childs[index].keys.insert(len(self.childs[index].keys), borrowed)
                        del self.childs[index+1]
                ok = not ok
        return ok        
        
    def splitNode(self) :
        """
        Divise un noeud
        
        Return :
            (milieu, gauche, droite) : la valuer du milieu, de gauche et de droite.
        
        Exemple(s):
        >>> Node([10,20,25]).splitNode()
        (20, Node([10]), Node([25]))
        >>> Node([12, 20, 22, 40]).splitNode()
        (22, Node([12, 20]), Node([40]))
        >>> Node([3, 5]).splitNode()
        (5, Node([3]), Node([]))
        >>> Node([3, 5], [Node([2]), Node([4]), Node([8])]).splitNode()
        (5, Node([3], [Node([2]), Node([4])]), Node([], [Node([8])]))
        >>> Node([3, 5, 7], [Node([1, 2]), Node([4]), Node([6]), Node([8, 9])]).splitNode()
        (5, Node([3], [Node([1, 2]), Node([4])]), Node([7], [Node([6]), Node([8, 9])]))
        """
        milieu = len(self.keys) //2
        g = Node(self.keys[:milieu], self.childs[:milieu+1])
        d = Node(self.keys[milieu+1:], self.childs[milieu+1:])
        
        return (self.keys[milieu], g, d)
    
    def linearisation(self):
        """
        linéarise un noeud en une liste triée dans l'order croissant
        
        Return :
            list : int

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
        """
        répresentation d'un noeud et de ces fils.
        """
        return (f"Node({self.keys}"
                + (f", {self.childs})" if len(self.childs) > 0 else ")"))

              
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)