with open("text.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if "," in line:
            print(line)
            continue
