
from kivy.storage.jsonstore import JsonStore
import pandas as pd
import sys

store = JsonStore('silka_final2.json')
tablica = store.get('Exercise4')
print(tablica)
tabs = tablica['weights']
tabs.append("48")
print(tabs)
store.put('Exercise4', name=tablica['name'], sets=tablica['sets'], repeats=tablica['repeats'], weights=tabs)



# store = JsonStore('weights.json')
# git = store.get('ExerciseWeights26')
# print(git[list(git)[-1]])
