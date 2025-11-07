import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖋️ Image Watermark Adder")
        self.image = None

        # UI Elements
        self.canvas = tk.Canvas(root, width=500, height=400, bg="gray")
        self.canvas.pack()

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=5)
        self.text_entry.insert(0, "Enter watermark text")

        self.add_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=5)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path).convert("RGBA")
            self.display_image(self.image)

    def display_image(self, img):
        img_resized = img.resize((500, 400))
        self.tk_img = ImageTk.PhotoImage(img_resized)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

    def add_watermark(self):
        if self.image:
            watermark_text = self.text_entry.get()
            watermark = self.image.copy()
            draw = ImageDraw.Draw(watermark)
            font = ImageFont.truetype("arial.ttf", 36)
            width, height = watermark.size
            draw.text((width - 250, height - 50), watermark_text, font=font, fill=(255, 255, 255, 128))
            self.image = watermark
            self.display_image(watermark)

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.image.save(file_path)
                print("✅ Image saved:", file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()