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
nbbillet10 = 0
nbPiece = 0


entreeSomme = input("Inserez votre billet : ")
somme = int(entreeSomme)

# got 100
nbBillet100 = somme // 100 
reste100 = somme % 100
if reste100 > 0:
    # got 50
    NbBillet50 = reste100 // 50
    reste50 = reste100 % 50

    if reste50 > 0:
        # got 10
        NbBillet10 = reste50 // 10
        reste10 = reste50 % 10

        if reste10 > 0:
            nbPiece = reste10 // 2
            nbPiece = reste10 % 2

print("la machine vous rend: ", nbBillet100)




