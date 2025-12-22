words = ["data", "science", "is", "fun"]

sentence = ""
for i in range(len(words)):
    if i == 0:
        sentence += words[i]
    else:
        sentence += " " + words[i]

print(sentence)
