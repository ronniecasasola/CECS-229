id2salary = {0: 1000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', '', 'Moe']

name2salary = {names[i]: id2salary[i] for i in range(0, len(names)) if i in id2salary}
print(name2salary)