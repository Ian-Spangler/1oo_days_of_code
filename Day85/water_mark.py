import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Watermark App")
        self.window.geometry("900x600")
        self.window.configure(bg="#f0f0f0")

        self.image = None
        self.image_tk = None

        # ---- UI Layout ----
        self.build_ui()

    def build_ui(self):
        # Frame for buttons
        control_frame = tk.Frame(self.window, bg="#f0f0f0")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20)

        # Load image button
        tk.Button(control_frame, text="Open Image", width=20, command=self.open_image).pack(pady=10)

        # Watermark text entry
        tk.Label(control_frame, text="Watermark Text:", bg="#f0f0f0").pack()
        self.text_entry = tk.Entry(control_frame, width=20)
        self.text_entry.pack(pady=5)

        tk.Button(control_frame, text="Add Text Watermark", width=20,
                  command=self.add_text_watermark).pack(pady=10)

        # Watermark logo
        tk.Button(control_frame, text="Load Logo", width=20,
                  command=self.open_logo).pack(pady=10)

        tk.Button(control_frame, text="Add Logo Watermark", width=20,
                  command=self.add_logo_watermark).pack(pady=10)

        # Save button
        tk.Button(control_frame, text="Save Image", width=20,
                  command=self.save_image).pack(pady=20)

        # Canvas to display image
        self.canvas = tk.Canvas(self.window, width=600, height=550, bg="white")
        self.canvas.pack(side=tk.RIGHT, padx=20)

    # ---- Open Main Image ----
    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if not file_path:
            return

        self.image = Image.open(file_path)
        self.show_image()

    # ---- Display Image on Canvas ----
    def show_image(self):
        if self.image is None:
            return

        img = self.image.copy()
        img.thumbnail((600, 550))
        self.image_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(300, 275, image=self.image_tk)

    # ---- Add Text Watermark ----
    def add_text_watermark(self):
        if self.image is None:
            messagebox.showerror("Error", "Load an image first.")
            return

        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "Enter watermark text.")
            return

        img = self.image.copy()
        draw = ImageDraw.Draw(img)

        # Select font
        font = ImageFont.truetype("arial.ttf", 40)

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = img.width - text_width - 20
        y = img.height - text_height - 20

        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

        self.image = img
        self.show_image()

    # ---- Load Logo ----
    def open_logo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if not file_path:
            return
        self.logo = Image.open(file_path).convert("RGBA")
        messagebox.showinfo("Logo Loaded", "Logo loaded successfully!")

    # ---- Add Logo Watermark ----
    def add_logo_watermark(self):
        if self.image is None:
            messagebox.showerror("Error", "Load an image first.")
            return

        if not hasattr(self, "logo"):
            messagebox.showerror("Error", "Load a logo first.")
            return

        img = self.image.copy()

        # Resize logo smaller
        logo = self.logo.copy()
        logo.thumbnail((img.width // 5, img.height // 5))

        # Position bottom-right
        x = img.width - logo.width - 20
        y = img.height - logo.height - 20

        img.paste(logo, (x, y), logo)
        self.image = img
        self.show_image()

    # ---- Save Final Image ----
    def save_image(self):
        if self.image is None:
            messagebox.showerror("Error", "Nothing to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
        )
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Saved", "Image saved successfully!")


# Run the app
window = tk.Tk()
app = WatermarkApp(window)
window.mainloop()
