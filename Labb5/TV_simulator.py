# Laboration 5 del 1

'''
orginalinnehåll textfilen allatv.txt
Vardagsrums TV,100,22,10,9
Köks TV,50,43,20,5
'''

from TV import TV

# Alla funktioner

def read_file(textfil="allatv.txt"): 
    '''skapar en lista med lika många TV-objekt som i filen allatv.txt'''
    fil = open(textfil) 
    filinnehåll = fil.readlines()
    tvlista = [] 

    for rad in filinnehåll:
        splittrad = rad.split(",")
        tv_name = splittrad[0]
        talen = [int(x) for x in splittrad[1:]]
        tvobjekt = TV(tv_name, *talen) 
        tvlista.append(tvobjekt)
    return tvlista 

def  select_TV_menu(tvlista):
    '''skriver ut namn på alla TV-objekt och ett menyval att avsluta programmet och låter användaren välja ett TV-objekt eller avsluta'''
    i = 0
    for TV in tvlista:
        print(i+1, end=" ")
        print(tvlista[i])
        i+=1
    print(i+1, "Avsluta")
    print("Välj: ", end="")

    j = 0
    while j == 0:
        tv_val = input()
        try:
            tv_val = int(tv_val)
            if tv_val in range(1,i+2):
                j += 1
                print()
                return tv_val
            else:
                print("Fel val, försök igen:", end=" ") #print("Vänligen skriv ett nummer som tillhör menyvalen.")
        except:
            print("Fel val, försök igen:", end=" ") #print("Vänligen skriv ett nummer som tillhör menyvalen.")

def adjust_TV_menu():
    '''gör att användaren kan byta kanal, höja och sänka ljudnivån för ett TV-objekt, eller återgå till huvudprogrammet'''
    loop = 0
    while loop == 0: #while loop tills användaren skriver ett korekt svar
        try:
            inställningar_val = input("\n1. Byt kanal \n2. Sänk ljudnivå \n3. Höj ljudnivå \n4. Gå till huvudmenyn \nVälj: ")
            inställningar_val = int(inställningar_val)
            if inställningar_val in range(1,5):
                return inställningar_val
            else:
                print("Vänligen skriv ett nummer som tillhör menyvalen.")
        except:
            print("Vänligen skriv ett nummer som tillhör menyvalen.")

def change_channel(ett_TV_objekt):
    '''ber användaren att mata in en ny TV-kanal och ändrar kanalen för det TV-objekt som skickas med som parameter'''
    loop = 0
    new_channel = input("\nAnge kanalnummer: ")
    while loop == 0: #while loop tills användaren skriver ett korekt svar 
        try:
            new_channel = int(new_channel)
            if ett_TV_objekt.change_channel(new_channel) == True:
                loop = 1
            else: 
                print("Kanal för den här TV:n ska vara mellan 1 till", ett_TV_objekt.max_channel, ", försök igen:", end=" ")
                new_channel = input()
        except:
            print("Kanal för den här TV:n ska vara mellan 1 till", ett_TV_objekt.max_channel, ", försök igen:", end=" ")
            new_channel = input()
        
def increase_volume(ett_TV_objekt):
    '''ökar ljudnivån för det TV-objekt som skickas med som parameter'''
    ett_TV_objekt.increase_volume()

def decrease_volume(ett_TV_objekt):
    '''sänker ljudnivån för det TV-objekt som skickas med som parameter'''
    ett_TV_objekt.decrease_volume()

def write_file(tvlista, textfil="allatv.txt"):
    '''tvobjekten i tvlistan skrivs i filen allatv.txt'''
    skriv = open(textfil, "w")
    for tvobjekt in tvlista:
        skriv.write(tvobjekt.str_for_file() + "\n")
    skriv.close()

# Huvudprogrammet

def main():
    '''kör huvudprogrammet'''
    print("****Välkommen till TV-simulatorn****")
    tvlista = read_file("allatv.txt")
    tv_val = 0
    while tv_val != len(tvlista)+1: #en while loop som avslutas när användaren väljer att avsluta
        tv_val = select_TV_menu(tvlista)
        if tv_val == len(tvlista)+1:
            break
        if tv_val != "hej":
            print(tvlista[tv_val-1].str_for_tv()) #printar informationen om den valda TV:en
            inställningar_val = adjust_TV_menu()
            while inställningar_val != 5: #en while loop som avslutas när användaren vill gå tillbaka till huvudmenyn
                if inställningar_val == 1:
                    change_channel(tvlista[tv_val-1])
                    print("\n" + tvlista[tv_val-1].str_for_tv())
                elif inställningar_val == 2:
                    decrease_volume(tvlista[tv_val-1])
                    print("\n" + tvlista[tv_val-1].str_for_tv())
                elif inställningar_val == 3:
                    increase_volume(tvlista[tv_val-1])
                    print("\n" + tvlista[tv_val-1].str_for_tv())
                elif inställningar_val == 4:
                    break
                inställningar_val = adjust_TV_menu()
    write_file(tvlista)
    print("Simuleringen avslutas")
    
# Kör huvudprogrammet

main()