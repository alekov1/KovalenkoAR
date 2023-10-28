sentence = str(input()).split(' ')
count = 0
for letter in sentence:
    if letter[0] == 'е' or letter[0] == 'Е':
        count += 1
print(count)