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
    (False, -1)
    >>> l = list(range(10))
    >>> recherche_dichotomique(5, l)
    (True, 5)
    >>> recherche_dichotomique(5.5, l)
    (False, -1)
    """
    n = len(l)
    debut, fin = 0, n
    index = 0
    while debut < fin:
        m = (debut + fin)//2
        if cmp(x, l[m]) == 0:
            return (True, m)
        elif cmp(x, l[m]) > 0:
            index += m
            debut = m + 1
        else:
            fin = m
            index = 0
    return (False, -1)

doctest.testmod()