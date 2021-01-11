#!/usr/bin/python3
satz = input('Bitte geben Sie einen Satz ein: ')
woerter = satz.split()
for word in woerter:
    print(word.upper())

