#!/usr/bin/python3



class fahrzeug():

    name = 'auto'
    farbe = 'rot'
    farben = ['rot', 'gruen', 'blau', 'gelb', 'schwarz',' weiss']

    def vorwaerts_bewegen(self, geschwindigkeit):
        print(f'vorwaerts fahren mit {geschwindigkeit}')

    def rueckwaerts_bewegen(self, geschwindigkeit):
        print(f'rueckwaerts fahren mit {geschwindigkeit}')

    def set_farbe(self, farbe):
        self.farbe = farbe

    def get_farbe(self):
        print(f'Farbe vom Objekt: {self.farbe}')


golf = fahrzeug()
golf.set_farbe('weiss')
golf.get_farbe()

golf.vorwaerts_bewegen('90km/h')
golf.farbe = 'gruen'
print(golf.farbe)


bmw = fahrzeug()
print(bmw.farbe)

