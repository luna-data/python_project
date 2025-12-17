import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def get_sns_posts():
    posts=[
        "Today is a happy day!",
        "Had delicious food",
        "Planning summer vacation",
        "Too hot and dizzy",
        "Studying hard during wxam period:,"
        "The recently released movie is so much fun",
        "Our dog is really cute",
        "Watched a soccer game",
        "The fashion style that is trending these days is impressive",
        "It's a difficult time with COVID-19, but let's stay strong!"
    ]
    df=pd.DataFrame(posts,columns=['post'])
    return df
def create_wordcloud(text_data):
    stopwords_set=set(stopwords.words('english'))
    wordcloud=WordCloud(
        background_color='white',
        width=800,
        height=600
    ).generate(text_data)

    plt.figure(figsize=(10,6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis=("off")
    plt.tight_layout()
    plt.show()

sns_posts_df=get_sns_posts()

all_posts_text=" ".join(sns_posts_df['post'])

create_wordcloud(all_posts_text)
