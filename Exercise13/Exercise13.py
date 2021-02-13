import re

# Δημιουργία λίστας με τις λέξεις του αρχείου
words = []
file = open("MyFile.txt", "r", encoding="utf8")
for a in file:
    line = re.findall(r"\w+", str(a))
    for b in line:
        words.append(b)
file.close()

WordsCouples = []
n = len(words)
index = 0
start = 1

while index < n:
    found = False
    n = len(words)
    i = start

    # Αναζήτηση για το ζευγάρι
    while (i != n) and not found:
        if len(words[index]) + len(words[i]) == 20:
            WordsCouples.append([words[index], words[i]])
            words.pop(i)
            words.pop(index)
            found = True
        i += 1

    # Αν δε βρέθηκε το ζευγάρι για την λέξη τότε πάμε στην επόμενη
    if not found:
        start += 1
        index += 1

for a in WordsCouples:
    print(a)
