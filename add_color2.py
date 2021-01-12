#!/usr/bin/python3
gueltige_farben = ['rot', 'grün', 'gelb', 'schwarz', 'weiß', 'lila', 'blau', 'orange' ]
farben = []
farbe = ''
while True:
    if farbe == 'q':
        break
    farbe = input('Bitte geben Sie eine Farbe ein: ')
    for _farbe in gueltige_farben:
        if farbe == _farbe:
            farben.append(farbe)

print(farben)

