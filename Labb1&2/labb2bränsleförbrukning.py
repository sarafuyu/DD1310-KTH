# Laboration 2 - Uppgift 1: Bränsleförbrukning

# scenario:

'''
Ange körsträcka i km: 189.7
Ange förbrukat bränsle i liter: 14.5
Bränsleförbrukningen för bilen är 7.644 l/100 km.
'''

# lösningen börjar här
# svar_körsträcka ex.

användare_körsträcka = input("Ange körsträcka i km: ") # sätter variabelns värde till användarens input (str)
körsträcka = float(användare_körsträcka) # ändrar värdets klass till float (flyttal)

användare_bränsle = input("Ange förbrukat bränsle i liter: ") #sätter variabelns värde till användarens input (str)
bränsle = float(användare_bränsle) # ändrar värdets klass till float (flyttal)

förbrukning = 100*bränsle/körsträcka # beräknar bilens bränsleförbrukning per 100 kilometer 
avrundad_förbrukning = round(förbrukning, 3) # avrundar resultatet till tre decimaler

print("Bränsleförbrukningen för bilen är", avrundad_förbrukning, "l/100 km.") # visar resultatet med avrundning till 3 decimalers noggrannhet