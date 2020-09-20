import os

path = r'C:\Users\ssark\OneDrive\Dokumenty\Python_scripts'
file = r'moj_plik.txt'
filepath = os.path.join(path, file)

with open(filepath, 'w') as f:
    for x in range(1,101):
        f.write(str(x)+'\n')
    else:
        f.write(str(x))

with open(filepath, 'r') as f:
    # temp = f.read().split('\n')
    temp = f.readlines()
z_pliku = [int(x) for x in temp]

print(z_pliku)
