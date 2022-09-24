# Laboration 4 del 1

#skapar en matris baserat på användarens input
def create_chocolate_bar(antal_rader, antal_kolumner):
    if antal_rader and antal_kolumner >=0: # om användarens input är positiva heltal exekveras funktionen
        global chocolate_bar_matris # gör matrisen global
        chocolate_bar_matris = []
        for r in range(1,antal_rader+1): # skapar en rad där alla tal börjar med värdet av r
            kolumn = []
            for k in range(1,antal_kolumner+1): # fyller raden med kolumner som ökar i värde
                kolumn.append(str(r)+str(k))
            chocolate_bar_matris.append(kolumn) # lägger till raden i matrisen
        return chocolate_bar_matris
    else:
        return None # om användarens input är något annat än positiva heltal returneras None

#skriver ut matrisen i rätt format på separata rader för de inre listorna
def print_chocolate_bar(chocolate_bar_matris):
    for i in range(len(chocolate_bar_matris)):
        for j in range(len(chocolate_bar_matris[i])):
            print(chocolate_bar_matris[i][j], end=" ")
        print()

# användarens valda parametrar
antal_rader = int(input("Hur många rader ska chokladbaren bestå av: "))
antal_kolumner = int(input("Hur många kolumner ska chokladbaren bestå av: "))

create_chocolate_bar(antal_rader, antal_kolumner)
print_chocolate_bar(chocolate_bar_matris)

#klipper ut delar av matrisen
def chomp(chocolate_bar_matris, rader, kolumner):
    for r in reversed(range(len(chocolate_bar_matris))):
        if r >= rader :
            for k in reversed(range(len(chocolate_bar_matris[r]))):
                if k >= kolumner:
                    del chocolate_bar_matris[r][k]

# användarens valda parametrar
rader = int(input("Vilken rad ska vi käka?: ")) - 1
kolumner = int(input("Vilken kolumn ska vi käka?: ")) - 1

# exekverar funktionerna
chomp(chocolate_bar_matris, rader, kolumner)
print_chocolate_bar(chocolate_bar_matris)

# tester som står i uppgiftsinstruktionen 
print(create_chocolate_bar(2,6)) # ska returnera följande matris:[["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]
print(create_chocolate_bar(0,0)) # ska returnera följande matris: None
print(create_chocolate_bar(-1,-1)) # ska returnera följande matris: None
print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # skriver ut följande: 11 12 13 14 15 16 21 22 23 24 25 26

#det här testet funkar fortfarande inte, men det borde inte va nåt större problem, vi kan nog bara ta bort den ur filen innan presentationen sen
#print(chomp([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]], 1, 2 ) # skriver ut följande: [["11", "12", "13", "14", "15", "16"], ["21", "22"]]

