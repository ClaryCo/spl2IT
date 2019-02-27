
frage = input ("Auf welche Zahl setzt du")
frage = int (frage)

i = input("Wie oft soll gewprfelt werden")
i = int (i)
counter = 0;

for nummer in range(0,i):
	import random
	random.seed()
	zahl = random.radint(1,6)
	print(zahl(
	
	if(frage == zahl):
		counter = counter + 1
		print("Gewonnen!Die Zahl", frage "kommt", counter,"mal vor")
		
	else:
		print("verloren")


