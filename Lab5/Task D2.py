def add(list1, list2):
    I = []
    length = len(list1)
    for i in range (length):
        value = list1[i] + list2[i]
        I.append(value)
        return I


list1 = [10,25,40]
list2 = [1,15,20]

I = add(list1, list2)

print (I)