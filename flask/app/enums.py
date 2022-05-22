import enum

# class Roles(enum.Enum):
#     admin = 'admin'
#     institucion = 'institucion'
#     viajero = 'viajero'


class Roles(enum.Enum):
    presidente = 'Presidente'
    vicepresidente = 'Vicepresidente'
    otros = 'Otros'

    # @classmethod
    # def choices(cls):
    #     return [(choice.name, choice.value) for choice in cls]
