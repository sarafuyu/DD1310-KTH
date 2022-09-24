from minmodul import *

def lasfil():
    f=open("personer.txt")
    allt=f.readlines()
    personlista=[]
    
    for rad in allt:
        namn,vikt=rad.split(" ")
        p=Person(namn, int(vikt))
        personlista.append(p)
    return personlista


def sparafil(listan):
    f=open("personer.txt","w")
    for person in listan:
        namn=person.namn
        vikt=person.vikt
        f.write(namn+" "+str(vikt)+"\n")
    f.close()

def bytNamn(person):
    nyttNamn=input("Ange nytt namn for "+person.namn+":")
    person.bytNamn(nyttNamn)

def skrivListan(listan):
    i=1
    for p in listan:
        print(i,".",p)
        i+=1
        
listan=lasfil()

nr=0
while nr!=len(listan)+1:
    skrivListan(listan)
    print(len(listan)+1,". Avsluta\nvalj:")
    nr = int(input("Ange nummer for den person som ska byta namn:"))
    if 0<nr<=len(listan):
        bytNamn(listan[nr-1])

sparafil(listan)

