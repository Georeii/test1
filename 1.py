num_1 = int(input("ведите первое число"))
num_2 = int(input("ведите второе число"))
num_3 = int(input("ведите третья число"))
if num_1 == num_2 and num_1 == num_3:
    print('одинаковых чисел 3')

elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print('одинаковых чисел 2')

elif num_1 != num_2 or num_1 != num_3:
    print('одинаковых чисел 0')
