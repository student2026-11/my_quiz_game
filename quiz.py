import json
import os

class QuizManager:
    def __init__(self):
        self.filename = "state.json"
        # 기본 데이터 설정
        self.default_data = {
            "quizzes": [
                {"question": "우리나라의 전통 고유 의상은 무엇일까요?", "options": ["치파오", "기모노", "한복", "사리"], "answer": 3},
                {"question": "대한민국의 수도는?", "options": ["부산", "인천", "서울", "대구"], "answer": 3},
                {"question": "가장 큰 행성은?", "options": ["지구", "화성", "목성", "토성"], "answer": 3}, 
                {"question": "지구에서 가장 가까운 행성은?", "options": ["태양", "화성", "목성", "금성"], "answer": 1},
                {"question": "빨간색과 파란색 물감을 섞으면 무슨색이 될까요?", "options": ["초록색", "노란색", "회색", "보라색"], "answer": 4}               

            ],
            "best_score": 0
        }
        self.data = self.load_state()

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
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"❌ 파일 저장 오류: {e}")

    def add_quiz(self, question, options, answer):
        """새로운 퀴즈를 추가합니다."""
        self.data["quizzes"].append({"question": question, "options": options, "answer": answer})
        self.save_state()

    def get_quizzes(self):
        """퀴즈 목록을 가져옵니다."""
        return self.data["quizzes"]

    def update_best_score(self, score):
        """최고 점수를 갱신합니다."""
        if score > self.data["best_score"]:
            self.data["best_score"] = score
            self.save_state()
            return True
        return False

    def get_best_score(self):
        """최고 점수를 가져옵니다."""
        return self.data["best_score"]