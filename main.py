
import random
import signal
import sys
from quiz import QuizManager

manager = None


# 비상 종료 처리: Ctrl+C를 눌러도 데이터가 저장되도록 설정
def signal_handler(sig, frame):
    print("\n\n💾 안전하게 저장 중...")
    if manager:
        manager.save_state()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


# 함수 분리: 퀴즈 풀기 로직 (출제 방식 선택 + 문제 수 선택)
def run_quiz_session():
    all_quizzes = manager.get_quizzes()
    if not all_quizzes:
        print("❌ 등록된 퀴즈가 없습니다.")
        return 0

    total_count = len(all_quizzes)

    # 1. 출제 방식 선택 (순차 vs 랜덤)
    while True:
        print("\n출제 방식을 선택하세요:")
        print("1. 순차 출제 (등록된 순서대로)")
        print("2. 랜덤 출제 (무작위 순서)")
        mode = input("선택 (1-2): ").strip()
        if mode in ("1", "2"):
            break
        print("⚠️ 1 또는 2만 입력 가능합니다. 다시 시도해 주세요.")

    # 2. 풀 문제 수 선택
    while True:
        try:
            count = int(input(f"\n몇 문제를 푸시겠습니까? (1-{total_count}): "))
            if 1 <= count <= total_count:
                break
            print(f"⚠️ 1부터 {total_count} 사이의 숫자만 입력 가능합니다.")
        except ValueError:
            print("⚠️ 숫자만 입력 가능합니다. 다시 시도해 주세요.")

    # 3. 선택한 방식에 따라 문제 리스트 구성
    if mode == "1":
        selected_quizzes = all_quizzes[:count]  # 순차 출제
    else:
        selected_quizzes = random.sample(all_quizzes, count)  # 랜덤 출제

    score = 0
    for i, q in enumerate(selected_quizzes, 1):
        max_num = len(q.options)

        while True:
            print(f"\n문제 {i}/{count}. {q.question}")
            for idx, opt in enumerate(q.options, 1):
                print(f"{idx}. {opt}")

            # 예외 처리: 숫자가 아니거나 1~선택지 개수를 벗어난 입력 시 해당 문제를 다시 보여줌
            try:
                ans = int(input(f"정답 번호 (1-{max_num}): "))
                if 1 <= ans <= max_num:
                    break
                else:
                    print(f"⚠️ 1부터 {max_num} 사이의 번호만 입력 가능합니다. 다시 시도해 주세요.")
            except ValueError:
                print("⚠️ 숫자만 입력 가능합니다. 다시 시도해 주세요.")

        if q.is_correct(ans):
            print("✅ 정답!")
            score += 1
        else:
            print(f"❌ 오답! (정답: {q.answer}번)")

    # 점수 계산 및 최고 점수 업데이트
    final_score = int((score / count) * 100)
    print(f"\n🎊 최종 점수: {final_score}점 ({count}문제 중 {score}문제 정답)")
    if manager.update_best_score(final_score):
        print("✨ 최고 점수 달성! ✨")
    return final_score


def main():
    global manager
    manager = QuizManager()
    last_score = 0

    while True:
        print("\n" + "=" * 30)
        print("    🎯 나만의 퀴즈 게임 🎯")
        print("=" * 30)
        print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
        print("=" * 30)

        choice = input("선택: ").strip()

        if choice == "1":
            last_score = run_quiz_session()

        elif choice == "2":
            print("\n📌 퀴즈 추가")
            question = input("문제 내용: ").strip()
            options = [input(f"선택지 {i}: ").strip() for i in range(1, 5)]
            while True:
                try:
                    answer = int(input("정답 번호 (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    print("⚠️ 1부터 4 사이의 숫자만 입력해야 합니다. 다시 입력해 주세요.")
                except ValueError:
                    print("❌ 숫자를 입력해야 합니다. 다시 입력해 주세요.")
            manager.add_quiz(question, options, answer)
            print("✅ 저장 완료!")

        elif choice == "3":
            print("\n📋 퀴즈 목록")
            for i, q in enumerate(manager.get_quizzes(), 1):
                print(f"{i}. {q.question} (정답: {q.answer}번)")

        elif choice == "4":
            print(f"\n😊 최근 점수 : {last_score}점")
            print(f"🏆 최고 점수: {manager.get_best_score()}점")

        elif choice == "5":
            manager.save_state()
            print("👋 종료합니다!")
            break

        else:
            print("⚠️ 1부터 5 사이의 메뉴 번호를 선택해 주세요.")


if __name__ == "__main__":
    main()


# # # main.py
# ===============랜덤 없는 순차 퀴즈====================
# import signal
# import sys
# from quiz import QuizManager

# manager = None


# # 비상 종료 처리: Ctrl+C를 눌러도 데이터가 저장되도록 설정
# def signal_handler(sig, frame):
#     print("\n\n💾 안전하게 저장 중...")
#     if manager:
#         manager.save_state()
#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)


# # 함수 분리: 퀴즈 풀기 로직을 별도 함수로 만들어 main을 간결하게 함
# def run_quiz_session():
#     quizzes = manager.get_quizzes()
#     if not quizzes:
#         print("❌ 등록된 퀴즈가 없습니다.")
#         return 0

#     score = 0
#     for i, q in enumerate(quizzes, 1):
#         max_num = len(q.options)

#         while True:
#             print(f"\n문제 {i}. {q.question}")
#             for idx, opt in enumerate(q.options, 1):
#                 print(f"{idx}. {opt}")

#             # 예외 처리: 숫자가 아니거나 1~선택지 개수를 벗어난 입력 시 해당 문제를 다시 보여줌
#             try:
#                 ans = int(input(f"정답 번호 (1-{max_num}): "))
#                 if 1 <= ans <= max_num:
#                     break
#                 else:
#                     print(f"⚠️ 1부터 {max_num} 사이의 번호만 입력 가능합니다. 다시 시도해 주세요.")
#             except ValueError:
#                 print("⚠️ 숫자만 입력 가능합니다. 다시 시도해 주세요.")

#         if q.is_correct(ans):
#             print("✅ 정답!")
#             score += 1
#         else:
#             print(f"❌ 오답! (정답: {q.answer}번)")

#     # 점수 계산 및 최고 점수 업데이트
#     final_score = int((score / len(quizzes)) * 100)
#     print(f"\n🎊 최종 점수: {final_score}점")
#     if manager.update_best_score(final_score):
#         print("✨ 최고 점수 달성! ✨")
#     return final_score


# def main():
#     global manager
#     manager = QuizManager()
#     last_score = 0

#     while True:
#         print("\n" + "=" * 30)
#         print("    🎯 나만의 퀴즈 게임 🎯")
#         print("=" * 30)
#         print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
#         print("=" * 30)

#         choice = input("선택: ").strip()

#         if choice == "1":
#             last_score = run_quiz_session()

#         elif choice == "2":
#             print("\n📌 퀴즈 추가")
#             question = input("문제 내용: ").strip()
#             options = [input(f"선택지 {i}: ").strip() for i in range(1, 5)]
#             while True:
#                 try:
#                     answer = int(input("정답 번호 (1-4): "))
#                     if 1 <= answer <= 4:
#                         break
#                     print("⚠️ 1부터 4 사이의 숫자만 입력해야 합니다. 다시 입력해 주세요.")
#                 except ValueError:
#                     print("❌ 숫자를 입력해야 합니다. 다시 입력해 주세요.")
#             manager.add_quiz(question, options, answer)
#             print("✅ 저장 완료!")

#         elif choice == "3":
#             print("\n📋 퀴즈 목록")
#             for i, q in enumerate(manager.get_quizzes(), 1):
#                 print(f"{i}. {q.question} (정답: {q.answer}번)")

#         elif choice == "4":
#             print(f"\n😊 최근 점수 : {last_score}점")
#             print(f"🏆 최고 점수: {manager.get_best_score()}점")

#         elif choice == "5":
#             manager.save_state()
#             print("👋 종료합니다!")
#             break

#         else:
#             print("⚠️ 1부터 5 사이의 메뉴 번호를 선택해 주세요.")


# if __name__ == "__main__":
#     main()


# ================================================================

# import signal
# import sys
# from quiz import QuizManager

# manager = None

# # 비상 종료 처리: Ctrl+C를 눌러도 데이터가 저장되도록 설정
# def signal_handler(sig, frame):
#     print('\n\n💾 안전하게 저장 중...')
#     if manager:
#         manager.save_state() 
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)

# #  함수 분리: 퀴즈 풀기 로직을 별도 함수로 만들어 main을 간결하게 함

# def run_quiz_session():
#     quizzes = manager.get_quizzes()
#     if not quizzes:
#         print("❌ 등록된 퀴즈가 없습니다.")
#         return

#     score = 0
#     for i, q in enumerate(quizzes, 1):
#         max_num = len(q['options'])

#         while True:
#             print(f"\n문제 {i}. {q['question']}")
#             for idx, opt in enumerate(q['options'], 1):
#                 print(f"{idx}. {opt}")

#             # 예외 처리: 숫자가 아니거나 1~선택지 개수를 벗어난 입력 시 해당 문제를 다시 보여줌
#             try:
#                 ans = int(input(f"정답 번호 (1-{max_num}): "))
#                 if 1 <= ans <= max_num:
#                     break
#                 else:
#                     print(f"⚠️ 1부터 {max_num} 사이의 번호만 입력 가능합니다. 다시 시도해 주세요.")
#             except ValueError:
#                 print("⚠️ 숫자만 입력 가능합니다. 다시 시도해 주세요.")

#         if ans == q['answer']:
#             print("✅ 정답!")
#             score += 1
#         else:
#             print(f"❌ 오답! (정답: {q['answer']}번)")

#     # 점수 계산 및 최고 점수 업데이트
#     final_score = int((score / len(quizzes)) * 100)
#     print(f"\n🎊 최종 점수: {final_score}점")
#     if manager.update_best_score(final_score):
#         print("✨ 최고 점수 달성! ✨")
#     return final_score


# def main():
#     global manager
#     manager = QuizManager()
#     last_score = 0
    
#     while True:
#         print("\n" + "="*30)
#         print("    🎯 나만의 퀴즈 게임 🎯")
#         print("="*30)
#         print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
#         print("="*30)
        
#         choice = input("선택: ")

#         if choice == '1':
#             last_score = run_quiz_session() # 분리한 함수 호출

#         elif choice == '2':
#             print("\n📌 퀴즈 추가")
#             question = input("문제 내용: ")
#             options = [input(f"선택지 {i}: ") for i in range(1, 5)]
#             while True:
#                  try:
#                      answer = int(input("정답 번호 (1-4): "))
#                      if 1 <= answer <= 4:
#                          break
#                      print("⚠️ 1부터 4 사이의 숫자만 입력해야 합니다. 다시 입력해 주세요.")
#                  except ValueError:
#                      print("❌ 숫자를 입력해야 합니다. 다시 입력해 주세요.")
#              manager.add_quiz(question, options, answer)
#              print("✅ 저장 완료!")

#          elif choice == '3':
#              print("\n📋 퀴즈 목록")
#              for i, q in enumerate(manager.get_quizzes(), 1):
#                  print(f"{i}. {q['question']} (정답: {q['answer']}번)")

#          elif choice == '4':
#              print(f"\n😊 최근 점수 : {last_score}점")
#              print(f"\n🏆 최고 점수: {manager.get_best_score()}점")

#          elif choice == '5':
#              manager.save_state()
#              print("👋 종료합니다!")
#              break

#  if __name__ == "__main__":
#      main()



