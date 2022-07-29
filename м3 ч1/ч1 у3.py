num = int(input())
num_sum = (num % 10) + (num % 100 // 10) + (num % 1000 //100) + (num % 10000 //1000)
print(num_sum)