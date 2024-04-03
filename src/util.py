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
    """Renvoie l'unique `index` vérifiant :
          * 0 ≤ index ≤ len(liste)
          * ∀j ∈ [0 ; len(liste)[, si j < index alors liste[j] < x
                                   sinon liste[j] ≥ x
    Cet indice `index` indiquera soit la place de l'élément x dans la liste,
    soit la place du fils susceptible de contenir l'élément x recherché
    dans un arbre de recherche.
    
    complexité:
        log(n)

    Précondition : `liste` est triée par ordre croissant
    Exemple(s) :
    >>> recherche_dichotomique(3, [1, 3, 5])
    (True, 1)
    >>> recherche_dichotomique(4, [1, 3, 5])
    (False, 2)
    >>> recherche_dichotomique(0, [1, 3, 5])
    (False, 0)
    >>> recherche_dichotomique(42, [1, 3, 5])
    (False, 3)
    >>> recherche_dichotomique(42, [])
    (False, 0)
    """
    # précondition : liste triée
    assert all(l[k] <= l[k+1] for k in range(len(l) - 1))
    
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
            
    # postcondition
    assert 0 <= index <= len(l)
    assert all(j < index and l[j] < x or l[j] >= x
                   for j in range(len(l)))
    return (False, index)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)