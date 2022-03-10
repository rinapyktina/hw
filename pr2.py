with open("text.txt", "r") as file:
    text = file.read().split()
    maxiword = ""
    count = 0

    for word in text:
        if len(word) > len(maxiword):
            maxiword = word

    for word in text:
        if word == maxiword:
            count += 1

    print(maxiword, count)
