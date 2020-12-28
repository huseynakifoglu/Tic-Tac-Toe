characters = list(input())
# print(characters)
vowels = ['a', 'e', 'i', 'o', 'u']
count=0
while count <len(characters):
    for char in characters:
        if char in vowels and char.isalpha():
            print("vowel")
        elif char not in vowels and char.isalpha():
            print("consonant")
        elif not char.isalpha():
            break
    break

