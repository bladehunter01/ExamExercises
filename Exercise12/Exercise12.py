text = ""
myfile = open("myfile.txt", "r", encoding="utf8")

for line in myfile:
    for character in range(len(line)):
        text = (chr(128 - ord(line[character]))) + text

print(text)
