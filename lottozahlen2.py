#import random
#random.seed()
#print("Lottoziehung")
#tipps=input("Welche Zahlen möchten Sie tippen?")
#zahlen=tipps.split(",")
#hier wird die Eingabe konvertiert 
#'meine Zahln' gepeichsert
#meine Zahlen = []
#for z in zahlen:
#l		meineZahlen.append(int(z))
		
#und die Eingabe aufsteigend sortieren,damit diese 
#spaeter auch mit den Lottozahlen vergliche werden kann.


import random
random.seed()

print("Lottoziehung")
	tipps = input ("Welche Zahlen möchten sie tippen?")
	
zahlen = tipps.split(",")

import random

arr2 = []
random.seed()

for i in range(1,46):
	arr2.append(i)

arr1 = []	
for nummer in range(1,7):
	arr1.append(random.randint(1,45))
	arr2.pop(nummer)


meineZahlen = []

