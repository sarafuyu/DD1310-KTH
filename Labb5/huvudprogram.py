from minmodul import *

p1 = Person("Kalle",55)
p2 = Person("Klara",50)


print(p1,p2)

if p1 > p2:
    print(p1.namn, "ar tyngre an ", p2.namn)
else:
    print(p2.namn, "ar tyngre an ", p1.namn)


p3 = Person("Klara",50)
    
if p3 == p2:
    print(p2.namn, "ar samma person som ", p3.namn)
else:
    print(p2.namn, "och ", p3.namn, "ar olika personer")
    

p3 = p2
if p3 is p2:
    print(p2.namn, "ar likadan som ", p3.namn)
else:
    print(p2.namn, "ar olika ", p3.namn)
