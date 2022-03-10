import os
import sys

if (len(sys.argv) > 1):
    file = sys.argv[1]
    if (not os.path.isfile(file)):
        print("Несуществующий файл")
        sys.exit()

else:
    print("Отсутствуют аргументы!")
    sys.exit()

with open(file, "r") as file:
    for i in range(10):
        string = file.readline()
        if string == "":
            continue
        print(string)
