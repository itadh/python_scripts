#!/usr/bin/python3

import os
import lib.Products as products
import lib.Cart as cart


os.system('clear')

# Liste aller kaufbaren Produkte
products = products.Products('/home/tn/products.lis')
# Liste der Produkte die ich kaufen möchte
cart = cart.Cart('/home/tn/cart.lis')


while True:
    print('-' * 30, 'Einkaufsliste', '-' * 30)
    print('[A] Produkt anlegen')
    print('[E] Produkt entfernen')
    print('[S] Produkt speichern')
    print('[Z] Produkte anzeigen')
    print('[a] Einkaufsliste: Produkt hinzufuegen')
    print('[e] Einkaufsliste: Produkt entfernen')
    print('[s] Einkaufsliste speichern')
    print('[z] Einkaufsliste anzeigen')
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

    # Einkaufsliste: Produkt hinzufuegen
    if action == 'a':
        counter = 0
        for product in products.lists():
            print(f'{counter}: {product["name"]}')
            counter += 1
        product_name = input('Welches Produkt möchten Sie in den Warenkorb legen: ')
        product_amount = input('Wieviele Produkte möchten Sie in den Warenkorb legen: ')
        cart.create(product_name, product_amount)
 
    # Einkaufsliste: Produkt entfernen
    if action == 'e':
        cart.delete()

    # Einkaufsliste speichern
    if action == 's':
        cart.save()

    # Einkaufsliste anzeigen
    if action == 'z':
        cart.show()

print('Viel Spass beim einkaufen.')
exit()

