# COMPS209W Course Project  
**🍅 Pomodoro Timer**

A clean, modern, and customizable **Pomodoro Timer** built with Python to help you stay focused and productive.

## Features
- Customizable work / short break / long break durations (in minutes)
- Task management with priority levels (1–10)
- Priority ranking powered by Heap Sort (highest priority first)
  
## 📁 Repository Structure

```text
PomodoroTimer/
├── gui_main.pyw              # Main GUI application
├── youtube_music.py          # YouTube Music random player
├── pomodoro_service.py       # Core service + MaxHeap
├── models.py                 # AbstractTimer, WorkTimer, BreakTimer (OOP)
├── data.py                   # Sample data loader (optional)
├── main.py                   # Console version (for reference)
├── run.bat                   # One-click launcher (recommended)
├── install.bat               # Install required packages
├── start_hidden.vbs          # Hidden console launcher
├── README.md                 # This file
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

## Inspiration & References

This project was inspired by the following excellent open-source projects:

- **[KEGOMODORO](https://github.com/Kagankakao/KEGOMODORO)** – Clean Pomodoro timer design and UI layout
- **[ytmdesktop2](https://github.com/Venipa/ytmdesktop2)** – YouTube Music desktop integration ideas
