filename = "data.txt"

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

text = text.lower()

for ch in [".", ","]:
    text = text.replace(ch, "")

words = text.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

items = list(freq.items())

def sort_key(item):
    word = item[0]
    count = item[1]
    return -count  # 빈도 높은 순

items_sorted = sorted(items, key=sort_key)

top5 = items_sorted[:5]
for word, count in top5:
    print(word, count)
