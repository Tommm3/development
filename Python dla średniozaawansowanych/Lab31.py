ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

tuplet = [(a,b) for a in ports for b in ports if a<b]

print(tuplet)
print(len(tuplet))

generator = ((a,b) for a in ports for b in ports if a<b)

i = 0

while True:
    try:
        next(generator)
        i+=1
    except:
        print(i)
        break
