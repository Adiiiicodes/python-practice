x = input('Enter a sentence: ')
words = x.split()
dups = []

for word in words:
    rword = ''
    for char in word:
        rword = char + rword
    dups.append(rword)

reversed_sentence = ''
for word in dups:
    reversed_sentence += word + ' '

print(reversed_sentence.strip())
