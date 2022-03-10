import os
import sys

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
        lines = file.readlines()
    with open(f"output-{i}.txt", "w") as f:
        for line in lines:
            for char in line:
                if char == "#":
                    line = line[:line.find("#")]
            f.write(line + "\n")
