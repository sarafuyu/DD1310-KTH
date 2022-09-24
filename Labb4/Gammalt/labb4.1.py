# Laboration 4 del 1

def create_chocolate_bar(antal_rader, antal_kolumer):
    if antal_rader and antal_kolumer >=0:
        global chocolate_bar_matris
        chocolate_bar_matris = []
        for r in range(1,antal_rader+1):
            kolumn = []
            for k in range(1,antal_kolumer+1):
                kolumn.append(str(r)+str(k))
            chocolate_bar_matris.append(kolumn)
        return chocolate_bar_matris
    else:
        return None

# användarens valda parametrar
antal_rader = int(input("Hur många rader ska chokladbaren bestå av: "))
antal_kolumer = int(input("Hur många kolumer ska chokladbaren bestå av: "))

# användbart exempel
def print_chocolate_bar(chocolate_bar_matris):
    for k in range(len(chocolate_bar_matris)):
        for x in range(len(chocolate_bar_matris[k])):
            print(chocolate_bar_matris[k][x], end=" ")
        print()

# ger rätt output enligt testet men är värdelös...
'''
def print_chocolate_bar(matris): #matris=chocolate_bar_matris?
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print()
'''
# test av output:
print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # ger: 11 12 13 14 15 16 "\n" 21 22 23 24 25 26
print_chocolate_bar(chocolate_bar_matris)

#början på sista funktionen, ska kolla exakt hur man använder del
'''def chomp(chocolate_bar_matris, rader, kolumer):
    for i in range(rader, antal_rader):
        del.chocolate_bar_matris(i)
    return chocolate_bar_matris
'''

#tester som står i uppgiftsinstruktionen 
#print(create_chocolate_bar(2,6)) # funkar och ger output [["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]
#print(create_chocolate_bar(0,0)) # funar och ger output None
#print(create_chocolate_bar(-1,-1)) # funar och ger output None
#print_chocolate_bar([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]]) # ger: 11 12 13 14 15 16 "\n" 21 22 23 24 25 26
#print(chomp([["11", "12", "13", "14", "15", "16"], ["21", "22", "23", "24", "25", "26"]], 1, 2 ) # funkar ännu inte [["11", "12", "13", "14", "15", "16"], ["21", "22"]]