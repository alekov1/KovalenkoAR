sentence = str(input()).replace('!','.').split(' ')

count = 0
countmax = 0
for word in sentence:
    for letter in word:
        if letter == 'н':
            count += 1
            countmax = max(countmax, count)

print(countmax, sentence)