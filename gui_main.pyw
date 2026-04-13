import tkinter as tk
from tkinter import ttk, messagebox
from pomodoro_service import PomodoroService
from youtube_music import YouTubeMusicPlayer

class PomodoroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🍅 Pomodoro Timer")
        self.root.geometry("850x700")
        self.root.minsize(700, 600)
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(True, True)

        self.service = PomodoroService()
        self.music_player = YouTubeMusicPlayer()

        self.work_time = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60

        self.time_left = self.work_time
        self.is_running = False
        self.is_work = True
        self.cycle = 1

        self.setup_ui()

    def setup_ui(self):
        main_canvas = tk.Canvas(self.root, bg="#1e1e1e", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = tk.Frame(main_canvas, bg="#1e1e1e")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )

        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)

        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            main_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        main_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        content_frame = tk.Frame(scrollable_frame, bg="#1e1e1e")
        content_frame.pack(expand=True, pady=40)

        def center_content(event=None):
            canvas_width = main_canvas.winfo_width()
            content_width = content_frame.winfo_reqwidth()
            if canvas_width > content_width:
                x = (canvas_width - content_width) // 2
                main_canvas.coords(main_canvas.find_withtag("all")[0], x, 0)

        main_canvas.bind("<Configure>", center_content)

        # Title
        tk.Label(content_frame, text="Pomodoro Timer", font=("Microsoft YaHei", 28, "bold"),
                 bg="#1e1e1e", fg="#ffffff").pack(pady=20)

        # Big Timer
        self.timer_label = tk.Label(content_frame, text="25:00", font=("Digital-7", 100, "bold"),
                                    bg="#1e1e1e", fg="#ff5252")
        self.timer_label.pack(pady=20)

        self.status_label = tk.Label(content_frame, text="Work Time", 
                                     font=("Microsoft YaHei", 18), bg="#1e1e1e", fg="#bbbbbb")
        self.status_label.pack(pady=10)

        # Timer buttons
        btn_frame = tk.Frame(content_frame, bg="#1e1e1e")
        btn_frame.pack(pady=20)
        ttk.Button(btn_frame, text="▶ Start", command=self.start_timer).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="⏸ Pause", command=self.pause_timer).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="⏭ Skip", command=self.skip_timer).grid(row=0, column=2, padx=10)
        ttk.Button(btn_frame, text="⟳ Reset", command=self.reset_timer).grid(row=0, column=3, padx=10)

        # Custom time
        custom_frame = tk.LabelFrame(content_frame, text="Custom Time", font=("Microsoft YaHei", 12),
                                     bg="#1e1e1e", fg="#ffffff")
        custom_frame.pack(pady=20, padx=80, fill="x")

        row_work = tk.Frame(custom_frame, bg="#1e1e1e")
        row_work.pack(fill="x", pady=8)
        tk.Label(row_work, text="Work Time:", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=10)
        self.work_min = tk.Entry(row_work, width=5); self.work_min.insert(0, "25"); self.work_min.pack(side="left")
        tk.Label(row_work, text="min", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=2)
        self.work_sec = tk.Entry(row_work, width=5); self.work_sec.insert(0, "00"); self.work_sec.pack(side="left")
        tk.Label(row_work, text="sec", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=5)

        row_short = tk.Frame(custom_frame, bg="#1e1e1e")
        row_short.pack(fill="x", pady=8)
        tk.Label(row_short, text="Short Break:", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=10)
        self.short_min = tk.Entry(row_short, width=5); self.short_min.insert(0, "5"); self.short_min.pack(side="left")
        tk.Label(row_short, text="min", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=2)
        self.short_sec = tk.Entry(row_short, width=5); self.short_sec.insert(0, "00"); self.short_sec.pack(side="left")
        tk.Label(row_short, text="sec", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=5)

        row_long = tk.Frame(custom_frame, bg="#1e1e1e")
        row_long.pack(fill="x", pady=8)
        tk.Label(row_long, text="Long Break:", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=10)
        self.long_min = tk.Entry(row_long, width=5); self.long_min.insert(0, "15"); self.long_min.pack(side="left")
        tk.Label(row_long, text="min", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=2)
        self.long_sec = tk.Entry(row_long, width=5); self.long_sec.insert(0, "00"); self.long_sec.pack(side="left")
        tk.Label(row_long, text="sec", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=5)

        ttk.Button(custom_frame, text="Apply Custom Time", command=self.apply_custom_time).pack(pady=15)

        # YouTube Music
        music_frame = tk.LabelFrame(content_frame, text="🎵 Music", font=("Microsoft YaHei", 12),
                                    bg="#1e1e1e", fg="#ffffff")
        music_frame.pack(pady=15, padx=80, fill="x")
        ttk.Button(music_frame, text="🎵 Open Music Player", command=self.open_youtube_music).pack(pady=15)

        # Task Management
        task_frame = tk.LabelFrame(content_frame, text="Task Management", font=("Microsoft YaHei", 12),
                                   bg="#1e1e1e", fg="#ffffff")
        task_frame.pack(pady=15, padx=80, fill="x")

        input_frame = tk.Frame(task_frame, bg="#1e1e1e")
        input_frame.pack(fill="x", padx=15, pady=8)
        tk.Label(input_frame, text="Task Name:", bg="#1e1e1e", fg="#ffffff").pack(side="left")
        self.task_entry = tk.Entry(input_frame, font=("Microsoft YaHei", 11))
        self.task_entry.pack(side="left", padx=5, fill="x", expand=True)

        tk.Label(input_frame, text="Priority:", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=5)
        self.pri_entry = tk.Entry(input_frame, width=6)
        self.pri_entry.pack(side="left", padx=5)

        self.task_listbox = tk.Listbox(task_frame, height=8, font=("Microsoft YaHei", 11), bg="#2d2d2d", fg="#ffffff")
        self.task_listbox.pack(fill="x", padx=15, pady=8)

        btn_task_frame = tk.Frame(task_frame, bg="#1e1e1e")
        btn_task_frame.pack(fill="x", padx=15, pady=5)
        ttk.Button(btn_task_frame, text="Add Task", command=self.add_task).pack(side="left", padx=5)
        ttk.Button(btn_task_frame, text="Delete Selected Task", command=self.delete_selected_task).pack(side="left", padx=5)

        self.update_display()


    def skip_timer(self):
        if not self.is_running:
            return
        self.is_running = False
        self.is_work = not self.is_work
        if self.is_work:
            self.time_left = self.work_time
            self.status_label.config(text="Work Time")
        else:
            self.time_left = self.short_break
            self.status_label.config(text="Break Time")
        self.update_display()

    def open_youtube_music(self):
        self.music_player.open_player()

    def add_task(self):
        name = self.task_entry.get().strip()
        try:
            pri = int(self.pri_entry.get().strip())
            if name and 1 <= pri <= 10:
                self.service.add_task(name, pri)
                self.task_listbox.insert(tk.END, f"{name} (Priority {pri})")
                self.task_entry.delete(0, tk.END)
                self.pri_entry.delete(0, tk.END)
        except:
            pass

    def delete_selected_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            return
        index = selected[0]
        self.task_listbox.delete(index)

    def apply_custom_time(self):
        try:
            w_min = int(self.work_min.get() or 0)
            w_sec = int(self.work_sec.get() or 0)
            s_min = int(self.short_min.get() or 0)
            s_sec = int(self.short_sec.get() or 0)
            l_min = int(self.long_min.get() or 0)
            l_sec = int(self.long_sec.get() or 0)

            self.work_time = w_min * 60 + w_sec
            self.short_break = s_min * 60 + s_sec
            self.long_break = l_min * 60 + l_sec
            self.reset_timer()
        except:
            pass

    def update_display(self):
        m, s = divmod(self.time_left, 60)
        self.timer_label.config(text=f"{m:02d}:{s:02d}")

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def pause_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.time_left = self.work_time if self.is_work else self.short_break
        self.update_display()

    def countdown(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            messagebox.showinfo("Completed!", "Round finished!")
            self.is_work = not self.is_work
            self.time_left = self.work_time if self.is_work else self.short_break
            self.status_label.config(text="Work Time" if self.is_work else "Break Time")
            self.is_running = False

if __name__ == "__main__":
    app = PomodoroGUI()
    app.root.mainloop()