# price = 123
# bonus = 23
# bonus_granted = True
#
# if bonus_granted:
#     price -= bonus
#
# print(price)
#
# price = 123
#
# print(price - bonus) if bonus_granted else print(price)

# rating = 5
#
# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')
#
# print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

import datetime
today_weekday = datetime.datetime.today().weekday()
print(today_weekday)
print('pomagam mamie') if today_weekday == 0 else print('mam pranie') if (today_weekday == 1 or today_weekday == 2) else print('mam dyżur') if today_weekday == 3 else print('mam dwa zeprania') if today_weekday == 4 else print('na lekcje ganiasz') if today_weekday == 5 else print('dziś jest dla nas!')
