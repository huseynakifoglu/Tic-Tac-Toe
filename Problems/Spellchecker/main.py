dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words_of_sentence = input().split()

wrong_spelled = []
# print(words)

for x in words_of_sentence:
    if x not in dictionary:
        wrong_spelled.append(x)

if len(wrong_spelled) == 0:
    print("OK")
else:
    print("\n".join(wrong_spelled))
