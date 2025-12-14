import tkinter as tk
import time
import random

TEST_DURATION = 60  # seconds

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed improves with daily practice.",
    "Python is widely used in robotics and AI.",
    "Accuracy is more important than raw speed.",
    "Consistency leads to better typing performance.",
    "Engineers should focus on problem solving skills."
]


class TypingSpeedApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Typing Speed Test")
        self.window.geometry("900x500")
        self.window.resizable(False, False)

        # State
        self.test_running = False
        self.time_left = TEST_DURATION

        self.total_typed_chars = 0
        self.total_correct_chars = 0

        self.sample_text = random.choice(SAMPLE_TEXTS)

        self.create_ui()

    def create_ui(self):
        tk.Label(
            self.window, text="Typing Speed Test",
            font=("Arial", 24, "bold")
        ).pack(pady=10)

        self.sample_label = tk.Label(
            self.window,
            text=self.sample_text,
            font=("Arial", 14),
            wraplength=800,
            justify="center"
        )
        self.sample_label.pack(pady=20)

        self.text_entry = tk.Text(
            self.window, height=5, font=("Arial", 14)
        )
        self.text_entry.pack(pady=10)
        self.text_entry.config(state="disabled")

        self.text_entry.bind("<Key>", self.start_test)
        self.text_entry.bind("<Return>", self.next_text)

        self.timer_label = tk.Label(
            self.window, text="Time: 60", font=("Arial", 16)
        )
        self.timer_label.pack(pady=5)

        self.result_label = tk.Label(
            self.window, text="", font=("Arial", 16, "bold")
        )
        self.result_label.pack(pady=10)

        tk.Button(
            self.window, text="Start / Reset",
            width=15, command=self.reset_test
        ).pack(pady=10)

    def start_test(self, event):
        if not self.test_running:
            self.test_running = True
            self.text_entry.config(state="normal")
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.window.after(1000, self.update_timer)
        else:
            self.end_test()

    def next_text(self, event):
        if not self.test_running:
            return "break"

        typed = self.text_entry.get("1.0", tk.END).strip()

        for i in range(min(len(typed), len(self.sample_text))):
            if typed[i] == self.sample_text[i]:
                self.total_correct_chars += 1

        self.total_typed_chars += len(typed)

        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.sample_label.config(text=self.sample_text)

        self.text_entry.delete("1.0", tk.END)

        return "break"

    def end_test(self):
        self.test_running = False
        self.text_entry.config(state="disabled")

        minutes = TEST_DURATION / 60
        words = self.total_typed_chars / 5
        wpm = round(words / minutes)

        if self.total_typed_chars == 0:
            accuracy = 0
        else:
            accuracy = round(
                (self.total_correct_chars / self.total_typed_chars) * 100
            )

        self.result_label.config(
            text=f"WPM: {wpm} | Accuracy: {accuracy}%"
        )

    def reset_test(self):
        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.sample_label.config(text=self.sample_text)

        self.total_typed_chars = 0
        self.total_correct_chars = 0

        self.time_left = TEST_DURATION
        self.timer_label.config(text="Time: 60")
        self.result_label.config(text="")

        self.text_entry.config(state="normal")
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.config(state="disabled")

        self.test_running = False


if __name__ == "__main__":
    window = tk.Tk()
    TypingSpeedApp(window)
    window.mainloop()
