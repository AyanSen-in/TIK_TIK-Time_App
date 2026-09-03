
import time
import tkinter as tk


class timestamp:
    """Expose the current local time in useful formats."""

    @staticmethod
    def current():
        return time.strftime('%H:%M:%S')

    @staticmethod
    def hour():
        return int(time.strftime('%H'))


def greet(hour: int) -> str:
    if 0 <= hour < 5:
        return "good night boss!"
    elif 5 <= hour < 12:
        return "good morning boss!"
    elif 12 <= hour < 16:
        return "good noon boss!"
    elif 16 <= hour < 20:
        return "good evening boss!"
    else:
        return "good night boss!"


class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.root.geometry("320x160")
        self.root.configure(bg="#bcab15")

        self.time_label = tk.Label(
            root, text="", font=("Helvetica", 36, "bold"),
            fg="#93cb1a", bg="#0E84BF"
        )
        self.time_label.pack(pady=(20, 5))

        self.greet_label = tk.Label(
            root, text="", font=("Helvetica", 16),
            fg="#a6e3a1", bg="#1e1e2e"
        )
        self.greet_label.pack(pady=5)

        self.last_hour = None
        self.update_clock()

    def update_clock(self):
        now = timestamp.current()
        hour = timestamp.hour()

        self.time_label.config(text=now)
        self.greet_label.config(text=greet(hour))

        # Fire a one-time popup notification when the hour changes
        if hour != self.last_hour:
            self.last_hour = hour
            self.notify(greet(hour))

        # refresh every second
        self.root.after(1000, self.update_clock)

    def notify(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("Notice")
        popup.geometry("260x100")
        popup.configure(bg="#313244")
        tk.Label(
            popup, text=message, font=("Helvetica", 15),
            fg="#f9e2af", bg="#313244", wraplength=220
        ).pack(expand=True)
        popup.after(4000, popup.destroy)                   # auto-close after 4s


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()