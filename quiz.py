class Quiz:
    def __init__(self, question, options, answer):
        self.question = question  # 질문
        self.options = options    # 보기 (리스트)
        self.answer = answer      # 정답 번호 (1, 2, 3...)

    def is_correct(self, user_answer):
        # 사용자가 입력한 번호가 정답과 일치하는지 확인
        return str(self.answer) == user_answer

class QuizGame:
    def __init__(self):
        self.quizzes = []  # 퀴즈들을 담을 바구니
        self.score = 0     # 점수

    def add_quiz(self, quiz):
        # 퀴즈 객체를 리스트에 추가
        self.quizzes.append(quiz)

    def start(self):
        print("=== 퀴즈 게임을 시작합니다! ===")
        for i, quiz in enumerate(self.quizzes):
            print(f"\n문제 {i+1}. {quiz.question}")
            for idx, option in enumerate(quiz.options):
                print(f"{idx+1}) {option}")
            
            user_input = input("정답 번호를 입력하세요: ")
            
            if quiz.is_correct(user_input):
                print("정답입니다! ✨")
                self.score += 1
            else:
                print(f"틀렸습니다. 정답은 {quiz.answer}번입니다. 😢")
        
        print(f"\n=== 게임 종료! 총점: {self.score}/{len(self.quizzes)} ===")