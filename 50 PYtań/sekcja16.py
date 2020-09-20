# Pytanie 15 - napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem ".py"
# Przetestuj nią stringi:
a = "python_moj_kod.py"
b = "python_notatki.txt"
c = "python_elosc.py"

# import re
#
# pyfileRegex = re.compile(r'python\w+\.py')
# mo = pyfileRegex.findall(a+b+c)
# print(mo)

def isPyFile(filename):
    return filename[:len('python')] == 'python' and filename[-3:] == '.py'

print(isPyFile(c))
