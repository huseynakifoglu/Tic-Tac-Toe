text = input()
words = text.lower().split()
for word in words:
    # finish the code here
    if word.startswith("https://") or word.lower().startswith("http://") or word.lower().startswith("www."):
        print(word)