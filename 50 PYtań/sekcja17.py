# Pytanie 16 - wypisz podaną listę imion przed każdym dodając kolejny numer.
# Zacznij numerowanie od 1.

imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

print(list(enumerate(imiona)))

for a, b in list(enumerate(imiona,1)):
    print('%2d - %12s' % (a,b))

for num in range(1,len(imiona)+1):
    print('%2d - %12s' % (num,imiona[num-1]))
