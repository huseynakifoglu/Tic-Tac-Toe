text = input()
print("_".join([x for x in text.split() if x.endswith('s')]))
