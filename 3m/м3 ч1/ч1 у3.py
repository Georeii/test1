num = int(input())
num_sum = (num % 10)
num1 = 10
num2 = 100
for i in range(20):
    num_sum = (num % num2 // num1) + num_sum
    num1 *= 10
    num2 *= 10
print(num_sum)
