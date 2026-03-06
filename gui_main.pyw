import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import os
from pytube import YouTube
from pomodoro_service import PomodoroService
from data import load_sample_tasks

class PomodoroGUI:
    def __init__(self):
        pygame.mixer.init()
        self.root = tk.Tk()
        self.root.title("🍅 番茄鐘 - 自訂時間 & YouTube 音樂")
        self.root.geometry("700x750")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.service = PomodoroService()
        load_sample_tasks(self.service)

        # 自訂時間（單位：分鐘）
        self.work_time = 25
        self.short_break = 5
        self.long_break = 15

        self.time_left = self.work_time * 60
        self.is_running = False
        self.is_work = True
        self.cycle = 1
        self.current_music = None

        self.setup_ui()

    def setup_ui(self):
        # 標題
        tk.Label(self.root, text="番茄鐘時間管理系統", font=("Microsoft YaHei", 24, "bold"),
                 bg="#1e1e1e", fg="#ffffff").pack(pady=15)

        # 大計時器
        self.timer_label = tk.Label(self.root, text="25:00", font=("Digital-7", 88, "bold"),
                                    bg="#1e1e1e", fg="#ff5252")
        self.timer_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text=f"第 1 輪 - 工作時間 ({self.work_time} 分)", font=("Microsoft YaHei", 14),
                                     bg="#1e1e1e", fg="#bbbbbb")
        self.status_label.pack(pady=5)

        # 自訂時間區
        custom_frame = tk.LabelFrame(self.root, text="自訂時間 (分鐘)", font=("Microsoft YaHei", 12),
                                     bg="#1e1e1e", fg="#ffffff")
        custom_frame.pack(pady=10, padx=40, fill="x")

        row1 = tk.Frame(custom_frame, bg="#1e1e1e")
        row1.pack(fill="x", pady=5)
        tk.Label(row1, text="工作時間：", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=10)
        self.work_entry = tk.Entry(row1, width=8)
        self.work_entry.insert(0, str(self.work_time))
        self.work_entry.pack(side="left")
        tk.Label(row1, text="短休息：", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=10)
        self.short_entry = tk.Entry(row1, width=8)
        self.short_entry.insert(0, str(self.short_break))
        self.short_entry.pack(side="left")
        tk.Label(row1, text="長休息：", bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=10)
        self.long_entry = tk.Entry(row1, width=8)
        self.long_entry.insert(0, str(self.long_break))
        self.long_entry.pack(side="left")

        ttk.Button(custom_frame, text="套用自訂時間", command=self.apply_custom_time).pack(pady=10)

        # 計時器按鈕
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="▶ 開始", command=self.start_timer).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="⏸ 暫停", command=self.pause_timer).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="⟳ 重置", command=self.reset_timer).grid(row=0, column=2, padx=10)

        # 音樂區
        music_frame = tk.LabelFrame(self.root, text="🎵 YouTube 音樂播放", font=("Microsoft YaHei", 12),
                                    bg="#1e1e1e", fg="#ffffff")
        music_frame.pack(pady=15, padx=40, fill="x")

        tk.Label(music_frame, text="貼上 YouTube 影片連結（單一影片）：", bg="#1e1e1e", fg="#ffffff").pack(anchor="w", padx=15)
        self.music_entry = tk.Entry(music_frame, font=("Microsoft YaHei", 11))
        self.music_entry.pack(fill="x", padx=15, pady=8)
        self.music_entry.insert(0, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # 測試用

        music_btn_frame = tk.Frame(music_frame, bg="#1e1e1e")
        music_btn_frame.pack(pady=5)
        ttk.Button(music_btn_frame, text="▶ 播放音樂", command=self.play_youtube_music).pack(side="left", padx=10)
        ttk.Button(music_btn_frame, text="⏹ 停止音樂", command=self.stop_music).pack(side="left", padx=10)

        # 音量控制 + 跳動效果
        vol_frame = tk.Frame(music_frame, bg="#1e1e1e")
        vol_frame.pack(fill="x", padx=15, pady=8)
        tk.Label(vol_frame, text="音量：", bg="#1e1e1e", fg="#ffffff").pack(side="left")
        self.volume_slider = ttk.Scale(vol_frame, from_=0, to=100, orient="horizontal", command=self.change_volume)
        self.volume_slider.set(70)
        self.volume_slider.pack(side="left", fill="x", expand=True, padx=10)

        # 任務區
        task_frame = tk.LabelFrame(self.root, text="任務管理", font=("Microsoft YaHei", 11), bg="#1e1e1e", fg="#ffffff")
        task_frame.pack(pady=10, padx=40, fill="x")

        tk.Label(task_frame, text="任務名稱：", bg="#1e1e1e", fg="#ffffff").pack(anchor="w", padx=15)
        self.task_entry = tk.Entry(task_frame, font=("Microsoft YaHei", 11))
        self.task_entry.pack(fill="x", padx=15, pady=5)

        pri_frame = tk.Frame(task_frame, bg="#1e1e1e")
        pri_frame.pack(fill="x", padx=15)
        tk.Label(pri_frame, text="優先度 (1-10)：", bg="#1e1e1e", fg="#ffffff").pack(side="left")
        self.pri_entry = tk.Entry(pri_frame, width=8)
        self.pri_entry.pack(side="left", padx=5)
        ttk.Button(pri_frame, text="新增任務", command=self.add_task).pack(side="right")

        ttk.Button(self.root, text="📊 顯示任務優先排行 (Heap Sort)", command=self.show_ranking).pack(pady=15)

        self.update_display()

        # 音量跳動動畫變數
        self.volume_anim_running = False
        self.volume_direction = 1
        self.volume_base = 70

    def apply_custom_time(self):
        try:
            self.work_time = int(self.work_entry.get())
            self.short_break = int(self.short_entry.get())
            self.long_break = int(self.long_entry.get())
            if self.work_time < 1 or self.short_break < 1 or self.long_break < 1:
                raise ValueError
            messagebox.showinfo("成功", "時間設定已更新")
            self.reset_timer()
        except:
            messagebox.showwarning("錯誤", "請輸入有效的正整數")

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
        self.time_left = self.work_time * 60 if self.is_work else self.short_break * 60
        self.update_display()

    def countdown(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            messagebox.showinfo("完成！", "本輪結束！")
            self.is_work = not self.is_work
            self.time_left = self.work_time * 60 if self.is_work else self.short_break * 60
            self.status_label.config(text=f"第 {self.cycle} 輪 - {'工作時間' if self.is_work else '休息時間'}")
            self.is_running = False

    def add_task(self):
        name = self.task_entry.get().strip()
        try:
            pri = int(self.pri_entry.get().strip())
            if name and 1 <= pri <= 10:
                self.service.add_task(name, pri)
                messagebox.showinfo("成功", f"已新增：{name}")
                self.task_entry.delete(0, tk.END)
                self.pri_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("錯誤", "請輸入有效名稱與優先度")
        except:
            messagebox.showwarning("錯誤", "優先度必須是 1-10 的數字")

    def show_ranking(self):
        win = tk.Toplevel(self.root)
        win.title("任務優先排行")
        win.geometry("420x320")
        win.configure(bg="#1e1e1e")
        text = tk.Text(win, bg="#2d2d2d", fg="#ffffff", font=("Microsoft YaHei", 11))
        text.pack(padx=20, pady=20, fill="both", expand=True)
        temp = sorted(self.service.tasks, key=lambda x: x['priority'], reverse=True)
        for i, t in enumerate(temp, 1):
            text.insert(tk.END, f"{i}. {t['name']} (優先度 {t['priority']})\n")
        text.config(state="disabled")

    # ======================== YouTube 音樂播放 ========================
    def play_youtube_music(self):
        url = self.music_entry.get().strip()
        if not url:
            messagebox.showwarning("錯誤", "請貼上 YouTube 影片連結")
            return

        try:
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            if not audio_stream:
                messagebox.showerror("錯誤", "無法取得音訊流")
                return

            if not os.path.exists("music"):
                os.makedirs("music")
            file_path = audio_stream.download(output_path="music", filename="temp_audio.mp3")

            if not os.path.exists(file_path) or os.path.getsize(file_path) < 100000:
                messagebox.showerror("錯誤", "下載檔案失敗或檔案太小")
                return

            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(-1)  # 循環播放
            pygame.mixer.music.set_volume(self.volume_slider.get() / 100)

            messagebox.showinfo("播放中", f"正在播放：{yt.title}\n\n音量可調整\n\n(若無聲音，請檢查電腦音量與耳機)")
            self.start_volume_anim()

        except Exception as e:
            messagebox.showerror("錯誤", f"播放失敗：\n{str(e)}\n\n請確認連結是單一影片，並檢查網路")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.volume_anim_running = False
        messagebox.showinfo("已停止", "音樂已停止")

    def change_volume(self, val):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.set_volume(float(val) / 100)

    def start_volume_anim(self):
        if pygame.mixer.music.get_busy() and not self.volume_anim_running:
            self.volume_anim_running = True
            self.animate_volume()

    def animate_volume(self):
        if not self.volume_anim_running or not pygame.mixer.music.get_busy():
            self.volume_anim_running = False
            return

        current = self.volume_slider.get()
        new_val = current + 0.5 if self.volume_direction > 0 else current - 0.5
        if new_val > self.volume_base + 15 or new_val < self.volume_base - 15:
            self.volume_direction *= -1
        self.volume_slider.set(new_val)
        pygame.mixer.music.set_volume(new_val / 100)
        self.root.after(120, self.animate_volume)

if __name__ == "__main__":
    app = PomodoroGUI()
    app.root.mainloop()