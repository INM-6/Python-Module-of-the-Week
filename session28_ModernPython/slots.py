class SomeClass(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


a = SomeClass(name='Moritz', identifier=25255)
try:
    a.PunkBandMembership = True
except AttributeError as e:
    print(e)
