from zope.interface import Interface
from zope.interface import implementer

class IidGenerator(Interface):
    def get(self):
        """Provee un id único"""
    def getIdFor(self, category):
        """Provee un id único para cada categoría"""
    def getIdFores(self, category, name):
        """Provee un id único para cada categoría y nombre"""

@implementer(IidGenerator)
class IdGenerator(object):
    def __init__(self):
        self.id = 0
        self.ids = {}
        self.ids['default']=0

    def get(self):
        """Provee un id único"""
        self.id += 1
        return self.id

    def getIdFor(self, category):
        """Provee un id único para cada categoría"""
        if category not in self.ids.keys():
            self.ids[category] = 0
        self.ids[category] += 1
        return self.ids[category]

    def getIdFores(self, category, name):
        """Provee un id único para cada categoría"""
        if category not in self.ids.keys():
            self.ids[category] = {}

        if category not in self.ids.keys():
            self.ids[category] [name]= 0
        self.ids[category] [name] += 1
        return self.ids[category]

id_generator = IdGenerator()
print(id_generator.get())
id_generator.getIdFor('default')
print(id_generator.getIdFor('default'))
id_generator.getIdFor('default')
#id_generator.getIdFores('default', 'Pablo')
#id_generator.getIdFores('default', 'María')
