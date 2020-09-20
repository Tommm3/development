# Pytanie 19 - wyjasnij jak działa poniższa funkcja.
# Wyjaśnij skąd wzięły się wyniki zwrócone przez poszczególne wywołania funkcji.

def dodaj_do_listy(n, lista=[]):  # lista=[] - argument domyślny funkcji
    lista.append(n)               # dodaj n do końca listy lista
    print(lista)

dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
dodaj_do_listy(3)
