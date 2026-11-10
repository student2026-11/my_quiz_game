class Quiz:
    def __init__(self, question, choices, answer):
        """
        - question: 문제 내용
        - choices: 보기 리스트 (4개)
        - answer: 정답 번호 (1~4 정수)
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_quiz(self, index):
        """이미지 예시처럼 [문제 1] 형식으로 출력합니다."""
        print(f"\n--------------------------------")
        print(f"[문제 {index}]")
        print(f"{self.question}\n")
        
        # 보기 출력 (1. 보기1  2. 보기2...)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
        print()

    def is_correct(self, user_choice):
        """정답 여부를 확인합니다."""
        return user_choice == self.answer