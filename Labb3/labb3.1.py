# Laboration 3 - Uppgift 1: For-satser och range

print("C   F") #skriver ut enheterna för tabellen

for c in range(0, 21): #för antal temperaturer i tabellen skriver värden
    f = (c*9+160)/5 #beräknar temp F
    print("{0:<3}".format(c), f) #skriver ut C och sen F
