s = [1, 2, 3, 4, 5, 6, 7, 8, 10]


def binary_search(isk_num, s_2):
    xentr_num = 0
    while isk_num != xentr_num:
        if len(s_2) / 2 >= len(s_2) // 2:
            xentr_num = s_2[len(s_2) // 2]
            if xentr_num == isk_num:
                return xentr_num
                break
            elif xentr_num < isk_num:
                del s_2[0:len(s_2) // 2 + 1]
                print(s_2)
            elif xentr_num > isk_num:
                del s_2[len(s_2) // 2:len(s_2)]
                print(s_2)


print(binary_search(1, s))