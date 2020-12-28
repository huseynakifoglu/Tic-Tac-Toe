# put your python code here
numbers = input().split()
digit = input()
index = []
for i, value in enumerate(numbers):
    if value == digit:
        index.append(i)
        # print(" ".join([str(elem) for elem in index]))
if not index:
    print("not found")
else:
    print(" ".join([str(elem) for elem in index]))



