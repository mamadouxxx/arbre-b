import doctest

def compare(a, b):
    """
    :param a: (any) un élément
    :param b: (any) un élément
    :return: (bool) * 1 si a est plus grand que b
                    * 0 si a est égal à b
                    * -1 si a est plus petit que b
    :CU: a et b sont comparables
    :Exemples:
    
    >>> compare(1, 2)
    -1
    >>> compare('z', 'a')
    1
    >>> compare(0, 0)
    0
    """
    if a > b:
        res = 1
    elif a < b:
        res = -1
    else:
        res = 0
    return res

def recherche_dichotomique(x, l, cmp = compare):
    """
    :param x: (any) un élément 
    :param l: (list) une liste
    :return: (bool) True si x appartient à l, False sinon
    :CU: x doit être comparable aux éléments de l,
         l est triée
    :Exemples:

    >>> recherche_dichotomique(1, [])
    (False, 0)
    >>> l = list(range(10))
    >>> recherche_dichotomique(5, l)
    (True, 5)
    >>> recherche_dichotomique(5.5, l)
    (False, 6)
    """
    taille = len(l)
    debut, fin = 0, taille
    index = 0
    while debut < fin:
        milieu = (debut + fin)//2
        if cmp(x, l[milieu]) == 0:
            return (True, milieu)
        elif cmp(x, l[milieu]) > 0:
            index = milieu +1
            debut = milieu + 1
        else:
            fin = milieu
            index = milieu
    return (False, index)

## LOIC
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

doctest.testmod()