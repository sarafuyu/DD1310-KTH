# Laboration 4 del 2

def write_intro():
    '''skriver spelintroduktionen'''
    print("\nVälkommen till spelet Chomp.\n")
    print("Instruktioner: I spelet kommer du utmanas om att välja ett blocknummer från spelplanen. Det\nvalda blocket och alla block under och till högre kommer att raderas. Spelet går ut på att\nundvika välja P. Den spelare som väljer P förlorar och den andra spelare vinner.\n")

def create_chocolate_bar(): 
    '''skapar en matris baserat på användarens input'''
    #kontrollerar användarens val av rader
    j = 0
    while j == 0:
        antal_rader = input("Hur många rader ska chokladbaren bestå av: ") 
        try:
            antal_rader = int(antal_rader)
            if antal_rader in range (2,10):
                j += 1
            else:
                print("Antal rader måste vara mellan 2 och 9, försök igen!")
        except:
            print("Antal rader måste vara mellan 2 och 9, försök igen!")
    #kontrollerar användarens val av kolumner
    k = 0
    while k == 0:
        antal_kolumner = input("Hur många kolumner ska chokladbaren bestå av: ")
        try:
            antal_kolumner=int(antal_kolumner)
            if antal_kolumner in range (2,10):
                k += 1
            else:
                print("Antal kolumner måste vara mellan 2 och 9, försök igen!")
        except:
            print("Antal kolumner måste vara mellan 2 och 9, försök igen!")
    #skapar en matris baserat på användarens valda parametrar 
    chocolate_bar_matris = []
    for r in range(1,antal_rader+1): # skapar en rad där alla tal börjar med värdet av r
        kolumn = []
        for k in range(1,antal_kolumner+1): # fyller raden med kolumner som ökar i värde
            kolumn.append(str(r)+str(k))
        chocolate_bar_matris.append(kolumn) # lägger till raden i matrisen
    chocolate_bar_matris[0][0] = "P "
    return chocolate_bar_matris

def print_chocolate_bar(chocolate_bar_matris):
    '''skriver ut matrisen i rätt format på separata rader för de inre listorna'''
    for rad in chocolate_bar_matris: #påbörjar utskriften av alla rader
        for cell in rad: #skriver ut alla celler i en rad med mellanrum
            print(cell, end=" ")
        print() #skapar ett radbyte

def ask_cellnumber(chocolate_bar_matris, counter):
    '''gör om användarens in-data till värden som används i funktionen chomp()'''
    #beroende på räknaren kommer funktionen skriva ut vilken spelares tur det är
    if counter < 2:
        print("Första spelarens tur, välj ett blocknummer:", end=" ")
        counter += 1
    else:
        print("Andra spelarens tur, välj ett blocknummer:", end=" ")
        counter -= 1
    #gör om spelarens valda cell till indexen för den rad och kolumn som cellen motsvarar
    while True:
        spelar_input = int(input())
        spelar_input_split = [int(a) for a in str(spelar_input)]
        käkad_rad = spelar_input_split[0] - 1
        käkad_kolumn = spelar_input_split[1] - 1
        #kontrollerar att spelaren skrivit rätt typ av input
        if käkad_rad + käkad_kolumn != 0:
            if käkad_rad in range(0, len(chocolate_bar_matris)):
                if käkad_kolumn in range(0, len(chocolate_bar_matris[käkad_rad])):
                    return käkad_rad, käkad_kolumn, counter
                else:
                    print(spelar_input, "är ett ogilltigt blocknummer, försök igen:", end=" ")
            else:
                print(spelar_input, "är ett ogilltigt blocknummer, försök igen:", end=" ")
        else:
            print(spelar_input, "är ett ogilltigt blocknummer, försök igen:", end=" ")

def chomp(chocolate_bar_matris, käkad_rad, käkad_kolumn):
    '''klipper ut alla celler nedanför och till höger om vald cell i matrisen'''
    #räknar raderna bakifrån och startar funktionen vid raden av den cell som spelaren valt sedan tidigare
    for rad in reversed(range(len(chocolate_bar_matris))): 
        if rad >= käkad_rad : 
            #räknar bakifrån och tar bort alla celler i den raden fram tills den kolumn som motsvarar spelarens valda cell
            for kolumn in reversed(range(len(chocolate_bar_matris[rad]))): 
                if kolumn >= käkad_kolumn:
                    del chocolate_bar_matris[rad][kolumn]
                    if len(chocolate_bar_matris[rad]) == 0:
                        del chocolate_bar_matris[rad]
    return chocolate_bar_matris

def check_winner(chocolate_bar_matris):
    '''undersöker om det bara finns en cell kvar, dvs om spelet är över'''
    if len(chocolate_bar_matris) == 1:
        if len(chocolate_bar_matris[0])== 1:
            return False
        else:
            return True
    else:
       return True

def main():
    '''anropar alla funktioner i programmet för att två personer ska kunna spela chomp'''
    write_intro()
    chocolate_bar = create_chocolate_bar()
    print_chocolate_bar(chocolate_bar)
    
    counter = 1 
    while check_winner(chocolate_bar) == True:
        i = 0
        while i == 0:
            try: 
                käkad_rad, käkad_kolumn, counter = ask_cellnumber(chocolate_bar, counter) 
                i = +1
            except:
                print("OBS: skriv en godtycklig ruta tack")
        chocolate_bar = chomp(chocolate_bar, käkad_rad, käkad_kolumn)
        print_chocolate_bar(chocolate_bar)
        check_winner(chocolate_bar)
        
    if counter == 1:
        print("Spelet är slut, Vinnare är andra spelaren!")
    else:
        print("Spelet är slut, Vinnare är första spelaren!")

main() #anropar huvudfunktionen och startar därför spelet