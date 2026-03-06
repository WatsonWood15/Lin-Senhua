from abc import ABC, abstractmethod
import time
import msvcrt  # Windows 專用，按鍵偵測

class AbstractTimer(ABC):
    def __init__(self, duration_minutes):
        self._duration = duration_minutes * 60
        self._remaining = self._duration
        self._is_running = False
        self._paused = False

    @abstractmethod
    def start(self):
        pass

class WorkTimer(AbstractTimer):
    def start(self):
        print(f"\n🍅 工作階段開始！（{self._duration // 60} 分鐘）")
        print("提示：按 [P] 暫停 | 按 [Q] 退出 | 按 Enter 繼續")
        self._is_running = True
        self._paused = False

        while self._remaining > 0 and self._is_running:
            if self._paused:
                print("\n⏸️ 已暫停... 按 Enter 繼續 | 按 Q 退出", end="\r")
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'q':
                        print("\n已退出當前計時器")
                        self._is_running = False
                        return
                    elif key == '\r':  # Enter
                        self._paused = False
                        print("\n▶️ 繼續計時...")
                time.sleep(0.2)
                continue

            mins, secs = divmod(self._remaining, 60)
            print(f"剩餘時間: {mins:02d}:{secs:02d}   (P=暫停 | Q=退出)", end="\r")

            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'p':
                    self._paused = True
                    print("\n⏸️ 已暫停...")
                elif key == 'q':
                    print("\n已退出當前計時器")
                    self._is_running = False
                    return

            time.sleep(1)
            self._remaining -= 1

        if self._remaining == 0:
            print("\n🎉 工作結束！該休息了～")

class BreakTimer(AbstractTimer):
    def start(self):
        print(f"\n☕ 休息階段開始！（{self._duration // 60} 分鐘）")
        print("提示：按 [P] 暫停 | 按 [Q] 退出 | 按 Enter 繼續")
        self._is_running = True
        self._paused = False

        while self._remaining > 0 and self._is_running:
            if self._paused:
                print("\n⏸️ 已暫停... 按 Enter 繼續 | 按 Q 退出", end="\r")
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'q':
                        print("\n已退出當前計時器")
                        self._is_running = False
                        return
                    elif key == '\r':
                        self._paused = False
                        print("\n▶️ 繼續計時...")
                time.sleep(0.2)
                continue

            mins, secs = divmod(self._remaining, 60)
            print(f"剩餘時間: {mins:02d}:{secs:02d}   (P=暫停 | Q=退出)", end="\r")

            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'p':
                    self._paused = True
                    print("\n⏸️ 已暫停...")
                elif key == 'q':
                    print("\n已退出當前計時器")
                    self._is_running = False
                    return

            time.sleep(1)
            self._remaining -= 1

        if self._remaining == 0:
            print("\n✅ 休息結束！繼續下一輪～")