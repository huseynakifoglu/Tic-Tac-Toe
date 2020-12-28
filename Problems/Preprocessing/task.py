text = input()
punctuations = [",", ".", "?", "!"]

for character in punctuations:
    text = text.replace(character, "").lower()
print(text)
