# put your python code here
first_num = float(input())
second_num = float(input())
operator = input()
if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "pow":
    print(first_num ** second_num)

if second_num != 0:
    if operator == "/":
        print(first_num / second_num)
    elif operator == "mod":
        print(first_num % second_num)
    elif operator == "div":
       print(first_num // second_num)
else:
    print("Division by 0!")
