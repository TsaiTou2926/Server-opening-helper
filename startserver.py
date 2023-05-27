import tkinter as tk
from tkinter import messagebox, filedialog
from os import system
from os.path import isfile


def start():
    messagebox.showinfo(message='伺服器正在開啟')
    messagebox.showinfo(message='請在cmd中管理伺服器')
    if isfile('eula.txt'):
        f = open('eula.txt', 'w+')
        f.write('eula=true\n')
        f.close()
    if path.get() == '':
        messagebox.showerror(title='啟動錯誤', message='目錄不能為空')
    else:
        system(f"java -jar -Xmx2048M -Xms512M {path.get()} nogui")

def select_path():
    path_ = filedialog.askopenfilename(title='選擇server.jar', filetypes=(("Server.jar","*.jar"),("All files,*.*")))
    path.set(path_)
    print(path)

def exit_main():
    que = messagebox.askokcancel(message='確定離開?')
    if que:
        root.destroy()

root = tk.Tk()
root.title('Server Opening Manager v0.1')
root.geometry('400x300')

path = tk.StringVar()

tk.Label(root).pack()
tk.Label(root,text='警告:請將此檔案放置在伺服器目錄下，否則會故障' , font=('微軟正黑體', 12), fg='red').pack()
tk.Label(root, text='啟動路徑:', font=('微軟正黑體', 12)).pack(padx=2, pady=0)
tk.Entry(root, textvariable=path, width=50).pack(padx=2, pady=1)
tk.Button(root, text='指定server.jar路徑', font=('微軟正黑體', 12), command=select_path).pack(padx=2, pady=2)
tk.Label(root).pack()
tk.Button(root, text='Start', font=('微軟正黑體', 12), width=15, height=3, command=start).pack()
tk.Label(root).pack()
tk.Button(root, text='離開', font=('微軟正黑體', 12), command=exit_main).pack()


root.mainloop()