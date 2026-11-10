import sys

def show_menu():
    print("\n==========================================")
    print("      🎯 나만의 퀴즈 게임 🎯      ")
    print("==========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("==========================================")

def add_new_quiz_ui(game):
    print("\n📌 새로운 퀴즈를 추가합니다.")
    question = input("문제를 입력하세요: ")
    options = []
    for i in range(1, 5):
        opt = input(f"선택지 {i}: ")
        options.append(opt)
    
    try:
        answer = int(input("정답 번호 (1-4): "))
        if 1 <= answer <= 4:
            # QuizGame 클래스의 add_quiz 메서드 사용
            from quiz_game import Quiz
            game.add_quiz(Quiz(question, options, answer))
            print("\n✅ 퀴즈가 추가되었습니다!")
        else:
            print("❌ 번호는 1에서 4 사이여야 합니다.")
    except ValueError:
        print("❌ 숫자만 입력 가능합니다.")

def main():
    # QuizGame 객체 생성 (기존에 만든 클래스)
    from quiz_game import QuizGame, Quiz
    game = QuizGame()

    # 기본 문제 몇 개 추가 (예시)
    game.add_quiz(Quiz("파이썬에서 리스트에 요소를 추가하는 메서드는?", ["push()", "add()", "append()", "insert()"], 3))

    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "1":
            game.start()
        elif choice == "2":
            add_new_quiz_ui(game)
        elif choice == "3":
            print("\n📋 현재 등록된 퀴즈 목록")
            for i, q in enumerate(game.quizzes, 1):
                print(f"{i}. {q.question}")
        elif choice == "4":
            # 최고 점수 확인 (이미 구현된 load_high_score 활용)
            high_score = game.load_high_score()
            print(f"\n🏆 현재 최고 기록: {high_score}점")
        elif choice == "5":
            print("\n게임을 종료합니다. 즐거웠어요! 👋")
            sys.exit()
        else:
            print("\n❌ 잘못된 선택입니다. 1~5 사이의 숫자를 입력하세요.")

if __name__ == "__main__":
    main()