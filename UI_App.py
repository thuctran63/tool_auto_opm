import tkinter as tk
import subprocess
from tkinter import font
import re
import tools_regacc_opm as tool

window = tk.Tk()
window.geometry("500x300")
window.title("Tools chơi game OPM server Trung")

# component ----------------------------------------------------------------
label = tk.Label(window, text = "Danh sách giả lập hiện tại", background="yellow",font= font.Font(weight= "bold", size= 12), borderwidth=1, relief= "solid")
label.grid(column= 0, row= 0)
button = tk.Button(window, text="Reload")
button.grid(column= 1, row= 0, padx= 10)

listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, width= 30)
listbox.grid(column=0, row= 1, sticky= "w")
btn_start = tk.Button(window,text = "Start", background="red",font= font.Font(weight= "bold", size= 10), borderwidth=1, relief= "solid", padx= 20)
btn_start.grid(column= 0, row=2, pady= 10, sticky= "w")


# function ----------------------------------------------------------------
def getListEmulator():
    path = r"C:\Users\vytra\AppData\Local\Android\Sdk\platform-tools\adb"
    result = subprocess.run([path, "devices"], capture_output=True, text=True)
    pattern = r"emulator-\d{4}"
    listbox.delete(0,tk.END)
    for i in re.findall(pattern, result.stdout):
        listbox.insert(tk.END,i)

def getEmulatorFromList():
    selections_index = listbox.curselection()
    return [listbox.get(index) for index in selections_index]

def startTools():
    list_devices = getEmulatorFromList()
    for name_device in list_devices:
        tool.start_tool(name_device)

# event --------------------------------
button.bind("<Button-1>", lambda a: getListEmulator())
btn_start.bind("<Button-1>", lambda a: startTools())
window.mainloop()

