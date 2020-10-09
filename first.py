from datetime import datetime, timedelta
# from tomaszSkrzypkowski import greatIdeas, skill

data = datetime.now()
data -= timedelta(days=1)

print(data.weekday())
