from Node import Node


class Btree() :
    
    def __init__(self, k, root=None) :
        self.root = root
        self.k = k
        
    def search(self, value):
        """
        Rechercher une valeur dans l'arbre
        Params :
            value : (int), valeur à rechercher
            
        Return :
            (Node, index) : renvoie le noeud qui contient la valeur recherchée et son indice
                            dans ce noeud.
                            ne renvoie rien si valeur inéxistante
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
        insérer une valeur dans l'arbre
        
        Params :
            value : (int), valeur à insérer
        
        Return :
            bool : (true) si insertion réussi, false sinon.
            
        Exemple(s):
        >>> a =Btree(2, Node([12, 42], [Node([2, 3]), Node([25]), Node([50])]))
        >>> a.insertion(1)
        True
        >>> a.search(1)
        (Node([1]), 0)
        >>> b= Btree(3, Node([12,25,50], [Node([1,11]), Node([20]), Node([100])]))
        >>> b.insertion(10)
        True
        >>> b.search(10)
        (Node([1, 10, 11]), 1)
        >>> Btree(2, Node([4, 10], [Node([1, 3]), Node([25]), Node([50])])).insertion(4)
        True
        >>> c = Btree(2,Node([1, 10]))
        >>> c.insertion(15)
        True
        """
        fini, milieu, g, d = self.root.insert(value, self.k)
        if (not fini):
            new_root = Node([milieu], [g, d])
            self.root = new_root
        return True
    
    
    def linearisation(self):
        """
        linéarise l'arbre en une liste triée dans l'order croissant
        
        Return :
            list : int
            
        Exemple(s):
        >>> a =Btree(2, Node([12, 42], [Node([2, 3]), Node([25]), Node([50])]))
        >>> a.linearisation()
        [2, 3, 12, 25, 42, 50]
        """
        return self.root.linearisation()
            
    def isBalance(self):
        """
        Verification de l'équilibrage de l'arbre
        • Toutes les feuilles ont la même profondeur, à savoir la hauteur h de l’arbre.
        • k/2 ≤ n ≤ k. Taux de remplissage min = 50%, et moyen 75%.
          n = nombre de clés contenus dans le nœud x
        • Si x n’est pas une feuille :
            • pour 2<=i<=n, pour toute clef x du filsi : clesi <= x <=clesi+1
            • Pour toute clef x du fils1 : x <= cles1
        • Si x n’est pas la racine, n est compris entre k/2 et k.
        
        Return :
            bool : true si l'arbre est bien équilibré et false sinon.
        
        Exemple(s) :
        >>> b = Btree(3, Node([12,25,50], [Node([1,11]), Node([20]), Node([30]), Node([100])]))
        >>> b.isBalance()
        True
        >>> Btree(3, Node([12,25,50,62], [Node([1,11]), Node([20]), Node([30]), Node([100])])).isBalance()
        False
        >>> Btree(3, Node([12,25,50], [Node([15]), Node([30]), Node([100])])).isBalance()
        False
        >>> Btree(3, Node([12,25,50])).isBalance()
        True
        """
        (ok, _, _, _) = self.root.is_ArbreB(self.k, True)
        return ok
    
    def suppr(self, value, k):
        """
        Supprimer une valeur dans l'arbre
        Params :
            value : (int), valeur à supprimer
            k : (int), nombre de clés
            
        Return :
            #TODO
        Exemple(s):
        >>> arbreB = Btree(2, Node([5,25]))
        >>> arbreB.suppr(25,2)
        True
        >>> arbreB
        Btree(Node([5]))

        """
        return self.root.suppression(value, k, True)
                
    def __repr__(self) :
        """
        representataion d'un btree
        """
        return f"Btree({self.root})"
                
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)