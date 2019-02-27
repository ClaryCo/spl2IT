#02_wuerfelspiel.py
#1.Eingabe wie oft gewürfelt werden soll
#2.EIngabe auf welche Zahl man setzt
#3.Ausgabe:
#gewonnen, wenn die Zahl mind. einmal vorkommt
#verloren wenn man die Zahl nicht vorkommt

# Beispiel
#Wie oft soll gewürfelt werden ? 12
#Auf welche Zahl setzt du ? 5
#1,4,3,4,5,6,
#gewonnen bongbonggggggg

##for zahl in 1,2,3,4,5,6:
	#print(zahl)

#for zahl in (1,7):
	#print(zahl)
	
# for zahl in range (0,10):
	# print(zahl, end= "")
	# print ()


# if(zahl == 10):
	# print("super")
# elif(zahl <10 )
	# print("unspitze")
# else:
	# print("nicht super")
	
wieoftwür = input ("Wie oft soll es gewürfelt werden?")
zahl = input ("Auf welche Zahl tippst du?")
import random
random.seed()


for ausgeben in range(0,wieoftwür):
	zufall = random.radint(1,6)

	if(zahl == zufall):
		print("gewonnen")
	else 
		print("niederlage")
	


