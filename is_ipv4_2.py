#!/usr/bin/python3
string_zahlen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = 0

# Hauptschleife
while result != 4:
    eingabe = input('Bitte geben Sie eine IPv4 Adresse an: ')
    teile = eingabe.split('.')
    result = 0
    # es muessen 4 Oktetts sein
    if len(teile) == 4:
        # Fuer jedes Oktett
        for teil in teile:

            valid = 0
            # fuer jedes Zeichen
            for _teil in teil:
                # pruefe ob das Zeichen eine Zahl
                for part in string_zahlen:
                    if _teil == part:
                        valid = valid + 1
            # Zeichen sind alles Zahlen
            if valid == len(teil):
                teil = int(teil)
                # Ist das Oktett gueltig
                if teil >= 0 and teil <= 255:
                    result = result + 1
            
    if result == 4:
        print('Alles gut')
    else:
        print('Ihre Eingabe ist keine gültige IPv4 Adresse.')

