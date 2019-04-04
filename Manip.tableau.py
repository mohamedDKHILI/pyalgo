""" 
@name manip_tableau.py
@author Aelion
@version 1.0.0
  Algorithmique spécifique sur les collections
""" 

# Déclaration du tableau de demonstration

monTablo= [15, 3, 25, 12, 7, -15]

"""
fonction de la plus petite appelé getLowerOf
cela permet de donner la plus petite valeur entre deux parametres"

"""

def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal

"""
fonction de la plus grande valeur appelé getGreaderOf
"""

def getGreaterOf(firstVal, secondVal):
    if firstVal < secondVal:
        return secondVal
    else:
        return firstVal

""" 
Compare fuction
@param firstVal First Value to compare
@param secondVal Second Value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of two depends on howTo params
"""

def compare(firstVal, SecondVal, desc=True):
    if (desc):
        return getLowerOf(firstVal, SecondVal)
    return getGreaterOf (firstVal, SecondVal)

"""
min function
@param anArray The array from which i want to get the min value
@return the min value of anArray
"""

def min(anArray):
    theMin = anArray [0]
    for value in anArray [1:]:
        theMin = compare (theMin, value, True)
    return theMin

"""
max function
@param anArray The array from which i want to get the max value
@return the min value of anArray
"""

def max(anArray):
    theMax = anArray [0]
    for value in anArray [1:]:
        theMax = compare (theMax, value, False)
    return theMax

print("La + petite est:", min(monTablo))
print ("La + grande est:", max(monTablo))

"""
fonction moyenne
@param anArray the array from wich evaluate the average value
@return average of anArray
"""
def avg(anArray):
    total = 0
    for indice in range(len(monTablo)):
        total = total + monTablo[indice]
    avg = total / len(monTablo)
    return avg

print("moyenne:",avg(monTablo))

"""
Fonction factorielle
@param anArray  the array 
"""

def facto(anArray):
    facto=1
    for indice in range (len(monTablo)):
        facto= facto * monTablo[indice]
    return facto

print("factorielle:",facto(monTablo))









#simple poor loop


for indice, val in enumerate(monTablo):
    print(monTablo[indice] * 2)

# More complex loop with condition

for indice, val in enumerate (monTablo):
    if indice % 2 == 0:
        print(monTablo[indice] * 2)
#autre exemple de cette boucle 

indice=0
for val in monTablo:
    if indice % 2 == 0:
        print(monTablo[indice] * 2)
indice = indice +1

# Plus petite valeur du tableau

prRefmin = monTablo[0] #cela permet d'initialiser la valeur de départ
for val in monTablo[1:]: # cela créer la boucle à partir du second élement
    if val < prRefmin: #condition: si la valeur est plus petite 
        prRefmin = getLowerOf(prRefmin, val) #on prend comme valeur de ref la ou l'indice est petit
print("La valeur la plus petite est: ", prRefmin)


#Plus grande valeur du tableau

prRefmax = monTablo[0] #cela permet d'initialiser la valeur de départ
for val in monTablo[1:]: # cela créer la boucle à partir du second élement
    if val > prRefmax: #condition: si la valeur est plus grande 
        prRefmax = getGreaterOf(prRefmax, val) #on prend comme valeur de ref la ou l'indice est grand
print("La valeur la plus grande est: ", prRefmax)










