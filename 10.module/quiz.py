import random
def quiz_game():
    questions={
        "프랑스의 수도는?": "파리",
        "독일의 수도는?": "베를린",
        "이탈리아의 수도는?": "로마",
        "스페인의 수도는?": "마드리드",
        "영국의 수도는?": "런던"
    }
    question=random.choice(list(questions.keys()))
    correct_answer=questions[question]
    print("다음 문제에 대한 답을 입력하세요:")
    print(question)
    user_answer=input("답: ")
    if user_answer.strip() == correct_answer.lower():
        print("정답입니다!")        
    else:
        print(f"오답입니다. 정답은 {correct_answer}입니다.")

quiz_game()