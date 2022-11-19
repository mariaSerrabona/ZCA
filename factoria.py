from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implementer
from zope.component.factory import Factory


class IFactory(Interface):
    def __call__():
        #'método que permite cerar un objeto'
        pass

# @implementer(IFactory)
# class Factory(object):
#     def __init__(self, clase):
#         self.clase=clase
#     def __call__(self):
#         return self.clase()

@implementer(IFactory)
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

factory = Factory(Perro, 'Perro')
perro=factory('manolo')
print(perro.nombre)
perro.ladrar()