#!/usr/bin/python3


person = {}
person['first'] = input('Bitte geben Sie den Vornamen ein: ')
person['last'] = input('Bitte geben Sie den Nachnamen ein: ')
person['city'] = input('Bitte geben Sie die Stadt ein: ')

print(person)

for _person in person:
    print(_person)
    print(person[_person])

print('-' * 40)

for key,value in person.items():
    print(f'{key}: {value}')


A1
rot.blau.grün
