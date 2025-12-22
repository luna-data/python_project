names = ["철수", "영희", "민수", "지영"]
scores = [90, 75, 60, 88]

score_dict = {}

for i in range(len(names)):
    name = names[i]
    score = scores[i]
    score_dict[name] = score

for name in score_dict:
    if score_dict[name] >= 80:
        print(name, score_dict[name])
