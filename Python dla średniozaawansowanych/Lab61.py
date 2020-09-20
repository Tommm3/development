import datetime

def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

def function_get_sequence_wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args,**kwargs)
        stop = datetime.datetime.now()
        print(stop - start)
        return result
    return func_with_wrapper

get_sequence_with_time = function_get_sequence_wrapper(get_sequence)

print(get_sequence_with_time(18))
