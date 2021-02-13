text = ""
FinalText = ""

file = open("myfile.txt", "r", encoding="utf8")
for line in file:
    text = text + line
file.close()

for index in range(len(text)-1, -1, -1):
    FinalText = FinalText + chr(128 - ord(text[index]))

print(FinalText)
