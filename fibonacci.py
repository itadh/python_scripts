#!/usr/bin/python3
print('0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946, ...')

eingabe = input('Wieviele Fibonacci-Zahlen sollen berechnet werden: ')
eingabe = int(eingabe)

startwert1 = 0
startwert2 = 1

zaehler = 1
while zaehler < eingabe - 1:
   ergebnis = startwert1 + startwert2
   if zaehler == 1:
       gesamtergebnis = f'{startwert1},{startwert2},{ergebnis}'
   else:
       gesamtergebnis = f'{gesamtergebnis},{ergebnis}'
   startwert1 = startwert2
   startwert2 = ergebnis
   zaehler = zaehler + 1
print(f'Fibonacci-Folge: {gesamtergebnis}')


# zaehler = 0
# startwert1 = 0
# startwert2 = 1
# ergebnis = 1
# 
# zaehler = 1
# startwert1 = 1 (startwert2)
# startwert2 = 1 (ergebnis vorheriger Durchlauf)
# ergebnis = 2
# 
# zaehler = 2
# startwert1 = 1 (startwert2)
# startwert2 = 2 (ergebnis vorheriger Durchlauf)
# ergebnis = 3
# 
# zaehler = 3
# startwert1 = 2 (startwert2)
# startwert2 = 3 (ergebnis vorheriger Durchlauf)
# ergebnis = 5
# 


