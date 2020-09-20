# def calculate_paint(efficiency_ltr_per_m2, *room_area):
#     return  sum(room_area)*efficiency_ltr_per_m2
#
# rooms = (3,4,5,5,6)
# print(calculate_paint(0.5, *rooms))

import os

def log_it(*stuff):
    filePath = r'C:\Users\ssark\OneDrive\Dokumenty\Python_scripts\log_it.txt'
    with open(filePath, 'a+') as f: 
        for i in stuff:
            content = f.write(i+' ')
        else:
            content = f.write('\n')

rooms = ('ok','git','elo','jas','adf')
log_it(*rooms)
