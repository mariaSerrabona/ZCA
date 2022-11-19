from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implementer
from zope.interface import implements


class IPerro(Interface):
    nombre = Attribute("""Nombre del perro""")
    def ladrar(filename):
        """Método que permite hacerlo ladrar"""

@implementer(IPerro)
class Perro(object):
    nombre = u''
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        """Método que permite hacerlo ladrar"""
        print('Guau')


class IGato(Interface):
    nombre = Attribute("""Nombre del gato""")
    def maullar(filename):
        """Método que permite hacerlo maullar"""

@implementer(IGato)
class Gato(object):
    nombre = u''
    def __init__(self, nombre):
        self.nombre = nombre
    def maullar(self):
        """Método que permite hacerlo maullar"""
        print('Miau')
