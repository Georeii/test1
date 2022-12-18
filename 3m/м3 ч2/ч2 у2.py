from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
max = 0
for i in range(n):
    for j in m[i]:
        if max < j:
            max = j

print(max)
print(m)
