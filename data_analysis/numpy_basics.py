import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1️⃣ Create and explore ndarrays
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", a)
print("Shape:", a.shape)
print("Access [1,2]:", a[1, 2])

# 2️⃣ Broadcasting
b = np.array([10, 20, 30])
broadcasted = a + b
print("Broadcasted Addition:\n", broadcasted)

# 3️⃣ Linear Algebra
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
product = np.dot(m1, m2)
print("Matrix Product:\n", product)

# 4️⃣ Generate points for plotting
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.title("📈 Sine Wave with NumPy")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.legend()
plt.show()

# 5️⃣ Image manipulation
try:
    img = Image.open("image.jpg")
    img_array = np.array(img)
    print("Image shape:", img_array.shape)

    # Flip image vertically
    flipped = np.flipud(img_array)

    # Show original and flipped
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_array)
    axs[0].set_title("Original")
    axs[1].imshow(flipped)
    axs[1].set_title("Flipped")
    plt.show()
except FileNotFoundError:
    print("🖼️ No image found. Add 'image.jpg' to try image manipulation.")