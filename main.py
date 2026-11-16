# main.py
import signal
import sys
from quiz import QuizManager

manager = None

def signal_handler(sig, frame):
    print('\n\n💾 (Ctrl+C 감지) 진행 상황을 안전하게 저장 중...')
    if manager:
        manager.save_state() # 현재 점수와 퀴즈 저장
    print('👋 안전하게 종료되었습니다!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    global manager
    manager = QuizManager()
    
    while True:
        print("\n" + "="*30)
        print("    🎯 나만의 퀴즈 게임 🎯")
        print("="*30)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("="*30)
        
        choice = input("선택: ")

        if choice == '1':
            quizzes = manager.get_quizzes()
            if not quizzes:
                print("❌ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요!")
                continue
                
            score = 0
            for i, q in enumerate(quizzes, 1):
                print(f"\n문제 {i}. {q['question']}")
                for idx, opt in enumerate(q['options'], 1):
                    print(f"{idx}. {opt}")
                
                try:
                    ans = int(input("정답 번호: "))
                    if ans == q['answer']:
                        print("✅ 정답!")
                        score += 1
                    else:
                        print(f"❌ 오답! (정답: {q['answer']}번)")
                except ValueError:
                    print("❌ 숫자만 입력 가능합니다. 오답 처리됩니다.")
            
            # [버그 수정] 괄호 위치를 수정하여 정확한 점수 계산
            final_score = int((score / len(quizzes)) * 100)
            print(f"\n🎊 최종 점수: {final_score}점")

            if manager.update_best_score(final_score):
                print("✨ 최고 점수 달성! ✨")

        elif choice == '2':
            print("\n📌 퀴즈 추가")
            question = input("문제 내용: ")
            options = [input(f"선택지 {i}: ") for i in range(1, 5)]
            try:
                answer = int(input("정답 번호 (1-4): "))
                manager.add_quiz(question, options, answer)
                print("✅ 저장 완료!")
            except ValueError:
                print("❌ 숫자를 입력해야 합니다.")

        elif choice == '3':
            print("\n📋 퀴즈 목록")
            for i, q in enumerate(manager.get_quizzes(), 1):
                print(f"{i}. {q['question']} (정답: {q['answer']}번)")

        elif choice == '4':
            print(f"\n🏆 최고 점수: {manager.get_best_score()}점")

        elif choice == '5':
            manager.save_state()
            print("👋 종료합니다!")
            break
        else:
            print("❌ 잘못된 선택입니다.")

if __name__ == "__main__":
    main()