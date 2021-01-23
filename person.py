#!/usr/bin/python3
# 
# author: jz@mgeg.de
# change: 21.01.2021
#
 
file_data = '/home/tn/persons.list'

persons = list()
action = True

# get person data
while True:
    print('-' * 30, 'MENU', '-' * 30)
    print('[a] Datensatz anlegen')
    print('[e] Daten aus Datei einlesen')
    print('[z] Daten anzeigen')
    print('[s] Daten in Datei speichern')
    print('[q] Program beenden')
    action = input('Was möchten Sie machen: ')

#    person = dict()
#    person['first'] = input('Bitte geben Sie den Vornamen an: ')
#    person['last'] = input('Bitte geben Sie den Nachnamen an: ')
#    person['city'] = input('Bitte geben Sie die Stadt an: ')
#    persons.append(person)
#    next_action = input('Wollen Sie eine weitere Person erfassen? [j|n]: ')
#    if next_action != 'j':
#        action = False
#
# save the person list
#with open(file_data, 'a') as fh:
#    fh.writelines(f'{persons}')
#
#print(persons)


# Vorname: Fred
# Nachname: Feuerstein
# Stadt: Bonn
#
# Vorname: ...

# Vorname;Nachname;Stadt
# Fred;Feuerstein;Bonn
# Joe;Doe;Essen

