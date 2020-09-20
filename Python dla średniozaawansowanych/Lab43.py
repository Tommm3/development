# import math
# import time
# formulas_list = [
#      "abs(x**3 - x**0.5)",
#      "abs(math.sin(x) * x**2)"
#      ]
#
# argument_list = []
# for a in formulas_list:
#     results_list = []
#     start = time.time()
#     for i in range (1000):
#         argument_list.append(i/10)
#         x = argument_list[i]
#         # print(a.replace('x',str(x)))
#         results_list.append(eval(a))
#     else:
#         stop = time.time()
#         print(stop - start)
#         print(results_list)
#
# argument_list = []
# for a in formulas_list:
#     results_list = []
#     start = time.time()
#     for i in range (1000):
#         argument_list.append(i/10)
#         x = argument_list[i]
#         # print(a.replace('x',str(x)))
#         sourceCompiled = compile(a, 'internal variable source', 'eval')
#         results_list.append(eval(sourceCompiled))
#     else:
#         stop = time.time()
#         print(stop - start)
#         print(results_list)


import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []


for i in range (1000000):
    argument_list.append(i/10)

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))


for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()

    print("Calculation time: {}".format(stop - start))
