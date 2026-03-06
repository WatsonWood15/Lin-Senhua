from pomodoro_service import PomodoroService
from data import load_sample_tasks

def main():
    service = PomodoroService()
    load_sample_tasks(service)

    while True:
        print("\n" + "=" * 50)
        print("🍅 番茄鐘時間管理系統")
        print("1. 顯示任務優先排行 (Heap Sort)")
        print("2. 新增任務")
        print("3. 開始番茄鐘循環")
        print("4. 離開")
        choice = input("請輸入選項 (1-4): ").strip()

        if choice == "1":
            service.show_priority_tasks()
        elif choice == "2":
            name = input("任務名稱: ").strip()
            try:
                priority = int(input("優先度 (1-10，越高越急): ").strip())
                if 1 <= priority <= 10:
                    service.add_task(name, priority)
                else:
                    print("優先度請輸入 1-10")
            except ValueError:
                print("優先度必須是數字")
        elif choice == "3":
            service.start_pomodoro_cycle()
        elif choice == "4":
            print("感謝使用！記得保持生產力～")
            break
        else:
            print("無效選項，請輸入 1-4")

if __name__ == "__main__":
    main()