

# Laboration 5 del 1

'''
orginalinnehåll textfil allatv.txt
Vardagsrums TV,100,22,10,9
Köks TV,50,43,20,5
'''

from TV import TV

#alla funktioner
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

def select_TV_menu(tvlista):
    '''skriver ut namn på alla TV-objekt och ett val att avsluta programmet och låter användaren välja ett TV-objekt eller avsluta'''

    '''
    #försökte göra om den här delen så att den ska skriva ut första menyn på rätt sätt men det gick inte så bra

    tv_names = []
    for tv_name in tvlista:
        tv_name = tvlista[0]
        tv_names.append(tv_name)

    i = 0
    for tv_name in tv_names:
        print(i+1, end=" ")
        print(tv_names[i])
        i+=1
    print(i+1, "Avsluta")
    '''

    i = 0
    for tv_name in tvlista:
        print(i+1, end=" ")
        print(tvlista[i])
        i+=1
    print(i+1, "Avsluta")
    
    print("Välj:", end=" ")
    j = 0
    while j == 0:
        try:
            tv_val = input()
            tv_val = int(tv_val)
            if tv_val in range(1,i+2):
                j += 1
                return tv_val
            else:
                print("Fel val, försök igen:", end=" ")
        except:
            print("Fel val, försök igen:", end=" ")

def adjust_TV_menu():
    '''gör att användaren kan byta kanal, höja och sänka ljudnivån för ett TV-objekt, eller återgå till huvudprogrammet'''
    loop = 0
    while loop == 0: #pernament loop tills användaren skriver ett korekt svar
        try:
            inställningar_val = input("\n1. Byt kanal \n2. Sänk ljudnivå \n3. Höj ljudnivå \n4. Gå till huvudmenyn \nVälj: ")
            inställningar_val = int(inställningar_val)
            if inställningar_val in range(1,5):
                return inställningar_val
            else:
                print("Vänligen skriv ett nummer som tillhör menyvalen.")
        except:
            print("Vänligen skriv ett nummer som tillhör menyvalen.")
    return inställningar_val

def change_channel(tvobjekt):
    '''ber användaren att mata in en ny TV-kanal och ändrar kanalen för det TV-objekt som skickas med som parameter'''
    
    pass

def decrease_volume(tvobjekt):
    '''sänker ljudnivån för det TV-objekt som skickas med som parameter'''

    pass

def increase_volume(inställningar_val):
    '''ökar ljudnivån för det TV-objekt som skickas med som parameter'''
    if inställningar_val == 3:
        TV.increase_volume()

def write_file(tvlista, textfil="allatv.txt"):
    '''tvobjekten i tvlistan skrivs i filen allatv.txt'''
    skriv = open(textfil, "w")
    for tvobjekt in tvlista:
        skriv.write(tvobjekt.str_for_file() + "\n")
    skriv.close()

#huvudprogrammet
def main():
    '''kör huvudprogrammet'''
    print("\n***Välkommen till TV-simulatorn****")
    tvlista = read_file("allatv.txt")
    tv_val = 0

    while tv_val != len(tvlista)+1: #en while loop som avslutas när användaren väljer att avsluta
        tv_val = select_TV_menu(tvlista)
        if tv_val != len(tvlista)+1:
            inställningar_val = adjust_TV_menu()
            while inställningar_val != 4: #en while loop som avslutas när användaren vill gå tillbaka till huvudmenyn
                if inställningar_val == 1:
                    print("\nbra jobbat, du skrev siffran 1!")
                    #fixa change_channel() här
                elif inställningar_val == 2:
                    print("\nbra jobbat, du skrev siffran 2!")
                    #fixa decrease_volume() här
                elif inställningar_val == 3:
                    print("\nbra jobbat, du skrev siffran 3!")
                    increase_volume(inställningar_val)
                inställningar_val = adjust_TV_menu()
    print("Simuleringen avslutas")
    write_file(tvlista)

    #samma kopplad till samma del som inte går helt TV.py
    #tv_information = TV.str_for_tv() 
    #print(tv_information)
        #har testat men den skriver inget efter den här delen!
    #for tv in tvlista:
        #print(tvlista) #inte den


#kör programmet

main()



'''
def save_file(tvlista):
    #sparar de bearbetade värderna och stänger filen
    file=open("allatv.txt","w")
    for tv in tvlista:
        file.write(tv.str_for_file())
    file.close()
'''

'''
#tester
tvlista = read_file("allatv.txt")  
for tv in tvlista: print(tv) #Här ska programmet skriva namn, inställd kanal och ljudnivå för båda tv-aparaten som finns i filen

#Vardagsrums TV, channel: 22, volume: 9
#Köks TV, channel: 43, volume: 5

tvlista[0].decrease_volume()
for tv in tvlista: print(tv) # Här ska programmet skriva ut information om båda tv-aparaterna (Observera att kanalen för första tv:n måste ha ändrats till 1)

#Vardagsrums TV, channel: 1, volume: 9
#KÃ¶ks TV, channel: 43, volume: 5

write_file(tvlista, "allatv.txt")  
tvlista = read_file("allatv.txt")  
for tv in tvlista: print(tv)

#Vardagsrums TV, channel: 1, volume: 9
#Köks TV, channel: 43, volume: 5
'''

'''
#tester
if __name__ == "__main__":
    tv = TV("Vardagsrunms TV", 100, 22, 10, 9)
    tv2 = TV("Sovrums TV", 50, 7, 20, 4)
    print(tv) #Vardagsrums TV, channel: 22, volume: 9
    print(tv2) #Sovrums TV, channel: 7, volume: 4
    print(tv.increase_volume()) #True
    print(tv) #Vardagsrums TV, channel: 22, volume: 10
    print(tv2) #Sovrums TV, channel: 7, volume: 4
    print(tv.increase_volume()) #False
    print(tv) #Vardagsrums TV, channel: 22, volume: 10
    print(tv2) #Sovrums TV, channel: 7, volume: 4
    print(tv.change_channel(55)) #True
    print(tv) #Vardagsrums TV, channel: 55, volume: 10
    print(tv2) #Sovrums TV, channel: 7, volume: 4
    print(tv2.change_channel(55)) #False
    print(tv) #Vardagsrums TV, channel: 55, volume: 10
    print(tv2) #Sovrums TV, channel: 7, volume: 4
'''

'''
fil = open("allatv.txt")
names = fil.readlines()
print(names)

#radsplit = rad.split(",")
#radjoin = " ".join(rad) 
#tvlista.append(radjoin)
#tv_name, max_channel, current_channel, max_volume, current_volume = rad.split(",") 
#int(max_channel), int(current_channel), int(max_volume), int(current_volume)) 
#tvlista existerar inte utanför funktionen i nuläget...

#gammal tester

print("row: 3" , tv)
print("row: 4" , tv2)
print("row: 5" , tv.increase_volume()) #just nu det skriver endast true, utan att ändra volymet
print("row: 6" , tv)
print("row: 7" , tv2)
print("row: 8" , tv.increase_volume())
print("row: 9" , tv)
print("row: 10" , tv2)
print("row: 11" , tv.change_channel(55))
print("row: 12" , tv)
print("row: 13" , tv2)
print("row: 14" , tv2.change_channel(55))
print("row: 15" , tv)
print("row: 16" , tv2)
'''