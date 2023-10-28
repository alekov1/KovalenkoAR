sentence = str(input()).split(' ')

for word in sentence:
    if word[-1:] == 'я':
        print(word)
