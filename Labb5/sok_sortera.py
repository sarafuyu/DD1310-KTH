class TV(object):

    def __init__(self, m, s):
        self.marke = m
        self.storlek = s

    def geMarke(self):
        return self.marke

    def geStorlek(self):
        return self.storlek

    def __str__(self):
        return self.marke+" "+str(self.storlek)

    def __lt__(self, other):
        if self.storlek < other.storlek:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.marke == other.marke:
            return True
        return False
        
        


def sok(lista, kriterie, sokord):
    listut=[]
    for t in lista:
        if sokord == kriterie(t):
            listut.append(t)
    return listut




tvlista = [ TV("LG",12),
            TV("Samsung",24),
            TV("LG",32),
            TV("IKEA",50),
            TV("Samsung", 12)]




#print("Soker efter TV med storleken 12:")
#tvlist12tum = sok(tvlista, TV.geStorlek, 12)
tvlist12tum = sok(tvlista, TV.geStorlek ,12)

for t in tvlist12tum:
    print(t)
print()
input()

tvlist12tum = sok(tvlista, TV.geMarke,"Samsung")

for t in tvlist12tum:
    print(t)
print()
input()

#print("soker efter TV med market Samsung:")
#tvlistaSamsung = sok(tvlista,TV.geMarke,"Samsung")
#for t in tvlistaSamsung:
#    print(t)
#print()
#
#
#
#
##tvlista = [TV("LG",21), TV("Samsung",20), TV("LG",32), TV("IKEA",50), TV("Samsung", 12)]
#for t in tvlista:
#    print(t)
#print()
#
print("Returnerar en sorterad kopia av listan efter marke:")
nytvlista = sorted(tvlista)
#tvlista.sort()
for t in tvlista:
    print(t)
print()
#
#
