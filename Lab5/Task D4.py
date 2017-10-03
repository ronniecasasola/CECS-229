dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
count = 0;
for i in dlist: #check for keys
    for j in i:
        if (k == j):
            print(i[j]) # print if found
            count = count + 1;
if(count == 0): # count doesn't change if no key in dictionary
    print("NOT PRESENT")

dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Frodo'
count = 0;
for i in dlist:
    for j in i:
        if (k == j):
            print(i[j])
            count = count + 1;
        if(count == 0):
            print("NOT PRESENT")