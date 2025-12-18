import tkinter as tk
import time

TIME_LIMIT = 5  # seconds

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Dangerous Writing App")
        self.root.geometry("700x500")

        self.last_typing_time = time.time()

        self.info_label = tk.Label(
            root,
            text="Keep typing! Stop for 5 seconds and everything will be deleted 💀",
            font=("Arial", 14, "bold"),
            fg="red"
        )
        self.info_label.pack(pady=10)

        self.text = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text.pack(expand=True, fill="both", padx=20, pady=10)

        self.text.bind("<Key>", self.on_key_press)

        self.check_timer()

    def on_key_press(self, event):
        self.last_typing_time = time.time()

    def check_timer(self):
        elapsed = time.time() - self.last_typing_time

        if elapsed >= TIME_LIMIT:
            self.text.delete("1.0", tk.END)
            self.last_typing_time = time.time()
            self.info_label.config(
                text="💀 You stopped typing! Everything is gone. Start again!",
                fg="black"
            )

        self.root.after(200, self.check_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
