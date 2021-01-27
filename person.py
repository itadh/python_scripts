#!/usr/bin/python3
# 
# author: jz@mgeg.de
# change: 21.01.2021
#
import os
import lib.person
#import ./lib/person.py

os.system('clear')
 
file_data = '/home/tn/persons.list'

persons = list()
action = True


# get person data
while True:
    print('-' * 30, 'MENU', '-' * 30)
    print('[a] Datensatz anlegen')
    print('[d] Datensatz löschen')
    print('[e] Daten aus Datei einlesen')
    print('[z] Daten anzeigen')
    print('[s] Daten in Datei speichern')
    print('[q] Program beenden')
    action = input('Was möchten Sie machen: ')

    # Datensatz anlegen
    if action == 'a':
        lib.person.add_person(persons)

    # Daten aus Datei einlesen
    if action == 'e':
        lib.person.read_file(file_data, persons)

    # Datensatz löschen
    if action == 'd':
        lib.person.del_person(persons)

    # Daten anzeigen
    if action == 'z':
        os.system('clear')
        counter = 0
        for person in persons:
            lib.person.show(person, True, counter)
            counter += 1

    # Daten in Datei schreiben
    if action == 's':
        lib.person.write_file(file_data, persons)

    # Program beenden
    if action == 'q':
        print(f'Sie drückten "{action}"')
        break

print('Das Program wurde erfolgreich beendet.')

