"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
"""
from functools import wraps


def require_typing(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        annotations = list(fn.__annotations__.keys())
        vars = list(fn.__code__.co_varnames)
        vars.append('return')
        if vars == annotations:
            return fn(*args,**kwargs)
        else:
            return f'Add typing to function {fn.__name__}, please!'
    return wrapper


