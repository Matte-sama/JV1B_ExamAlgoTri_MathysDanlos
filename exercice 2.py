#exercice 2

Myliste = [24,12,36,9]
n = len(Myliste)

for i in range(n-1):         
    if Myliste[i] > Myliste[i+1] :    
        Myliste[i],Myliste[i+1] = Myliste[i+1],Myliste[i]
print(Myliste)