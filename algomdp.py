"""
@name algomdp.py
@author Aelion
@version 1.0.0
""" 

"""
Fonction permettant de creer un mdp de maniere aléatoire
"""



import random
import string

theCharacter = [",", ";", "/","(", ")","[", "]", "-","_"]



tailleMdp = random.randint(8, 12)
print(tailleMdp)

theChar = random.choice(theCharacter)
print(theChar)

theDig = random.choice(string.digits)
print(theDig)

theMaj = random.choice(string.ascii_uppercase)
print (theMaj)

firstPassword = [theChar, theDig, theMaj]
 
 #2eme etape: creer boucle tant que j'ai pas rempli les "n" caracteres du mdp



while len(firstPassword) < tailleMdp:
    nouvelBoite = random.randint(0,2)
    if nouvelBoite == 0:
        nouvellePioche = random.choice(theCharacter)
    if nouvelBoite == 1:
        nouvellePioche =random.choice(string.digits)
    if nouvelBoite == 2:
        nouvellePioche =random.choice(string.ascii_uppercase)
    


    firstPassword.append(nouvellePioche)  
print(firstPassword)

random.shuffle(firstPassword)
print(firstPassword)

finalPassword = ""
for indice in range(len(firstPassword)):
    finalPassword = finalPassword +firstPassword[indice]

print("Le mot de passe est", finalPassword)






  
  

























