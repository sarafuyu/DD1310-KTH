# Laboration 4 del 1

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

#början på sista funktionen, ska kolla exakt hur man använder del
'''
def chomp(chocolate_bar_matris, rader, kolumner):
    for r in chocolate_bar_matris(rader):
        del chocolate_bar_matris()
        for k in range (kolumner, antal_kolumner):
            del chocolate_bar_matris([r]:k]
    return chocolate_bar_matris
'''

'''
rader = int(input("vilken rad ska vi käka?: ")) - 1
kolumner = int(input("vilken kolumn ska vi käka?: ")) - 1
chomp(chocolate_bar_matris, rader, kolumner)
print_chocolate_bar(chocolate_bar_matris)
'''

'''while list.count(chocolate_bar_matris[1,1]) > 1:
    rader = int(input("vilken rad ska vi käka?: "))
    kolumner = int(input("vilken kolumn ska vi käka?: "))
    chomp(chocolate_bar_matris, rader, kolumner)
    print_chocolate_bar(chocolate_bar_matris)
'''

# användarens valda parametrar
antal_rader = int(input("Hur många rader ska chokladbaren bestå av: "))
antal_kolumner = int(input("Hur många kolumner ska chokladbaren bestå av: "))

# tester av outputs
'''
create_chocolate_bar(antal_rader, antal_kolumner)
print_chocolate_bar(chocolate_bar_matris)
'''

#tester som står i uppgiftsinstruktionen 
#print(create_chocolate_bar(2,6)) # funkar och ger rätt output [["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]
#print(create_chocolate_bar(0,0)) # funar och ger rätt output None
#print(create_chocolate_bar(-1,-1)) # funar och ger rätt output None
#print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # funkar och ger rätt output 11 12 13 14 15 16 "\n" 21 22 23 24 25 26
#print(chomp([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]], 1, 2 ) # funkar ännu inte. ska ge rätt output [["11", "12", "13", "14", "15", "16"], ["21", "22"]]