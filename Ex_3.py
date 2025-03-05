'''
Dans cet exercice, vous allez devoir créer une fonction qui s'appelle recherche prennant comme paramètre un tableau de liste, 
dont un example est donné ci-dessous, et un nombre. Cette fonction doit retourner la position de ce nombre, de la manière marquée ci-dessous. 
Si le nombre n'est pas dans le tableau, la fonction devra retourner None. On assume que les nombres ne se répètent pas.
'''
tableau_de_liste = [[1, 2, 3, 4],
                    [5, 6]]

# la position de 2 est [1,2], et la position de 5 est [2,1]
# écrire votre code ici


assert recherche([[1, 2, 3, 4],[5, 6]], 5) == [2,1]
assert recherche([10, 20, 30, 40, -50], 10) == [1,1]
assert recherche([[1, 2, 3, 4],[5, 6]], 7) == None
assert recherche([]) == None

