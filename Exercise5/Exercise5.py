import random

SquareHeight = int(input("Δώσε Ύψος\n"))
SquareBase = int(input("Δώσε Βάση\n"))

# Έλεγχος διαστάσεων για να είναι τουλάχιστων 3
while SquareHeight < 3 and SquareBase < 3:
    print("Το ορθογώνιο πρέπει να έχει τουλάχιστων Ύψος = 3 και Βάση = 3")
    SquareHeight = int(input("Δώσε Ύψος\n"))
    SquareBase = int(input("Δώσε Βάση\n"))

Sum = 0
perimeter = SquareHeight * SquareBase


def val_horizontal(val_one, val_two, val_three):
    global Sum
    if val_one[val_two][val_three + 1] == "O":
        if val_one[val_two][val_three + 2] == "S":
            Sum += 1


# Έυρεση του μισού και στρογγυλοποίηση προς τα πάνω αν χρειαστεί
if perimeter % 2 == 0:
    half = int(perimeter / 2)
    half2 = half
else:
    half = int(perimeter / 2) + 1
    half2 = half - 1

for index in range(100):
    # Δημιουργία λίστας με S και O
    sos = ["S" for i in range(half)]
    for i in range(half2):
        sos.append("O")

    # Δημιουργία του πίνακα
    square = [["" for a in range(SquareBase)] for b in range(SquareHeight)]
    for vertical in range(SquareHeight):
        for horizontal in range(SquareBase):
            square[vertical][horizontal] = random.choice(sos)
            sos.remove(square[vertical][horizontal])

    for vertical in range(SquareHeight):
        for horizontal in range(SquareBase):
            if square[vertical][horizontal] == "S":

                if vertical < (SquareHeight - 2):

                    # Έυρεση τριάδων κάθετα
                    if (square[vertical + 1][horizontal] == "O") and \
                            (square[vertical + 2][horizontal] == "S"):
                        Sum += 1

                    # Έυρεση τριάδων οριζόντια
                    if (SquareBase - horizontal) > 2:
                        val_horizontal(square, vertical, horizontal)

                        # Έυρεση τριάδων διαγώνια προς τα δεξιά
                        if (square[vertical + 1][horizontal + 1] == "O") and \
                                (square[vertical + 2][horizontal + 2] == "S"):
                            Sum += 1

                    # Έυρεση τριάδων διαγώνια προς τα αριστερά
                    if horizontal > 1:
                        if (square[vertical + 1][horizontal - 1] == "O") and \
                                (square[vertical + 2][horizontal - 2] == "S"):
                            Sum += 1

                # Έυρεση τριάδων οριζόντια στις δυο τελευταίες στήλες
                elif (SquareBase - horizontal) > 2:
                    val_horizontal(square, vertical, horizontal)

Average = Sum / 100
print("Ό Μέσος όρος των sos είναι ", int(Average))
