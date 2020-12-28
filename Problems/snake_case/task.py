text = input()
text_ = list(text)
output = ""
for i in range(len(text_)):
    if text_[i].islower():
        output += text_[i]
    elif text_[i].isupper():
        text_[i] = text_[i].lower()
        output += "_" + text_[i]

print(output)
