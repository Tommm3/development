
from kivy.storage.jsonstore import JsonStore
import pandas as pd

store = JsonStore('silka_final.json')
df = pd.read_excel('silka.xlsx')
df = df.to_records()
print(df)
counter = 0

for i in df:
    head = 'Exercise'+ str(counter)
    store.put(head, name=i[1], sets=i[2], repeats=i[3], weights=[i[4],i[5]])
    counter+=1
