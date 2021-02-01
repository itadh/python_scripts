"""
Einkaufsliste
"""

class Cart ():


    def __init__(self, file_data):
        """
        Konstruktor, Laed Daten aus Datei

        :param  file_data: Datei in der die Daten gespeichert sind
        """
        self.cart = list()
        self.file_data = file_data
        with open(self.file_data, 'r') as fh:
            for line in fh.readlines():
                line = line[:-1]
                part = line.split(';')
                self.cart.append({'name': part[0], 'amount': part[1]})


    def create(self, name=None, amount=None):
        """
        Haengt ein neues Produkt an die Liste

        :param  name: Name des Produktes
        :param  amount : Anzahl des Produktes
        """
        if None in (name, amount):
            print('missing argument')
        self.cart.append({'name': name, 'amount': amount})
        return(True)


    def save(self):
        """
        speichert die Einkaufsliste in eine Datei
        """
        with open(self.file_data, 'w') as fh:
            for cart in self.cart:
                fh.writelines(f'{cart["name"]};{cart["amount"]}\n')


    def show(self, id=None):
        """
        :param  id: Identnummer des Produktes

        zeige Produkte an
        """
        counter = 0
        for product in self.cart:
            print('-' * 60)
            if id is True:
                print(f'ID:      {counter}')               
            print(f'Name:    {product["name"]}')
            print(f'Menge:   {product["amount"]}')
            print('')
            counter += 1


    def delete(self):
        """
        entferne ein Produkt
        """
        self.show(id=True)
        item_to_delete = int(input('Welches Produkt wollen Sie entfernen: '))
        del self.cart[item_to_delete]


