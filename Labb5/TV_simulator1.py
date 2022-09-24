# Laboration 5 del 1

'''
orginalinnehåll textfilen allatv.txt
Vardagsrums TV,100,22,10,9
Köks TV,50,43,20,5
'''

from TV import TV

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

def write_file(tvlista, textfil="allatv.txt"):
    '''tvobjekten i tvlistan skrivs i filen allatv.txt'''
    skriv = open(textfil, "w")
    for tvobjekt in tvlista:
        skriv.write(tvobjekt.str_for_file() + "\n")
    skriv.close()

def change_channel():
    '''ber användaren att mata in en ny TV-kanal och ändrar kanalen för det TV-objekt som skickas med som parameter'''
    
    pass

def increase_volume():
    '''ökar ljudnivån för det TV-objekt som skickas med som parameter'''

    pass

def decrease_volume():
    '''sänker ljudnivån för det TV-objekt som skickas med som parameter'''

    pass

def adjust_TV_menu():
    '''gör att användaren kan byta kanal, höja och sänka ljudnivån för ett TV-objekt, eller återgå till huvudprogrammet'''
    
    pass

def  select_TV_menu(tvlista):
    '''skriver ut namn på alla TV-objekt och ett menyval att avsluta programmet och låter användaren välja ett TV-objekt eller avsluta'''
    i = 0
    for tv in tvlista:
        print(i+1, end=" ")
        print(tvlista[i])
        i+=1
    print(i+1, "Avsluta")

    j = 0
    while j == 0:
        tv_val = input("Välj: ")
        try:
            tv_val = int(tv_val)
            if tv_val in range(1,4):
                j += 1
            else:
                print("Vänligen skriv ett nummer som tillhör menyvalen.")
        except:
            print("Vänligen skriv ett nummer som tillhör menyvalen.")


def main():
    '''kör huvudprogrammet'''
    print("\n***Välkommen till TV-simulatorn****")
    tvlista = read_file("allatv.txt")
    select_TV_menu(tvlista)

    #samma kopplad till samma del som inte går helt TV.py
    
    

#tester
main()
#tv_information =  
#print(TV()str_for_tv())