# Laboration 2 - Uppgift 3: Slingor

# scerario: 
'''
Hur många paket vill du skicka? 6
Ange vikt för paket 1: 3
Ange vikt för paket 2: 1 
Ange vikt för paket 3: 7 
Ange vikt för paket 4: 9 
Ange vikt för paket 5: 10
Ange vikt för paket 6: 15 

Det kommer att kosta 1109 kr.
'''

# lösningen börjar här
i = 1 # räknaren för antal paket
summa = 0 # summan av priserna
antal = int(input("Hur många paket vill du skicka? ")) # sätter antal till användarens input (int)

while i <= antal:
    vikt = 0                        # sätter vikten till 0
    print("Ange vikt för paketet", i, ":")
    vikt = float(input())           # sätter vikt till användarens input (float)
    if vikt < 2:
        pris = 30                   # om vikt < 2 sätts pris till 30kr/kg
    elif vikt < 6:    
        pris = 28                   # om vikt 2 <= vikt < 6 -> 28kr/kg
    elif vikt < 12:   
        pris = 25                   # om vikt 6 <= vikt < 12 -> 25kr/kg
    else:
        pris = 23                   # annars -> 23kr/kg
    paketpris = vikt*pris           # beräknar paketets pris
    summa += paketpris              # lägger till priset till summan
    i += 1                          # ökar räknaren med 1
print("Det kommer att kosta", summa, "kr") # skriver ut summan