days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()

workdays.remove("sun")
workdays.remove("sat")

print(days,workdays)
