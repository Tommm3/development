from datetime import datetime

start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

def createFunction(span):

    if span == 'm':
        sec = 60
    elif span == 'h':
        sec == 3600
    elif span == 'd':
        sec == 1440*60

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)
    exec(source, globals())
    return f

fasdf = createFunction('h')
print(fasdf(start,end))

# from datetime import datetime
#
#
# start = datetime(2019, 1, 1, 0, 0, 0)
# end  = datetime.now()
#
# def create_function(span):
#
#     if span == 'm':
#         sec = 60
#     elif span == 'h':
#         sec = 3600
#     elif span =='d':
#         sec = 86400
#
#     source = '''
# def f(start, end):
#     duration = end - start
#     duration_in_s = duration.total_seconds()
#     return divmod(duration_in_s, {})[0]
# '''.format(sec)
#
#     exec(source, globals())
#
#     return f
#
# f_hours = create_function('h')
#
# print(f_hours(start, end))
