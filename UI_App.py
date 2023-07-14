import threading
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import font
import re
import tools_regacc_opm as tool
from tkinter import messagebox


WITH_COMPONENT = 50
HEIGHT_COMPONENT = 50 
window = tk.Tk()
window.geometry("500x300")
window.title("Tools chơi game OPM server Trung")

# component ----------------------------------------------------------------
label_list_devices = tk.Label(window, text = "Danh sách giả lập hiện tại", background="yellow",font= font.Font(weight= "bold", size= 12), borderwidth=1, relief= "solid")
label_list_devices.grid(column= 0, row= 0)

label_list_threads = tk.Label(window, text = "Danh sách luồng đang chạy", background="yellow",font= font.Font(weight= "bold", size= 12), borderwidth=1, relief= "solid")
label_list_threads.grid(column= 3, row= 0, sticky="w")

button = tk.Button(window, text="Reload")
button.grid(column= 1, row= 0, padx= 10)

listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, width= 31)
listbox.grid(column=0, row= 1, sticky= "nw")

treeView_threads = ttk.Treeview(window, columns= ("name_thread", "status"), show= "headings", height= 7)
treeView_threads.heading("name_thread", text="Tên luồng")
treeView_threads.heading("status", text="Trạng thái")
treeView_threads.column("name_thread", width=130)
treeView_threads.column("status", width=90)
treeView_threads.grid(column=3, row= 1, sticky= "w")

btn_start = tk.Button(window,text = "Start", background="red",font= font.Font(weight= "bold", size= 10), borderwidth=1, relief= "solid", padx= 20)
btn_start.grid(column= 0, row=2, pady= 10, sticky= "w")



# function ----------------------------------------------------------------
def show_message(mess):
    messagebox.showinfo("Thong bao", mess)

def getListEmulator():
    path = r"C:\Users\vytra\AppData\Local\Android\Sdk\platform-tools\adb"
    result = subprocess.run([path, "devices"], capture_output=True, text=True)
    pattern = r"emulator-\d{4}"
    listbox.delete(0,tk.END)
    for i in re.findall(pattern, result.stdout):
        listbox.insert(tk.END,i)

def getEmulatorFromList(listbox_):
    selections_index = listbox.curselection()
    return [listbox_.get(index) for index in selections_index]

def startTools(name):
    try:
        window.after(0, show_message, "Thanh Cong")
        tool.start_tool(name)
    except:
        pass

def create_thread():
    list_devices = getEmulatorFromList(listbox)
    for name_device in list_devices:
        thread = threading.Thread(target= startTools, args=(name_device,))
        thread.start()
        thread.name = "Thread: " + name_device
        status = "Alive" if thread.is_alive() else "Dead"
        treeView_threads.insert("", "end", values= (thread.name, status))

def find_thread(name):
    for thread in threading.enumerate():
        if thread.name == name:
            return thread

def update_status_of_thread():
    for thread in threading.enumerate():
        status = "Alive" if thread.is_alive() else "Dead"
        index = treeView_threads.index(thread.name)
        treeView_threads.item(treeView_threads.get_children("")[index], values=(thread.name, status))


# event --------------------------------

button.bind("<Button-1>", lambda a: getListEmulator())
btn_start.bind("<Button-1>", lambda a: create_thread())
window.after(10, update_status_of_thread)
window.mainloop()

