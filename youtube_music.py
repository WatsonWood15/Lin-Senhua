import webbrowser
import random
from tkinter import messagebox

class YouTubeMusicPlayer:
    def __init__(self):
        self.lofi_live_list = [
            {"name": "lofi hip hop radio 📚 beats to relax/study to", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk"},
            {"name": "synthwave radio 🌌 beats to chill/game to", "url": "https://www.youtube.com/watch?v=4xDzrJKXOOY"},
            {"name": "jazz lofi radio 🎷 beats to chill/study to", "url": "https://www.youtube.com/watch?v=HuFYqnbVbzY"},
            {"name": "relaxing jazz music 🌹 cozy radio to study/chill to", "url": "https://www.youtube.com/watch?v=A8jDx9TLMQc"},
            {"name": "christmas lofi music 🎄 cozy radio to get festive to", "url": "https://www.youtube.com/watch?v=XSXEaikz0Bc"},
            {"name": "classical music radio 🎻 relaxing songs to read/study to", "url": "https://www.youtube.com/watch?v=jXAEIWcGXwE"},
        ]

    def open_player(self):
        try:
            live = random.choice(self.lofi_live_list)
            
            webbrowser.open_new(live["url"])

        except Exception as e:
            messagebox.showerror("錯誤", f"無法開啟 LofiGirl 直播間：\n{str(e)}")