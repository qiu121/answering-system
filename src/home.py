from tkinter import Frame, Label, Button, Tk, messagebox, LEFT, StringVar

from db import Database


class Widgets:
    def __init__(self, window):
        """初始化"""

        self.str = StringVar()  # StringVar()是为了让Label控件可以显示变化的题目
        self.window = window
        self.num = 1  # 记录当前题号,全局变量，整个类共享
        self.btn = None  # 下一题的按钮，必要时设置为不可点击

        screenwidth = window.winfo_screenwidth()  # 屏幕宽度
        screenheight = window.winfo_screenheight()  # 屏幕高度
        width = 900  # 设置窗口宽度
        height = 600  # 设置窗口高度
        # 获取屏幕分辨率，使窗口居中显示
        # 横向的屏幕分辨率减去窗口宽度的一半，等于让窗口居中显示的偏移量(就是窗口距离屏幕左边的距离)
        # 纵向类推
        x = (screenwidth - width) // 2
        y = (screenheight - height) // 2
        window.geometry('%dx%d+%d-%d' % (width, height, x, y))  # 设置窗口大小及坐标
        window.configure(background="white")  # 设置背景颜色
        window.title("简易答题系统")  # 设置窗口标题
        window.attributes("-alpha", 0.8)  # 设置窗口透明度,数值越小越透明
        window.resizable(False, False)  # 窗口大小不可变

        self.main_page()

    def main_page(self):
        """主界面"""
        # question = self.question
        # 上面答题区域显示容器
        frame_top = Frame(self.window, width=700, height=460, bd=1, relief='groove')
        frame_top.pack_propagate(0)
        frame_top.pack()
        Label(frame_top, textvariable=self.str, font=('宋体', 14),  # bg='white',
              fg='blue', justify=LEFT, wraplength=650).pack()  # bg='white'
        # wrap length将Label显示的文本分行，该参数指定了分行后每一行的长度

        ###################################################################################

        # 下面按钮区域显示容器
        frame_bottom = Frame(self.window, width=700, height=100, bd=1, relief='groove')
        frame_bottom.place(x=100, y=470, height=90)

        offset_x = 60  # 按钮间距偏移量
        btn_x = 100  # 按钮宽度
        btn = [0, 0, 0, 0, 0]
        # # 左一按钮
        # next_ = Button(frame_bottom, text='第一题', font='黑体', width=10, height=1, activebackground='pink',
        #                # command=self.show_question(),
        #                cursor='hand2')
        # next_.place(width=100, height=70, x=60, y=10)
        # # 左二按钮
        # next_ = Button(frame_bottom, text='下一题', font='黑体', width=10, height=1, activebackground='pink',
        #                # command=self.login,
        #                cursor='hand2')
        # next_.place(width=100, height=70, x=(offset_x * 2) + button_x, y=10)
        #
        # # 右二按钮
        # next_ = Button(frame_bottom, text='下一题', font='黑体', width=10, height=1, activebackground='pink',
        #                # command=self.login,
        #                cursor='hand2')
        # next_.place(width=100, height=70, x=(offset_x * 3) + (button_x * 2), y=10)
        #
        # # 右一按钮
        # next_ = Button(frame_bottom, text='下一题', font='黑体', width=10, height=1, activebackground='pink',
        #                # command=self.login,
        #                cursor='hand2')
        # next_.place(width=100, height=70, x=(offset_x * 4) + (button_x * 3), y=10)

        # 循环布局Button控件
        text = ['第一题', '下一题', '显示答案', '上一题']
        for i in range(1, len(text) + 1):
            btn[i] = Button(frame_bottom, text=text[i - 1], font=('宋体', 15),
                            width=10, height=1, cursor='hand2')
            btn[i].place(width=100, height=70, x=(offset_x * i) + (btn_x * (i - 1)), y=10)
            btn[i].bind('<Button-1>', self.btn_click)
        messagebox.showwarning("警告", "为确保程序正常启动，请务必在良好网络环境下启动！！！")

    def btn_click(self, event):
        """按钮点击事件"""
        # 调用模块中的类，实现功能
        if event.widget['text'] == '第一题':
            self.num = 1
            db = Database()
            question = db.query_question(self.num)
            self.str.set(question)
            messagebox.showinfo('提示', '没有查询到该题号对应的题目\n\t当前题号 %d' % self.num)
        if event.widget['text'] == '下一题':
            self.num += 1
            db = Database()
            question = db.query_question(self.num)
            self.str.set(question)

            next_ = db.question_id()
            if self.num not in next_:
                messagebox.showinfo("提示", "未查询到该题\n当前题号 %d" % self.num)

            # if db.query_answer(self.num) is None:
            #     self.btn[2]["status"] = ACTIVE

        if event.widget['text'] == '显示答案':
            db = Database()
            ans = db.query_answer(self.num)
            # 未查询到数据,不设定返回值，直接返回None
            if ans is not None:
                messagebox.showinfo("答案", ans)
        if event.widget['text'] == '上一题':
            if self.num > 1:
                self.num -= 1
                db = Database()
                question = db.query_question(self.num)
                self.str.set(question)
            else:
                messagebox.showinfo("提示", "当前已为第一题")


if __name__ == '__main__':
    """测试代码"""
    root = Tk()
    Widgets(root)
    root.mainloop()
