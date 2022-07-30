s = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
b = {}
for i in s:
    print(s[i])
    b[s[i]] = i
s = b
print(s)
