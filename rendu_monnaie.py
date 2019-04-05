"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest in division
Use input () function to a user entry
"""
#definition des variables

nbBillet100 = 0
nbBillet50 = 0
nbBillet10 = 0
nbPiece = 0



entreeSomme = 470 
somme = int(entreeSomme)


# got 100
nbBillet100 = somme // 100 
reste100 = somme % 100
if reste100 > 0:
    # got 50
    nbBillet50 = reste100 // 50
    reste50 = somme % 50


    if  reste50 > 0:
        # got 10
        nbBillet10 = reste50 // 10
        reste10 = somme % 10

        if reste10 > 0:
            nbPiece = reste10 // 2
            nbPiece = reste10 % 2

print("la machine vous rend: ", nbBillet100, "billets de 100e", nbBillet50, "billets de 50e", nbBillet10, "Billets de 10e") 