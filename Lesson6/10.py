sentence = str(input()).split(' ')
sentence_next = ''
for letter in sentence:
    letter123 = letter[0].upper() + letter[1:]
    sentence_next += letter123 + ' '
print(sentence_next[:-1])