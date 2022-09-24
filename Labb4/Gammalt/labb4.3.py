# Laboration 4 del 1

# användarens valda parametrar
antal_rader = int(input("Hur många rader ska chokladbaren bestå av: "))
antal_kolumner = int(input("Hur många kolumner ska chokladbaren bestå av: "))

#skapar en matris baserat på användarens input
def create_chocolate_bar(antal_rader, antal_kolumner):
    if antal_rader and antal_kolumner >=0: 
        global chocolate_bar_matris 
        chocolate_bar_matris = [] 
        for r in range(1,antal_rader+1):
            kolumn = []
            for k in range(1,antal_kolumner+1):
                kolumn.append(str(r)+str(k))
            chocolate_bar_matris.append(kolumn)
        return chocolate_bar_matris
    else:
        return None

#skriver ut matrisen i rätt format på separata rader för de inre listorna
def print_chocolate_bar(chocolate_bar_matris):
    for i in range(len(chocolate_bar_matris)):
        for x in range(len(chocolate_bar_matris[i])):
            print(chocolate_bar_matris[i][x], end=" ")
        print()

# användarens valda parametrar
rader = int(input("vilken rad ska vi käka?: ")) - 1
kolumner = int(input("vilken kolumn ska vi käka?: ")) - 1

#klipper ut delar av matrisen
def chomp(chocolate_bar_matris, rader, kolumner):
    
    for r in reversed(range(len(chocolate_bar_matris))):
        if r >= rader :
            for k in reversed(range(len(chocolate_bar_matris[r]))):
                if k >= kolumner:
                    del chocolate_bar_matris[r][k]

chomp(chocolate_bar_matris, rader, kolumner)
print_chocolate_bar(chocolate_bar_matris)

create_chocolate_bar(antal_rader, antal_kolumner)
print_chocolate_bar(chocolate_bar_matris)

# tester som står i uppgiftsinstruktionen 
#print(create_chocolate_bar(2,6)) # ska returnera följande matris:[["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]
#print(create_chocolate_bar(0,0)) # ska returnera följande matris: None
#print(create_chocolate_bar(-1,-1)) # ska returnera följande matris: None
#print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # skriver ut följande: 11 12 13 14 15 16 21 22 23 24 25 26
#print(chomp([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]], 1, 2 ) # skriver ut följande: [["11", "12", "13", "14", "15", "16"], ["21", "22"]]


'''
#tester som står i uppgiftsinstruktionen 
#print(create_chocolate_bar(2,6)) # funkar och ger output [["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]
#print(create_chocolate_bar(0,0)) # funar och ger output None
#print(create_chocolate_bar(-1,-1)) # funar och ger output None
#print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # försöker nu lösa print_chocolate_bar funktionen så att den ska kunna ge output 11 12 13 14 15 16 "\n" 21 22 23 24 25 26
#print(chomp([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]], 1, 2 ) # funkar ännu inte [["11", "12", "13", "14", "15", "16"], ["21", "22"]]

chomp(chocolate_bar_matris, rader, kolumner)
print_chocolate_bar(chocolate_bar_matris)
'''

'''while list.count(chocolate_bar_matris[1,1]) > 1:
    rader = int(input("vilken rad ska vi käka?: "))
    kolumner = int(input("vilken kolumn ska vi käka?: "))
    chomp(chocolate_bar_matris, rader, kolumner)
    print_chocolate_bar(chocolate_bar_matris)'''

'''
gammal version eftersom den inte ska ha flera inparametrar
def print_cholate_bar(antal_rader, antal_kolumner):
    create_chocolate_bar(antal_rader, antal_kolumner)
    for i in chocolate_bar_matris:
        print(*i)
'''

'''
gammal version eftersom den inte ska ha flera inparametrar
def print_cholate_bar(antal_rader, antal_kolumer):
    create_chocolate_bar(antal_rader, antal_kolumer)
    for i in chocolate_bar_matris:
        print(*i)

        global chocolate_bar
        chocolate_bar = []
        chocolate_bar.append(matris[i])
    return chocolate_bar
'''

'''
# test av output: 
print_chocolate_bar(antal_rader, antal_kolumer)

# test av givna värden: 
print_chocolate_bar(4, 5)

# chomp([["11", "12", "13", "14"], ["21", "22", "23", "24"], ["31", "32", "33", "34"]] ,1 ,2)
'''

'''
tallista = [ 5, 4, 7, 8]
print(tallista)
del tallista[1:3]
print( tallista )
[5,8] 
'''

'''
print(create_chocolate_bar(3,4))

def print_chocolate_bar():
    create_chocolate_bar()
    for i in chocolate_bar_matris:
        print(chocolate_bar_matris[i], end="")

print(print(chocolate_bar()))

for i in chocolate_bar_matris:          #skapar for-loop för alla värden i resultat (som då är antalet tärningar vi har)
        resultat_mening+=str(resultat[s])       #klistrar ihop alla resultat i resultat_mening
        if s<antal_tärningar-1:                 #om vi inte är på sista index i resultat kommer vi även klistra på ", " innan vi går till nästa tärningsresultat
            resultat_mening+=", "
    print("Du fick", resultat_mening+".")  
'''

'''
def chomp():
    spelare1 = int(input("Första spelarens tur, välj ett blocknummer: "))
    spelare2 = int(input("Andra spelarens tur, välj ett blocknummer: "))
'''