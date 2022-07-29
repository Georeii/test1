l = [1, 2, 3, 1, 5, "123123", "3", '3']
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
