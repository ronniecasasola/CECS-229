drinks = ["wine", "water", "beer", "vodka"]

food = ["ice cream", "pizza", "banana"]

combo = []

for i in food:
    for j in drinks:
        combo.append((i, j))

print(combo)