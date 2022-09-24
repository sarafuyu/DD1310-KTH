# Laboration 4 del 1

#skapar en matris baserat på användarens input
def create_chocolate_bar(antal_rader, antal_kolumner):
    if antal_rader and antal_kolumner >=0: # om användarens input är positiva heltal exekveras funktionen
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
    for rad in chocolate_bar_matris: #bestämmer första siffran i en "bit" (beroende på raden)
        for cell in rad: #bestämmer andra siffran i en "bit" (beroende på kolumnen)
            print(cell, end=" ") #skriver ut "biten" beroende på i och j, repeterar tills raden är full
        print() #skapar en mellanrum så nästa rad kan bli inskriven

#klipper ut delar av matrisen
def chomp(chocolate_bar_matris, käkad_rad, käkad_kolumn):
    for r in reversed(range(len(chocolate_bar_matris))): #checkar för matrisens längd, använder svaren för en reverse range funktion
        if r >= käkad_rad :
            for k in reversed(range(len(chocolate_bar_matris[r]))): #checkar för längden av listan i matrisen, därefter används i reverse range funktion
                if k >= käkad_kolumn:
                    del chocolate_bar_matris[r][k]
                    if len(chocolate_bar_matris[r]) == 0:
                        del chocolate_bar_matris[r]
    return chocolate_bar_matris

# användarens valda parametrar, används för att skapa matrisen i rad 4
antal_rader = int(input("Hur många rader ska chokladbaren bestå av: "))
antal_kolumner = int(input("Hur många kolumner ska chokladbaren bestå av: "))

chocolate_bar_matris = create_chocolate_bar(antal_rader, antal_kolumner)
print_chocolate_bar(chocolate_bar_matris)

# användarens valda parametrar
käkad_rad = int(input("Vilken rad ska vi käka?: ")) - 1
käkad_kolumn = int(input("Vilken kolumn ska vi käka?: ")) - 1

# exekverar funktionerna
chomp(chocolate_bar_matris, käkad_rad, käkad_kolumn)
print_chocolate_bar(chocolate_bar_matris)

# tester som står i uppgiftsinstruktionen 
print(create_chocolate_bar(2,6)) # ska returnera följande matris:[["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]
print(create_chocolate_bar(0,0)) # ska returnera följande matris: None
print(create_chocolate_bar(-1,-1)) # ska returnera följande matris: None
print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # skriver ut följande: 11 12 13 14 15 16 "/n" 21 22 23 24 25 26
print(chomp([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]], 1, 0 )) # skriver ut följande: [["11", "12", "13", "14", "15", "16"], ["21", "22"]]
