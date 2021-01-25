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
    print('[d] Datensatz löschen')
    print('[e] Daten aus Datei einlesen')
    print('[z] Daten anzeigen')
    print('[s] Daten in Datei speichern')
    print('[q] Program beenden')
    action = input('Was möchten Sie machen: ')

    # Datensatz anlegen
    if action == 'a':
#        print(f'Sie drückten "{action}"')
        _person = dict()
        _person['first'] = input('Bitte geben Sie den Vornamen an: ')
        _person['last'] = input('Bitte geben Sie den Nachnamen an: ')
        _person['city'] = input('Bitte geben Sie die Stadt an: ')
        persons.append(_person)

    # Daten aus Datei einlesen
    if action == 'e':
#        print(f'Sie drückten "{action}"')
        with open(file_data, 'r') as fh:
            for line in fh.readlines():
                person = dict()
                line = line[0:-1]
                person['first'], person['last'], person['city'] = line.split(';')
                persons.append(person)
#            print(persons)
#                _person = line.split(';')
#                person['first'] = _person[0]
#                person['last'] = _person[1]
#                person['city'] = _person[2]

    # Daten anzeigen
    if action == 'z':
 #       print(f'Sie drückten "{action}"')
        for _person in persons:
            print('-' * 66)
            print(f'Vorname: {_person["first"]}')
            print(f'Nachname: {_person["last"]}')
            print(f'Stadt: {_person["city"]}')
            print('')

    # Daten in Datei schreiben
    if action == 's':
        print(f'Sie drückten "{action}"')
        with open(file_data, 'a') as fh:
            for _person in persons:
                fh.writelines(f'{_person["first"]};{_person["last"]};{_person["city"]}\n')

    # Program beenden
    if action == 'q':
        print(f'Sie drückten "{action}"')
        break

print('Das Program wurde erfolgreich beendet.')


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

