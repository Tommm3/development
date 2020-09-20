import os
def howManyWords(path):
    with open(filepath, 'r') as f:
        content = f.read()
        wordCount = len(content.split())
    return wordCount

filepath = r'C:\Users\ssark\OneDrive\Dokumenty\Python_scripts\pogoda.txt'
if os.path.isfile(filepath):
    print(howManyWords(filepath))

os.path.isfile(filepath) and print("There are {} words in the file {}".format(howManyWords(filepath), filepath))
