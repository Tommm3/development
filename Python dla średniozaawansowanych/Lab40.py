import os
files_to_process = [
    r"C:\Users\ssark\OneDrive\Dokumenty\Python_scripts\math_sin_square.py",
    r"C:\Users\ssark\OneDrive\Dokumenty\Python_scripts\math_square_root.py"
    ]

print(os.path.basename(files_to_process[0]))

with open(files_to_process[0], 'r') as f:
    source = f.read()
print(exec(source))
print(argument_list)
