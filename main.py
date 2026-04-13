from pomodoro_service import PomodoroService
from data import load_sample_tasks

def main():
    service = PomodoroService()
    load_sample_tasks(service)

    while True:
        print("\n" + "=" * 50)
        print("🍅 Pomodoro Time Management System")
        print("3. Start Pomodoro cycle")
        print("4. Exit")
        choice = input("Please enter option (1-4): ").strip()

        if choice == "1":
            service.show_priority_tasks()
        elif choice == "2":
            name = input("Task name: ").strip()
            try:
                priority = int(input("Priority (1-10, higher is more urgent): ").strip())
                if 1 <= priority <= 10:
                    service.add_task(name, priority)
                else:
                    print("Priority must be between 1 and 10")
            except ValueError:
                print("Priority must be a number")
        elif choice == "3":
            service.start_pomodoro_cycle()
        elif choice == "4":
            print("Thank you for using! Stay productive~")
            break
        else:
            print("Invalid option, please enter 1-4")

if __name__ == "__main__":
    main()