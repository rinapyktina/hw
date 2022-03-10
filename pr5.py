import os
import sys
import string

alphab = string.ascii_lowercase
files = []
if(len(sys.argv) > 1):
    for i in range(1, len(sys.argv)):
        file = sys.argv[i]
        if(os.path.isfile(file)):
            files.append(file)
            continue
        print(f"Файла {file} не существует")
else:
    print("Отсутствуют аргументы!")
    sys.exit()

for i in files:
    with open(i, "r") as file:
        file = file.read()
    with open(f"output-{i}.txt", "w") as f:
        for letter in alphab:
            count = 0
            for char in file:
                    if letter == char.lower():
                    	count += 1;
            print(letter, ": ", count / len(file) * 100, "%")
