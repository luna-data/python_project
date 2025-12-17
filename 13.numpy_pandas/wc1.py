import matplotlib.pyplot as plt
from wordcloud import WordCloud

text=""
with open("13.numpy_pandas/mobydick.txt", "r", encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        text+=line

wc=WordCloud(width=600,height=400)
wc.generate(text)
wc.to_file("wc.png")
plt.figure(figsize=(30,10))
plt.imshow(wc)
plt.show()