import sys
import os

if __name__ == "__main__":
    files = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            file = sys.argv[i]
            if os.path.isfile(file):
                files.append(file)
                continue
            print(f"File {file} doesn't exist")
    else:
        print("Not enough arguments!")
        sys.exit()
    funcs = []
    for i in files:
        with open(i, "r", encoding="utf-8") as f:
            a = f.readlines()
        for j in range(len(a)):
            if a[j].startswith("def "):
                if not a[j - 1].startswith("#"):
                    funcs.append(f"file name: {i}, line: {j} function name: {a[j][4:]}")

    for i in funcs:
        print(i)
