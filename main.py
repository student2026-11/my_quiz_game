from quiz import Quiz, QuizGame

def main():
    # 1. 게임 객체 생성
    game = QuizGame()

    # 2. 문제 추가 (질문, 보기 리스트, 정답 번호)
    q1 = Quiz("파이썬의 탄생 연도는?", ["1989년", "1991년", "1995년", "2000년"], 2)
    q2 = Quiz("파이썬을 만든 사람은?", ["귀도 반 로섬", "빌 게이츠", "스티브 잡스", "제임스 고슬링"], 1)
    q3 = Quiz("파이썬의 특징이 아닌 것은?", ["읽기 쉽다", "오픈 소스이다", "컴파일 속도가 가장 빠르다", "라이브러리가 풍부하다"], 3)

    game.add_quiz(q1)
    game.add_quiz(q2)
    game.add_quiz(q3)

    # 3. 게임 시작!
    game.start()

if __name__ == "__main__":
    main()