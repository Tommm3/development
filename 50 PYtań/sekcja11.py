# Pytanie 9 - dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu

# x = "myszydokazujągdykotanieczują"
#
# D = {}                   # tworzenie pustego słownika
# for litera in x:         # dla kolejnej litery w stringu x
#     if litera not in D:  # jeśli litera nie znajduje się w słowniku D
#         D[litera] = 1    # stwórz nowy klucz 'litera' w D i przypisz mu wartość 1
#     else:                # w przeciwnym wypadku (klucz już istnieje)
#         D[litera] += 1   # zwiększ wartość pod kluczem o 1 (D[litera] += 1 to zapis równoważny do D[litera] = D[litera] + 1)
# print(D)                 # wydrukuj słownik D
#
# is4times = False
#
# for d in D:
#     if D[d] == 3:
#         is4times = True
#
# print(is4times)
#
# print(4 in list(D.values()))

pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}

print(sum(pensje.values()))
