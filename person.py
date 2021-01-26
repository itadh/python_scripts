#!/usr/bin/python3
# 
# author: jz@mgeg.de
# change: 21.01.2021
#
 
file_data = '/home/tn/persons.list'

persons = list()
action = True


def show(data, multi_line, counter):
    if multi_line is True:
        print('-' * 66)
        print(f'Vorname: {data["first"]}')
        print(f'Nachname: {data["last"]}')
        print(f'Stadt: {data["city"]}')
    else:
        print(f'{counter}: {data["first"]} - {data["last"]} - {data["city"]}')


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
        _person = dict()
        _person['first'] = input('Bitte geben Sie den Vornamen an: ')
        _person['last'] = input('Bitte geben Sie den Nachnamen an: ')
        _person['city'] = input('Bitte geben Sie die Stadt an: ')
        persons.append(_person)

    # Daten aus Datei einlesen
    if action == 'e':
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

    # Datensatz löschen
    if action == 'd':
        counter = 0
#        new_persons = list()
        for _person in persons:
#            print('-' * 66)            
#            print(f'ID: {counter}')
#            print(f'Vorname: {_person["first"]}')
#            print(f'Nachname: {_person["last"]}')
#            print(f'Stadt: {_person["city"]}')
#            print('')
            show(_person, False, counter)
            counter += 1
        del_dataset = input('Welchen Datensatz möchten Sie löschen: ')
        del persons[int(del_dataset)]
#        counter2 = 0
#        for _person in persons:
#            if int(del_dataset) != counter2:
#                new_persons.append(_person)
#            counter2 += 1
#        persons = new_persons
        print(persons)

    # Daten anzeigen
    if action == 'z':
        counter = 0
        for _person in persons:
            show(_person, True, counter)
            counter += 1

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

