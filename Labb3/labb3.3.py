# Laboration 3 - Uppgift 3: Slingor och listor

antal_tärningar=int(input("Hur många tärningar behövs i spelet? "))
antal_kast=int(input("Hur många kast får en spelare? "))

from random import randint

while True:           #loopen så att spelet inte slutar efter en runda, vi använder while loop då vi inte vet hur många gånger vi behöver loopa den
    start=input("Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A: ")
    if start=="A":                  #stoppar programmet om använder skriver A
        print("Hej då!")
        break

    for k in range(0,antal_kast):       #använder for-loop då vi vet hur många gånger vi ska loopa den
        resultat=[]
        for i in range(0,antal_tärningar):        #använder for-loop då vi vet hur många gånger man ska loopa den
            resultat.append(randint(1,6))           #genererar random nummer för tärningarna och lägger in dem i listorna
            print("Tärning",i+1,":", resultat[i])

        if k < antal_kast-1:       #om spelaren har kast kvar och inte är på sitt sista kast (det är därför vi har antal_kast-1) kommer vi fråga om hen vill kasta igen
            omstart=input("Är du inte nöjd kan du kansta igen, vill du kasta igen?(j/n) ")
            if omstart=="n":
                break               #tar oss ur for-loopen om spelaren inte vill kasta igen

    resultat_mening=', '.join([str(x) for x in resultat])
    print("Du fick", resultat_mening+".")

    '''
    resultat_mening=", ".join([])          #tom variabel där vi kommer skriva in alla tärningslag

    for s in range(0,antal_tärningar):          #skapar for-loop för alla värden i resultat (som då är antalet tärningar vi har)
        resultat_mening+=str(resultat[s])       #klistrar ihop alla resultat i resultat_mening
        if s<antal_tärningar-1:                 #om vi inte är på sista index i resultat kommer vi även klistra på ", " innan vi går till nästa tärningsresultat
            resultat_mening+=", "
    print("Du fick", resultat_mening+".")    #skriver ut allt med sista värdet och punkt i slutet
    '''