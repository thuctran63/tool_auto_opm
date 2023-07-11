import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Danh sách có thể chọn được")

# Tạo Listbox
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
listbox.pack()

# Thêm mục vào Listbox
items = ["Mục 1", "Mục 2", "Mục 3", "Mục 4", "Mục 5"]
for item in items:
    listbox.insert(tk.END, item)

window.mainloop()
