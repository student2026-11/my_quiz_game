import json
import os


class Question:
    """개별 퀴즈 문제 하나를 표현하는 클래스"""

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        """입력받은 번호(1부터 시작)가 정답인지 확인합니다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리 형태로 변환합니다."""
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리 데이터로부터 Question 객체를 생성합니다."""
        return cls(
            question=data["question"],
            options=data["options"],
            answer=data["answer"],
        )


class QuizManager:
    def __init__(self):
        self.filename = "state.json"
        self.default_data = {
            "quizzes": [
                {"question": "우리나라의 전통 고유 의상은 무엇일까요?", "options": ["치파오", "기모노", "한복", "사리"], "answer": 3},
                {"question": "대한민국의 수도는?", "options": ["부산", "인천", "서울", "대구"], "answer": 3},
                {"question": "가장 큰 행성은?", "options": ["지구", "화성", "목성", "토성"], "answer": 3},
                {"question": "지구에서 가장 가까운 행성은?", "options": ["태양", "화성", "목성", "금성"], "answer": 4},
                {"question": "빨간색과 파란색 물감을 섞으면 무슨색이 될까요?", "options": ["초록색", "노란색", "회색", "보라색"], "answer": 4},
            ],
            "best_score": 0,
        }
        state = self.load_state()
        self.quizzes = [Question.from_dict(q) for q in state.get("quizzes", [])]
        self.best_score = state.get("best_score", 0)

    def load_state(self):
        """파일에서 데이터를 읽어옵니다. 파일이 없으면 기본 데이터를 반환합니다."""
        try:
            if not os.path.exists(self.filename):
                return self.default_data
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return self.default_data

    def save_state(self):
        """현재 데이터를 state.json 파일에 저장합니다."""
        payload = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"❌ 파일 저장 오류: {e}")

    def add_quiz(self, question, options, answer):
        """새로운 Question 객체를 추가하고 저장합니다."""
        new_question = Question(question, options, answer)
        self.quizzes.append(new_question)
        self.save_state()

    def get_quizzes(self):
        """Question 객체 목록을 가져옵니다."""
        return self.quizzes

    def update_best_score(self, score):
        """최고 점수를 갱신합니다."""
        if score > self.best_score:
            self.best_score = score
            self.save_state()
            return True
        return False

    def get_best_score(self):
        """최고 점수를 가져옵니다."""
        return self.best_score


# import json
# import os

# class QuizManager:
#     def __init__(self):
#         self.filename = "state.json"
#         # 기본 데이터 설정
#         self.default_data = {
#             "quizzes": [
#                 {"question": "우리나라의 전통 고유 의상은 무엇일까요?", "options": ["치파오", "기모노", "한복", "사리"], "answer": 3},
#                 {"question": "대한민국의 수도는?", "options": ["부산", "인천", "서울", "대구"], "answer": 3},
#                 {"question": "가장 큰 행성은?", "options": ["지구", "화성", "목성", "토성"], "answer": 3}, 
#                 {"question": "지구에서 가장 가까운 행성은?", "options": ["태양", "화성", "목성", "금성"], "answer": 4},
#                 {"question": "빨간색과 파란색 물감을 섞으면 무슨색이 될까요?", "options": ["초록색", "노란색", "회색", "보라색"], "answer": 4}               

#             ],
#             "best_score": 0
#         }
#         self.data = self.load_state()

#     def load_state(self):
#         """파일에서 데이터를 읽어옵니다. 파일이 없으면 기본 데이터를 반환합니다."""
#         try:
#             if not os.path.exists(self.filename):
#                 return self.default_data
#             with open(self.filename, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         except (json.JSONDecodeError, IOError):
#             return self.default_data

#     def save_state(self):
#         """현재 데이터를 state.json 파일에 저장합니다."""
#         try:
#             with open(self.filename, "w", encoding="utf-8") as f:
#                 json.dump(self.data, f, ensure_ascii=False, indent=4)
#         except IOError as e:
#             print(f"❌ 파일 저장 오류: {e}")

#     def add_quiz(self, question, options, answer):
#         """새로운 퀴즈를 추가합니다."""
#         self.data["quizzes"].append({"question": question, "options": options, "answer": answer})
#         self.save_state()

#     def get_quizzes(self):
#         """퀴즈 목록을 가져옵니다."""
#         return self.data["quizzes"]

#     def update_best_score(self, score):
#         """최고 점수를 갱신합니다."""
#         if score > self.data["best_score"]:
#             self.data["best_score"] = score
#             self.save_state()
#             return True
#         return False

#     def get_best_score(self):
#         """최고 점수를 가져옵니다."""
#         return self.data["best_score"]