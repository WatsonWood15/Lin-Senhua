# COMPS209W Course Project  
**🍅 Pomodoro Timer**

A clean, modern, and customizable **Pomodoro Timer** built with Python to help you stay focused and productive.

## Features
- Customizable work / short break / long break durations (in minutes)
- Task management with priority levels (1–10)
- Priority ranking powered by Heap Sort (highest priority first)
- Beautiful dark-mode GUI (Tkinter) with large countdown display
- Volume slider with animated feedback when music is playing (optional extension)
- Double-click to launch (no console window)
  
## 📁 Repository Structure

```text
PomodoroTimer/
├── models.py                 # AbstractTimer, WorkTimer, BreakTimer (OOP core)
├── pomodoro_service.py       # PomodoroService + MaxHeap + Heap Sort
├── data.py                   # Sample tasks loader
├── main.py                   # Console version entry point
├── gui_main.pyw              # GUI version (Tkinter) - double-click to run
├── install.bat
├── run.bat                   # Double-click launcher for GUI (no console window)
└── README.md                 # This file
```
---

## 🚀 How to Run

### GUI Version (Recommended)

1. Double-click `install.bat`
   → Download the prerequisites
2. Double-click `run.bat`
   → Opens a clean, dark-mode GUI window

Features:
   - Customizable work/break time (set in minutes)
   - Add tasks with priority (1–10)
   - Show task priority ranking using Heap Sort
   - Countdown timer with pause/resume/exit support (keyboard P/Q/Enter)

### Console Version

```bash
cd PomodoroTimer
python main.py

```
Menu options:

1. Show task priority ranking (Heap Sort)
2. Add new task
3. Start Pomodoro cycle
4. Exit

## 🔮 Future Improvements

  - Add background music from YouTube (single video support)
  - Save/load tasks to JSON file
  - Sound notifications for work/break end
