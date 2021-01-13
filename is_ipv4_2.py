#!/usr/bin/python3
result = 0
while result != 4:
    eingabe = input('Bitte geben Sie eine IPv4 Adresse an: ')
    teile = eingabe.split('.')
    result = 0
    if len(teile) == 4:
        for teil in teile:
            teil = int(teil)
            if teil >= 0 and teil <= 255:
                result = result + 1
            
    if result == 4:
        print('Alles gut')
    else:
        print('Ihre Eingabe ist keine gültige IPv4 Adresse.')

