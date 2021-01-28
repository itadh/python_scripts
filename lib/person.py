
# funktion show
def show(data, multi_line, counter):
    if multi_line is True:
        print('-' * 66)
        print(f'Vorname: {data["first"]}')
        print(f'Nachname: {data["last"]}')
        print(f'Stadt: {data["city"]}')
    else:
        print(f'{counter}: {data["first"]} - {data["last"]} - {data["city"]}')


# funktion hinzufuegen
def add_person(persons):
    os.system('clear')
    person = dict()
    person['first'] = input('Bitte geben Sie den Vornamen an: ')
    person['last'] = input('Bitte geben Sie den Nachnamen an: ')
    person['city'] = input('Bitte geben Sie die Stadt an: ')
    persons.append(person)


# Daten aus Datei lesen
def read_file(file, persons):
    with open(file, 'r') as fh:
        for line in fh.readlines():
            person = dict()
            line = line[0:-1]
            person['first'], person['last'], person['city'] = line.split(';')
            persons.append(person)


# Datensatz loeschen
def del_person(persons):
    os.system('clear')
    counter = 0
    for person in persons:
        show(person, False, counter)
        counter += 1
    del_dataset = input('Welchen Datensatz möchten Sie löschen: ')
    del persons[int(del_dataset)]
    print(persons)


# Daten in Datei schreiben
def write_file(file, persons):
    keys = list()
    # hole alle Daten aus der Datei
    with open(file, 'r') as fh:
        for line in fh.readlines():
            keys.append(line[:-1])
    with open(file, 'a') as fh:
        for person in persons:
            if f'{person["first"]};{person["last"]};{person["city"]}' in keys:
                continue
            fh.writelines(f'{person["first"]};{person["last"]};{person["city"]}\n')

