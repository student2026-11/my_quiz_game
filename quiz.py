import json
import os

class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.best_score = self.load_best_score() # 시작할 때 최고 점수 불러오기

    def add_quiz(self, quiz):
        self.quizzes.append(quiz) # 오타 수정: self.quizzes.append(quiz)

    # 최고 점수를 파일(score.json)에서 읽어오는 함수
    def load_best_score(self):
        if os.path.exists("score.json"):
            with open("score.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("best_score", 0)
        return 0

    # 최고 점수를 파일에 저장하는 함수
    def save_best_score(self, score):
        with open("score.json", "w", encoding="utf-8") as f:
            json.dump({"best_score": score}, f)

    def start(self):
        self.score = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("-" * 35)

        for i, quiz in enumerate(self.quizzes):
            print(f"\n[문제 {i+1}]")
            print(quiz.question)
            for j, option in enumerate(quiz.options):
                print(f"{j+1}. {option}")
            
            try:
                user_input = int(input("\n정답 입력: "))
                if user_input == quiz.answer:
                    print("✅ 정답입니다!")
                    self.score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")
            except ValueError:
                print("⚠️ 숫자만 입력해주세요!")

        self.show_result()

    def show_result(self):
        total = len(self.quizzes)
        percent = int((self.score / total) * 100)
        
        print("\n" + "="*40)
        print(f"🏆 결과: {total}문제 중 {self.score}문제 정답! ({percent}점)")
        
        # 최고 점수 비교 및 갱신
        if self.score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.save_best_score(self.score)
        else:
            print(f"현재 최고 기록: {self.best_score}문제 정답")
        print("="*40)