"""
Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
"""


import inspect


def deco_doc(new_docstring):
    def deco(cls):
        for func in filter(inspect.isfunction, vars(cls).values()):
            if func.__name__.startswith('__'):
                continue
            else:
                func.__doc__ = new_docstring
        return cls
    return deco


