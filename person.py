#!/usr/bin/python3
persons = list()
action = True
while action is True:
    person = dict()
    person['first'] = input('Bitte geben Sie den Vornamen an: ')
    person['last'] = input('Bitte geben Sie den Nachnamen an: ')
    person['city'] = input('Bitte geben Sie die Stadt an: ')
    persons.append(person)
    next_action = input('Wollen Sie eine weitere Person erfassen? [j|n]: ')
    if next_action != 'j':
        action = False
print(persons)

