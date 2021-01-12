#!/usr/bin/python3
farben = []
farbe = ''
while True:
    if farbe == 'q':
        break
    farbe = input('Bitte geben Sie eine Farbe ein: ')
#    if farbe != 'q' and farbe != '':
#        farben.append(farbe)
    if farbe == 'q' or farbe == '':
        continue
    farben.append(farbe)

print(farben)

