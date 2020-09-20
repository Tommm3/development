projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for project, leader in zip(projects, leaders):
    print('The leader of %s is %s' % (project, leader))
for project, date, leader in zip(projects, dates, leaders):
    print('The leader of %s started %s is %s' % (project, date, leader))
for number, (project, date, leader) in enumerate(zip(projects, dates, leaders)):
    print('%d - The leader of %s started %s is %s' % (number+1, project, date, leader))
    print('{} - The leader of "{}" started {} is {}'.format(number+1,project,date,leader))
