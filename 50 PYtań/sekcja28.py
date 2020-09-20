
# Pytanie 27
# Objętość graniastosłupa oblicza się na podstawie wzoru: V = a * b * h
# a i b to długości boków jego podstawy, a h to wysokość.
# Poniższy kod znajduje największy graniastosłup jaki możemy utworzyć
# z elementów list A, B i H.
# Ile operacji zostane wykonane w wyniku uruchomienia tego kodu?
# W jaki sposób można by to zadanie rozwiązać bardziej efektywnie?

import random                                     # biblioteka random służy do generowania liczb losowych

A = [random.randint(0,100) for i in range(5)]     # tworzenie pięcioelementowej listy losowych integerów z zakresu od 0 do 100
B = [random.randint(0,100) for i in range(5)]
H = [random.randint(0,100) for i in range(5)]

max_v = max(A) * max(B) * max(H)

print(max_v)
