# Laboration 4 del 2

def write_intro():
    '''skriver spelintroduktionen'''
    print("\nVälkommen till spelet Chomp!\n")
    print("Instruktioner:\nI spelet kommer du utmanas om att välja ett blocknummer från spelplanen.\nDet valda blocket och alla block under och till högre kommer att raderas.\nSpelet går ut på att undvika välja P, den spelare som väljer P förlorar\noch den andra spelare vinner.\n")

def create_chocolate_bar(antal_rader, antal_kolumner): 
    '''skapar en matris baserat på användarens input'''
    if antal_rader and antal_kolumner >=0: # om användarens input är positiva heltal exekveras funktionen
        chocolate_bar_matris = []
        for r in range(1,antal_rader+1): # skapar en rad där alla tal börjar med värdet av r
            kolumn = []
            for k in range(1,antal_kolumner+1): # fyller raden med kolumner som ökar i värde
                kolumn.append(str(r)+str(k))
            chocolate_bar_matris.append(kolumn) # lägger till raden i matrisen
        chocolate_bar_matris[0][0] = "P "
        return chocolate_bar_matris
    else:
        return None # om användarens input är något annat än positiva heltal returneras None

#skriver ut matrisen i rätt format på separata rader för de inre listorna
def print_chocolate_bar(chocolate_bar_matris):
    for rad in chocolate_bar_matris: #bestämmer första siffran i en "bit" (beroende på raden)
        for cell in rad: #bestämmer andra siffran i en "bit" (beroende på kolumnen)
            print(cell, end=" ") #skriver ut "biten" beroende på i och j, repeterar tills raden är full
        print() #skapar en mellanrum så nästa rad kan bli inskriven

# användarens valda parametrar chomp
def ask_cellnumber(chocolate_bar_matris):
    spelar_input = int(input("Välj en ruta: "))
    spelar_input_split = [int(a) for a in str(spelar_input)]
    käkad_rad = int(spelar_input_split[0] - 1)
    käkad_kolumn = int(spelar_input_split[1] - 1)
    return käkad_rad, käkad_kolumn

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

def check_winner(chocolate_bar_matris):
    if len(chocolate_bar_matris) == 1:
        if len(chocolate_bar_matris[0])== 1:
            return True
    else:
       return False #stod inte i första punkten vad som ska retuneras eller skrivas utöver detta men man ska nog lägger till det sen!!


#huvudprogramm
def play_chomp():
    write_intro()
    antal_rader = int(input("Hur många rader ska chokladbaren bestå av: "))
    antal_kolumner = int(input("Hur många kolumner ska chokladbaren bestå av: "))
    chocolate_bar = create_chocolate_bar(antal_rader, antal_kolumner)
    print_chocolate_bar(chocolate_bar)

    while True:
        käkad_rad, käkad_kolumn = ask_cellnumber(chocolate_bar)
        print(käkad_rad, käkad_kolumn)
        chocolate_bar = chomp(chocolate_bar, käkad_rad, käkad_kolumn)
        print_chocolate_bar(chocolate_bar)
        #create_chocolate_bar(antal_rader, antal_kolumner)
        #print_chocolate_bar(chocolate_bar_matris)
        #
        #print(chocolate_bar_matris)
        
        #ask_cell_number() ger ett antal felmeddelande i nuläget!
        #chomp()
        #check_winner()

play_chomp()
