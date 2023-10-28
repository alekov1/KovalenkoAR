sentence = str(input())
lensen = len(sentence) // 2
sentence1 = sentence[:lensen]
sentence2 = sentence[lensen:]
sentence1 = sentence1.replace('п','*')
print(sentence1+sentence2)
