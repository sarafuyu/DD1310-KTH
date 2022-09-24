# Laboration 3 - Uppgift 2: Nästlade slingor

rader=int(input("Ange antal rader: "))              #frågar om input för kolumn och rader
kolumner=int(input("Ange antal kolumner: "))

print("    ", end="")   #första space på början av första kolumnen

p=1
i=1
while p<=kolumner:          #skriver ut top raden av multiplikationstabellen
    print("{0:<3d}".format(i*p), end=(" "))
    p=p+1
print()

while i<=rader:
    j=1
    while j<=kolumner:
        if j<2:             #börjar raden med nummer igen
            print("{0:<3d}".format(i), end=" ")
        print("{0:<3d}".format(i*j), end=" ")
        j=j+1
    print()
    i=i+1
    j=1
    
#klarar upp till 31 för det är 3 per rad