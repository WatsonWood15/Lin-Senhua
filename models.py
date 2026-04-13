from abc import ABC, abstractmethod
import time
import msvcrt

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
        print(f"\n🍅 Work session started! ({self._duration // 60} minutes)")
        print("Hint: Press [P] to pause | Press [Q] to quit | Press Enter to resume")
        self._is_running = True
        self._paused = False

        while self._remaining > 0 and self._is_running:
            if self._paused:
                print("\n⏸️ Paused... Press Enter to resume | Press Q to quit", end="\r")
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'q':
                        print("\nExited current timer")
                        self._is_running = False
                        return
                    elif key == '\r':
                        self._paused = False
                        print("\n▶️ Resuming timer...")
                time.sleep(0.2)
                continue

            mins, secs = divmod(self._remaining, 60)
            print(f"Time remaining: {mins:02d}:{secs:02d}   (P=pause | Q=quit)", end="\r")

            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'p':
                    self._paused = True
                    print("\n⏸️ Paused...")
                elif key == 'q':
                    print("\nExited current timer")
                    self._is_running = False
                    return

            time.sleep(1)
            self._remaining -= 1

        if self._remaining == 0:
            print("\n🎉 Work finished! Time for a break~")

class BreakTimer(AbstractTimer):
    def start(self):
        print(f"\n☕ Break session started! ({self._duration // 60} minutes)")
        print("Hint: Press [P] to pause | Press [Q] to quit | Press Enter to resume")
        self._is_running = True
        self._paused = False

        while self._remaining > 0 and self._is_running:
            if self._paused:
                print("\n⏸️ Paused... Press Enter to resume | Press Q to quit", end="\r")
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'q':
                        print("\nExited current timer")
                        self._is_running = False
                        return
                    elif key == '\r':
                        self._paused = False
                        print("\n▶️ Resuming timer...")
                time.sleep(0.2)
                continue

            mins, secs = divmod(self._remaining, 60)
            print(f"Time remaining: {mins:02d}:{secs:02d}   (P=pause | Q=quit)", end="\r")

            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'p':
                    self._paused = True
                    print("\n⏸️ Paused...")
                elif key == 'q':
                    print("\nExited current timer")
                    self._is_running = False
                    return

            time.sleep(1)
            self._remaining -= 1

        if self._remaining == 0:
            print("\n✅ Break finished! Ready for the next round~")