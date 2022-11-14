from tkinter import Tk
from home import Widgets

if __name__ == '__main__':
    window = Tk()
    Widgets(window)
    window.mainloop()  # 循环事件，始终保留窗口
