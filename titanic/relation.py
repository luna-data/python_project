# 1️⃣ 라이브러리 불러오기
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 2️⃣ 데이터 로드
titanic = sns.load_dataset("titanic")

# 데이터 기본 확인
titanic[['survived', 'sex', 'pclass']].head()

# 3️⃣ 객실 등급별 생존률
pclass_survival = titanic.groupby('pclass')['survived'].mean()
pclass_survival

# 시각화: 객실 등급별 생존률
plt.figure(figsize=(6,4))
sns.barplot(x=pclass_survival.index, y=pclass_survival.values)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.ylim(0,1)
plt.show()

# 4️⃣ 성별 생존률
sex_survival = titanic.groupby('sex')['survived'].mean()
sex_survival

# 5️⃣ 성별 × 객실 등급 생존률 (상호작용)
interaction = titanic.groupby(['sex', 'pclass'])['survived'].mean().unstack()
interaction

# 🔥 핵심 시각화: 히트맵
plt.figure(figsize=(7,4))
sns.heatmap(interaction, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Survival Rate by Sex and Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Sex")
plt.show()
