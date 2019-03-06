#Llottozahlen.py

#Zahlen von 1 bis 45 in einer List
#6 x ziehen (ohne Zurückliegen)
# Ausgabe der gezogenen Zhalen in aufsteigener Reihenfolge
# z.B
#Lottoziehung von heute: 
#Es wurden die folgenden Zhalen gezogen 
#1,12,23,41,42 und 45

#import random
#random.seed()

#lottozahlen = [1,2,3,4......,44,45]
#zahl = radint (1,45)

import random

arr2 = []
random.seed()

for i in range(1,46):
	arr2.append(i)

arr1 = []	
for nummer in range(1,7):
	arr1.append(random.randint(1,45))
	arr2.pop(nummer)

print("Die Lottozahlen sind:", arr1)

	


