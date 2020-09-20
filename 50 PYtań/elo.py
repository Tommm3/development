A = [1,2,3,3,2,1,2,3]
B = []

for i in A:
    if i not in B:
        B.append(i)
print(B)

B = list(set(A))
print(B)

# Sprawdź i wypisz ile unikatowych elementów znajduje się w liście A.

C = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]
D = []

D = list(set(C))
print(len(D))
