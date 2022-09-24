# Laboration 2 - Uppgift 2: If-satser

# scenario:
'''
Scenario:
Hur mycket väger paketet: 9.5 
Det kommer att kosta 237.5 Kr
'''

# lösningen börjar här
vikt = float(input("Hur mycket väger paketet: ")) # sätter vikt till användarens input (float)

if vikt < 2:
    pris = 30                   # om vikt < 2 sätts pris till 30kr/kg
elif vikt < 6:    
    pris = 28                   # om vikt 2 <= vikt < 6 -> 28kr/kg
elif vikt < 12:   
    pris = 25                   # om vikt 6 <= vikt < 12 -> 25kr/kg
else:
    pris = 23                   # annars -> 23kr/kg

paketpris = vikt*pris               # beräknar paketets pris
print("Det kommer att kosta", paketpris, "Kr") # skriver ut priset