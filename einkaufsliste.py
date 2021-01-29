#!/usr/bin/python3

import os
#import lib.Product as product
import lib.Products as products


os.system('clear')

"""
* Warenkorb Produkte hinzufügen
** Daten sichern 
* Warenkorb Produkte entfernen
** Daten sichern 

* Produkt anlegen
** Daten sichern 
* Produkt loeschen
** Daten sichern 
* Produkt anpassen
** Daten sichern 
* Produkt anzeigen
** Daten sichern 
"""

# Liste aller kaufbaren Produkte
products = products.Products('/home/tn/products.lis')
#products.load('/home/tn/products.lis')
# Liste der Produkte die ich kaufen möchte
to_buy_products = list()


while True:
    print('-' * 30, 'Einkaufsliste', '-' * 30)
    print('[A] Produkt anlegen')
    print('[E] Produkt entfernen')
    print('[S] Produkt speichern')
    print('[Z] Produkte anzeigen')
    print('[q] Program beenden')
    action = input('Was möchten Sie machen: ')

    # Programende
    if action == 'q':
        break

    # Produkte anzeigen
    if action == 'Z':
        products.show()

    # Produkt entfernen
    if action == 'E':
        products.delete()

    if action == 'A':
        product_name = input('Wie soll das anzulegende Produkt heissen: ')
        product_price = input('Wieviel kostet das Produkt: ')
        product_size = input('Welche Einheit hat das Produkt: ')

        # erzeuge ein Produktobjekt
#        product = Product()
#        product.init(product_name, product_price, product_size)

        # fuege das Produkt der Produktliste hinzu
        result = products.create(name=product_name, price=product_price, size=product_size)
        print(result)

    # Produktliste speichern    
    if action == 'S':
        products.save()


print('Viel Spass beim einkaufen.')
exit()

