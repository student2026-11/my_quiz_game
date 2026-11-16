import signal
import sys
import time

# 1. 비상 지침서(함수) 만들기
def signal_handler(sig, frame):
    print("\n\n[확인] Ctrl+C 신호를 감지했습니다!")
    print("데이터를 저장하고 프로그램을 종료합니다... 휘리릭!")
    sys.exit(0)

# 2. 시스템에 지침서 등록하기 (Ctrl+C 상황 지정)
signal.signal(signal.SIGINT, signal_handler)

print("프로그램이 실행 중입니다... (종료하려면 Ctrl+C를 누르세요)")

# 3. 프로그램이 바로 끝나지 않게 무한 루프로 대기
try:
    while True:
        time.sleep(1) # 1초마다 대기하며 신호를 기다림
except KeyboardInterrupt:
    # 사실 signal_handler가 먼저 가로채기 때문에 여기까지 안 올 수도 있습니다.
    pass