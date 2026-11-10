from quiz import Quiz, QuizGame

def main():
    game = QuizGame()

    # 문제 1
    game.add_quiz(Quiz(
        "파이썬의 탄생 연도는?", 
        ["1989년", "1991년", "1995년", "2000년"], 
        2
    ))

    # 문제 2 추가
    game.add_quiz(Quiz(
        "파이썬의 창시자는?", 
        ["제임스 고슬링", "귀도 반 로섬", "데니스 리치", "비야네 스트롭스트룹"], 
        2
    ))

    # 문제 3 추가
    game.add_quiz(Quiz(
        "파이썬 파일의 확장자는?", 
        [".py", ".python", ".pyt", ".exe"], 
        1
    ))

    # 문제 4 추가
    game.add_quiz(Quiz(
        "리스트에 요소를 추가하는 함수는?", 
        ["add()", "push()", "append()", "insert_at()"], 
        3
    ))

    # 문제 5 추가
    game.add_quiz(Quiz(
        "파이썬에서 '출력'을 담당하는 함수는?", 
        ["input()", "print()", "output()", "write()"], 
        2
    ))

    # 게임 시작!
    game.start()

if __name__ == "__main__":
    main()