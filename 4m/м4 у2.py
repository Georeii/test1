from random import randint
numbers = []
for q in range(50):
    numbers.append(randint(0, 50))


def insertion_sort1(a):
    a1 = [1e500]
    for i in a:
        s = 0
        for j in a1:
            if i < j:
                a1.insert(s, i)
                break
            else:
                s += 1
    del a1[a1.index(1e500)]
    return a1


print(insertion_sort1(numbers))
