# put your python code here
num = int(input())
digits = [int(x) for x in str(num)]
digits_sum = 0
for x in digits:
    digits_sum += x
print(digits_sum)
