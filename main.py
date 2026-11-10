# main.py
import sys
from quiz import QuizGame, Quiz

def main():
    game = QuizGame()
    
    # 초기 문제 (원하는 만큼 추가하세요)
    game.add_quiz(Quiz("파이썬의 탄생 연도는?", ["1989년", "1991년", "1995년", "2000년"], 2))
    # 1. 초기 문제들을 여기서 추가합니다 (while 루프 밖에서!)
    game.add_quiz(Quiz("파이썬의 탄생 연도는?", ["1989년", "1991년", "1995년", "2000년"], 2))
    game.add_quiz(Quiz("대한민국의 수도는?", ["부산", "인천", "서울", "대구"], 3)) # 여기에 추가!
    game.add_quiz(Quiz("일본의 수도는?", ["오사카", "도쿄", "교토", "후쿠오카"], 2)) # 여기에 추가!
    game.add_quiz(Quiz("가장 큰 행성은?", ["지구", "화성", "목성", "금성"], 3)) # 여기에 추가!


    while True: # 이 루프가 있어야 메뉴가 계속 반복됩니다!
        print("\n==========================================")
        print("      🎯 나만의 퀴즈 게임 🎯      ")
        print("==========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("==========================================")
        
        choice = input("선택: ")

        if choice == "1":
            # 1번 선택 시: 퀴즈 풀기 화면으로 전환
            game.start()
            
        elif choice == "2":
            # 2번 선택 시: 퀴즈 추가 화면으로 전환
            print("\n📌 새로운 퀴즈를 추가합니다.")
            question = input("문제를 입력하세요: ")
            options = []
            for i in range(1, 5):
                opt = input(f"선택지 {i}: ")
                options.append(opt)
            try:
                answer = int(input("정답 번호 (1-4): "))
                game.add_quiz(Quiz(question, options, answer))
                print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")
            except ValueError:
                print("\n❌ 숫자를 입력해야 합니다. 추가 실패!")

        elif choice == "3":
            print("\n📋 등록된 퀴즈 목록")
            if not game.quizzes:
                print("등록된 퀴즈가 없습니다.")
            else:
                # 이 줄(48번 줄 근처)의 시작 간격이 else보다 한 단계 더 들어가야 합니다.
                for i, q in enumerate(game.quizzes, 1):
                    print(f"{i}. {q.question}")
                    for idx, option in enumerate(q.options, 1):
                        print(f"   ({idx}) {option}")
                    print(f"   ✅ 정답: {q.answer}번")
                    print("-" * 30)

        elif choice == "4":
            # 4번 선택 시: 점수 확인
            score = game.load_best_score()
            print(f"\n🏆 현재 최고 점수: {score}점")

        elif choice == "5":
            # 5번 선택 시: 종료
            print("\n게임을 종료합니다. 즐거웠어요! 👋")
            break # while 루프를 빠져나갑니다.
        
        else:
            print("\n❌ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

if __name__ == "__main__":
    main()