"""
Liste mit kaufbaren Produkten
"""

class Products ():


    def __init__(self, file_data):
        """
        Konstruktor, Laed Daten aus Datei

        :param  file_data: Datei in der die Daten gespeichert sind
        """
        self.products = list()
        self.file_data = file_data
        with open(self.file_data, 'r') as fh:
            for line in fh.readlines():
                line = line[:-1]
                part = line.split(';')
                self.products.append({'name': part[0], 'price': part[1], 'size': part[2]})


    def create(self, name=None, price=None, size=None):
        """
        Haengt ein neues Produkt an die Liste

        :param  name: Name des Produktes
        :param  prize: Preis des Produktes
        :param  size: Einheit des Produktes
        """
#        if name is None:
#            print('fehlendes Argument "name"')
#        if price is None:
#            print('fehlendes Argument "price"')
#        if size is None:
#            print('fehlendes Argument "size"')
        if None in (name, price, size):
            print('missing argument')
#        product = dict()
#        self.product['name'] = name
#        product['prize'] = prize
#        product['size'] = size
        self.products.append({'name': name, 'price': price, 'size': size})
        return(True)


    def save(self):
        """
        speichert die Produktliste in eine Datei
        """
        with open(self.file_data, 'w') as fh:
            for product in self.products:
                fh.writelines(f'{product["name"]};{product["price"]};{product["size"]}\n')


    def show(self, id=None):
        """
        :param  id: Identnummer des Produktes

        zeige Produkte an
        """
        counter = 0
        for product in self.products:
            print('-' * 60)
            if id is True:
                print(f'ID:      {counter}')               
            print(f'Name:    {product["name"]}')
            print(f'Preis:   {product["price"]}')
            print(f'Einheit: {product["size"]}')
            print('')
            counter += 1


    def delete(self):
        """
        entferne ein Produkt
        """
        self.show(id=True)
        item_to_delete = int(input('Welches Produkt wollen Sie loeschen: '))
        del self.products[item_to_delete]


