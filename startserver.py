import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import subprocess
import os
import webbrowser

version_number = 'v1.0'


def start():
    messagebox.showinfo(message='伺服器正在開啟')
    if not os.path.exists('eula.txt'):
        with open('eula.txt', 'w+') as f:
            f.write('eula=true\n')
        f.close()
    if server_path.get() == '':
        messagebox.showerror(title='啟動錯誤', message='目錄不能為空')
    else:
        if java_path.get() == '':
            messagebox.showerror(title='啟動錯誤', message='目錄不能為空')
        else:
            t1 = (f"{java_path.get()} -jar -Xmx{Ram_Max.get()}M -Xms{Ram_Min.get()}M {server_path.get()} {gui_state.get()}")
            print(t1)
            if gui_state.get() == '0':
                messagebox.showinfo(message='請在cmd中管理伺服器')
                subprocess.Popen(f'"{java_path.get()}" -jar -Xmx{Ram_Max.get()}M -Xms{Ram_Min.get()}M "{server_path.get()}" nogui',
                                 shell=False,
                                 creationflags=subprocess.CREATE_NEW_CONSOLE
                                 )
            else:
                messagebox.showinfo(message='Minecraft Server 的圖形介面好像啟動得比較慢呢!')
                subprocess.Popen(f'"{java_path.get()}" -jar -Xmx{Ram_Max.get()}M -Xms{Ram_Min.get()}M "{server_path.get()}"', shell=True)


def select_server_path():

    server_path_ = filedialog.askopenfilename(title='選擇server.jar', initialdir='/', filetypes=(("Server.jar", "*.jar"), ("All Files","*.*")))
    server_path.set(server_path_)
    print(server_path.get())

def select_java_path():
    java_home = os.environ.get('JAVA_HOME')
    if java_home:
        initialdir = java_home
    else:
        initialdir = 'C:\\Program Files\\'
    java_path_ = filedialog.askopenfilename(title='選擇Java路徑', initialdir=initialdir, filetypes=(('java.exe','java.exe'),('All Files','*.*')))
    java_path.set(java_path_)
    print(java_path.get())

def settings():
    setup = tk.Toplevel(root)
    setup.title(f'Server Opening Helper {version_number} - Settings')
    def ok():
        Ram_Max.set(f'{RX.get()}')
        Ram_Min.set(f'{RL.get()}')
        if GUI_Enable.get() == 'Enable':
            gui_state.set('1')
        else:
            gui_state.set('0')
        if server_path.get() == '':
            messagebox.showerror(title='設定錯誤', message='路徑不能為空 (Server Path Err)')
        else:
            if java_path.get() == '':
                messagebox.showerror(title='設定錯誤', message='路徑不能為空 (Java Path Err)')
            else:
                setup.destroy()
    tk.Label(setup, text='伺服器路徑', font=('微軟正黑體', 12)).grid(row=0, column=0)
    tk.Entry(setup, font=('微軟正黑體', 12), textvariable=server_path).grid(row=0, column=1)
    tk.Button(setup, text='...', font=('微軟正黑體', 12), command=select_server_path).grid(row=0, column=2)
    tk.Label(setup).grid(row=1)
    tk.Label(setup, text='Java路徑', font=('微軟正黑體', 12)).grid(row=2, column=0)
    tk.Entry(setup, font=('微軟正黑體', 12), textvariable=java_path).grid(row=2, column=1)
    tk.Button(setup, text='...', font=('微軟正黑體', 12), command=select_java_path).grid(row=2, column=2)
    tk.Label(setup).grid(row=3)
    tk.Label(setup, text='記憶體上限', font=('微軟正黑體', 12)).grid(row=4, column=0)
    RX = ttk.Combobox(setup, font=('微軟正黑體', 12), values=['512','1024','2048','4096','8192','16384','32768'])
    RX.grid(row=4, column=1)
    RX.set(Ram_Max.get())
    tk.Label(setup, text='記憶體下限', font=('微軟正黑體', 12)).grid(row=5, column=0)
    RL = ttk.Combobox(setup, font=('微軟正黑體', 12), values=['0','512','1024','2048','4096','8192','16384'])
    RL.grid(row=5, column=1)
    RL.set(Ram_Min.get())
    tk.Label(setup, text='啟用伺服器GUI?', font=('微軟正黑體', 12)).grid(row=6, column=0)
    GUI_Enable = ttk.Combobox(setup, values=['Enable','Disable'], font=('微軟正黑體', 12))
    GUI_Enable.grid(row=6, column=1)
    GUI_Enable.set('Disable')
    tk.Button(setup, text='確定', font=('微軟正黑體', 12), command=ok).grid(row=7, column=1)
    setup.wait_window()

def Version():
    information = tk.Toplevel()
    information.title(f'Server Opening Helper {version_number} - Version Information')
    information.geometry('140x170')

    def exit_Version():
        information.destroy()

    def open_link():
        webbrowser.open('https://github.com/TsaiTou2926/Server-opening-helper')

    tk.Label(information, text=f'Version:{version_number}').grid()
    tk.Label(information).grid()
    Github_link = tk.Label(information, text='Github', fg='blue', cursor='hand2')
    Github_link.grid()
    Github_link.bind("<Button-1>", lambda event: open_link())
    tk.Label(information).grid()
    tk.Label(information, text='Tsaitou Studios @ 2023').grid()
    tk.Label(information).grid()
    tk.Button(information, text='確認', command=exit_Version).grid()
    information.wait_window()


def exit_main():
    que = messagebox.askokcancel(message='確定離開?')
    if que:
        root.destroy()

root = tk.Tk()
root.title(f'Server Opening Manager {version_number}')
root.geometry('400x300')
menu = tk.Menu(root)

server_path = tk.StringVar()
java_path = tk.StringVar()
Ram_Max = tk.StringVar()
Ram_Min = tk.StringVar()
gui_state = tk.StringVar()

menubar = tk.Menu(menu)
menubar.add_command(label='設定', command=settings)
menubar.add_command(label='離開', command=exit_main)
menu.add_cascade(label='檔案', menu=menubar)

menubar2 = tk.Menu(menu)
menubar2.add_command(label='資訊', command=Version)
menu.add_cascade(label='編輯', menu=menubar2)

root.config(menu=menu)


tk.Label(root).grid()
tk.Label(root,text=' 警告:請務必將此檔案放置在伺服器目錄下，否則會故障' , font=('微軟正黑體', 12), fg='red').grid(row=1, column=0)
tk.Label(root).grid()
tk.Label(root).grid()
tk.Button(root, text='啟動', font=('微軟正黑體', 12), width=15, height=3, command=start).grid()

root.mainloop()