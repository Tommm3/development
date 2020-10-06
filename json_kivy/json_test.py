	# -*- coding: utf-8 -*-
from kivy.storage.jsonstore import JsonStore
# import pandas as pd
# import sys



def get_init_exercise_tuple(wd):
    store = JsonStore('silka5.json')
    store_weights = JsonStore('weights.json')
    listOfTuples = []
    if wd==0:
        exRange = store.keys()[:8]
        exRange2 = store.keys()[:8]
    elif wd==1:
        exRange = store.keys()[8:17]
        exRange2 = store.keys()[8:17]
    elif wd==3:
        exRange = store.keys()[17:25]
        exRange2 = store.keys()[17:25]
    elif wd==4:
        exRange = store.keys()[25:30]
        exRange2 = store.keys()[25:30]
    else:
        return ""
        exit()
    counter=1
    for k,j in exRange,exRange2:
        dict_json = store.get(k)
        list_json=[counter]
        counter+=1
        for i in dict_json.items():
            list_json.append(i[1])

        listOfTuples.append(tuple(list_json))
    return listOfTuples

print(get_init_exercise_tuple(1))
