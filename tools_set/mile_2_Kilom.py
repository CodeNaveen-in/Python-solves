import tkinter as tk

def convert():
    miles = float(entry.get())
    km = round(miles * 1.60934, 2)
    result_label.config(text=f"{km}")

# Set up window
window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry for miles
entry = tk.Entry(width=10)
entry.grid(column=1, row=0)

# Labels
mile_label = tk.Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = tk.Button(text="Convert", command=convert)
button.grid(column=1, row=2)

# Run the app
window.mainloop()