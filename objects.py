#!/usr/bin/python3



class fahrzeug():

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

bmw = fahrzeug()
bmw.set_farbe('rot')
bmw.get_farbe()


golf.get_farbe()


