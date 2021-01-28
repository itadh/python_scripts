#!/usr/bin/python3

import os
import lib.Product as Product
import lib.Products


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
products = Products()
products.load('/home/tn/products.lis')
# Liste der Produkte die ich kaufen möchte
to_buy_products = list()


while True:
    print('-' * 30, 'Einkaufsliste', '-' * 30)
###
    print('[A] Produkt anlegen')
    print('[E] Produkt entfernen')
    print('[S] Produkt speichern')
    print('[L] Produkte laden')
###
    print('[q] Program beenden')
    action = input('Was möchten Sie machen: ')

    # Programende
    if action == 'q':
        break

    if action == 'A':
        product_name = input('Wie soll das anzulegende Produkt heissen: ')
        product_price = input('Wieviel kostet das Produkt: ')
        product_size = input('Welche Einheit hat das Produkt: ')

        # erzeuge ein Produktobjekt
        product = Product()
        product.init(product_name, product_price, product_size)

        # fuege das Produkt der Produktliste hinzu
        products.create(product)
        products.save('/home/tn/products.lis')


print('Viel Spass beim einkaufen.')
exit()

