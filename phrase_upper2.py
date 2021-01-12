#!/usr/bin/python3
satz = input('Bitte geben Sie einen Satz ein: ')
woerter = satz.split()
for word in woerter:
    line = ''
    for zeichen in word.upper():
        line = f'{line} {zeichen}'
    print(line)

