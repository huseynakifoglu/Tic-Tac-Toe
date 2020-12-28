floats = []
while True:
    a = input()
    if a != ".":
        floats.append(float(a))
    if a == ".":
        break
# print(floats)


print(str(min(floats)))
