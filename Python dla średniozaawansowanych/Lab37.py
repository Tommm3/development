import math
while True:
    print('Type a calculation')
    calc = str(input())
    for x in range(0,11):
        try:
            print('%.1f' % float(eval(calc.replace('x', str(x)))))
            # eval(calc)
            # print()
        except:
            print('Syntax error')
            break
