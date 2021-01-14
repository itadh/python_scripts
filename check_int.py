#!/usr/bin/python3
string_zahlen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
eingabe = input('Bitte geben Sie eine Zahl ein: ')

#valid = 0
#for teil in eingabe:
#    for part in string_zahlen:
#        if teil == part:
#            print('ok')
#            valid = valid + 1
#if valid == len(eingabe):
#    print('Eingabe ist eine Zahl')
#    zahl = int(eingabe)

for teil in eingabe:
    valid = False
    for part in string_zahlen:
        if teil == part:
            valid = True            
    if valid is False:
        break

if valid is True:
    print('RICHTIG')
else:
    print('FALSCH')

