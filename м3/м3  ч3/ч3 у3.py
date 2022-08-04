list2 = [900, 100,]


def max_number(list):
    list_2 = [0]
    num_sum = ""
    for i in list:
        num = i
        if num // 10 == 0:
            num1 = (num % 10)
        else:
            num1 = (num // 10)
        s = 0
        for j in range(len(list_2)):
            if list_2[s] // 10 == 0:
                num2 = (list_2[s] % 10)
            else:
                num2 = (list_2[s] // 10)

            if num1 > num2:
                list_2.insert(s,num)
            else:
                s += 1
    list_2.pop()
    for i in list_2:
        num_str = str(i)
        num_sum = num_sum + num_str
    print(num_sum)


max_number(list2)
