# COMPS209W Course Project  
**Library Management System + Heap & Heap Sort**

## 📁 Repository Structure

```text
PomodoroTimer/
├── models.py                 # AbstractTimer, WorkTimer, BreakTimer (OOP core)
├── pomodoro_service.py       # PomodoroService + MaxHeap + Heap Sort
├── data.py                   # Sample tasks loader
├── main.py                   # Console version entry point
├── gui_main.pyw              # GUI version (Tkinter) - double-click to run
├── run.bat                   # Double-click launcher for GUI (no console window)
└── README.md                 # This file

🚀 How to Run
GUI Version (Recommended - Modern Interface)

Double-click run.bat
→ Opens a clean, dark-mode GUI window (no black console)
Features:
Custom work/break time (set in minutes)
Add tasks with priority (1–10)
Show priority ranking (Heap Sort)
Countdown timer with pause/resume/exit support
