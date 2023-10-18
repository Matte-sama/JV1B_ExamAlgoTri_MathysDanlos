#exercice 3


Myliste = [24,12,36,9]
n = len(Myliste)


for i in range(n):      #permet le parcours du tableau
    for j in range(0, n-i-1):       #retourne au départ tout en enlevant la dernière valeur de la loop qui est également la plus grande
        if Myliste[j] > Myliste[j+1] :      #échange de place si la valeur de devant est plus grande que la suivante
            Myliste[j],Myliste[j+1] = Myliste[j+1],Myliste[j]
print(Myliste)