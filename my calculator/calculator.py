import tkinter
import math
import random
import pygame
import tkinter.messagebox
from tkinter import *
pygame.init()
button1_music = pygame.mixer.Sound("audio2/64.wav")
button2_music = pygame.mixer.Sound("audio2/65.wav")
button3_music = pygame.mixer.Sound("audio2/66.wav")
button4_music = pygame.mixer.Sound("audio2/67.wav")
button5_music = pygame.mixer.Sound("audio2/68.wav")
button6_music = pygame.mixer.Sound("audio2/69.wav")
button7_music = pygame.mixer.Sound("audio2/70.wav")
button8_music = pygame.mixer.Sound("audio2/71.wav")
button9_music = pygame.mixer.Sound("audio2/72.wav")
button0_music = pygame.mixer.Sound("audio2/73.wav")
game_music = pygame.mixer.Sound("audio2/bgm.wav")
class calculator:
    # 界面布局方法
    def __init__(self):
        # 创建主界面，并且保存到成员属性中
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('娱乐计算器')
        # 设置显式面板的变量
        self.result = tkinter.StringVar()
        self.result.set(0)
        self.result2 = tkinter.StringVar()
        self.result2.set(0)
        # 设置一个全局变量  运算数字和f符号的列表
        self.lists = []
        self.Lists2 = []
        # 添加一个用于判断是否按下运算符号的标志
        self.ispresssign = False
        # 界面布局
        photo = tkinter.PhotoImage(file="3.gif")
        bg = tkinter.Label(self.root,image = photo)
        bg.place(width=280, height=470)
        photo2 = tkinter.PhotoImage(file="timg.gif")
        bg2 = tkinter.Label(self.root,image = photo2)
        bg2.place(x=225, y=95, width=50, height=50)
        self.menus()
        self.page()
        self.root.mainloop()
    def menus(self):
            # 添加菜单
            # 创建总菜单
            allmenu = tkinter.Menu(self.root)
            # 添加子菜单
            filemenu = tkinter.Menu(allmenu, tearoff=0)
            # 添加选项卡
            filemenu.add_command(label='历史记录(Y)      Ctrl+H',
                                 command=self.lsjl)
            filemenu.add_command(label='标准型(T)            Alt+1',
                                 command=self.normal)
            filemenu.add_command(label='科学型(S)            Alt+2',
                                 command=self.kexue)
            # 添加分割线
            filemenu.add_separator()
            # 添加选项卡
            filemenu.add_command(label='统计信息(A)        Alt+4',
                                 command=self.myfunc)
            filemenu.add_command(label='数字分组(I)',
                                 command=self.myfunc)
            # 添加分割线
            filemenu.add_separator()
            # 添加选项卡
            filemenu.add_command(label='更换背景(B)             Ctrl+F4',
                                 command=self.myfunc)
            filemenu.add_command(label='单位转换(U)      Ctrl+U',
                                 command=self.myfunc)
            filemenu.add_command(label='日期计算(D)      Ctrl+E',
                                 command=self.myfunc)
            menu1 = tkinter.Menu(filemenu, tearoff=0)
            menu1.add_command(label='条形图(M)',
                              command=self.myfunc)
            menu1.add_command(label='扇形图(V)',
                              command=self.myfunc)
            menu1.add_command(label='柱状图(F)',
                              command=self.myfunc)
            menu1.add_command(label='折线图(U)',
                              command=self.myfunc)
            filemenu.add_cascade(label='工作表(W)',
                                 menu=menu1)
            allmenu.add_cascade(label='查看(V)',
                                menu=filemenu)

            # 添加子菜单2
            editmenu = tkinter.Menu(allmenu, tearoff=0)
            # 添加选项卡
            editmenu.add_command(label='复制(C)         Ctrl+C',
                                 command=self.copy)
            editmenu.add_command(label='粘贴(V)         Ctrl+V',
                                 command=self.paste)
            editmenu.add_command(label ='剪切          Ctrl+T',
                                 command = self.cut)
            editmenu.add_command(label='清除(L)    Ctrl+Shift+D',
                              command=self.c_c)
            editmenu.add_command(label='清除图形(N)    Ctrl+Shift+',
                              command=self.qctx)
            editmenu.add_command(label = '退出          Ctrl+T',
                                 command = self.root.quit)
            # 添加分割线
            editmenu.add_separator()
            # 添加选项卡
            menu2 = tkinter.Menu(filemenu, tearoff=0)
            editmenu.add_cascade(label='历史记录(H)', menu=menu2)
            allmenu.add_cascade(label='编辑(E)', menu=editmenu)
            menu2.add_command(label='复制历史记录(I)',
                              command=self.myfunc)
            menu2.add_command(label='编辑(E)                      F2',
                              command=self.myfunc)
            menu2.add_command(label='取消编辑(N)            Esc',
                              command=self.myfunc)
            menu2.add_command(label='清除(L)    Ctrl+Shift+D',
                              command=self.c_c)

            # 添加子菜单3
            helpmenu = tkinter.Menu(allmenu, tearoff=0)
            allmenu.add_cascade(label='帮助(H)',
                                menu=helpmenu)

            # 添加选项卡
            helpmenu.add_command(label='查看帮助(V)       F1',
                                 command=self.lookhelp)

            # 添加分割线
            helpmenu.add_separator()
            # 添加选项卡
            helpmenu.add_command(label='关于计算器(A)',
                                 command=self.aboutcalculator)
            self.root.config(menu=allmenu)

    # 计算器的主界面
    def page(self):
        # 显示屏
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root,bg = 'pink' ,font=('宋体', 20),
                                   anchor='e', textvariable=self.result)
        show_label.place(x=5, y=0, width=270, height=45)
        canvas = tkinter.Canvas(self.root,bg = 'pink' )
        x, y, x1, y1 = 1100, 500, 1500, 400
        line = canvas.create_line(x,y,x1,y1)

        canvas.place(x=5,y=50, width=270, height=45)
        # 按钮1
        bt1 = tkinter.Button(self.root, text='1',
                             command=lambda:self.pressnum('1'))
        bt1.place(x=5, y=315, width=50, height=50)
        # 按钮2
        bt2 = tkinter.Button(self.root, text='2',
                             command=lambda:self.pressnum('2'))
        bt2.place(x=60, y=315, width=50, height=50,)
        # 按钮3
        bt3 = tkinter.Button(self.root, text='3',
                             command=lambda:self.pressnum('3'))
        bt3.place(x=115, y=315, width=50, height=50)
        # 按钮4
        bt4 = tkinter.Button(self.root, text='4',
                             command=lambda:self.pressnum('4'))
        bt4.place(x=5, y=260, width=50, height=50)

        # 按钮5
        bt5 = tkinter.Button(self.root, text='5',
                             command=lambda:self.pressnum('5'))
        bt5.place(x=60, y=260, width=50, height=50)
        # 按钮6
        bt6 = tkinter.Button(self.root, text='6',
                             command=lambda:self.pressnum('6'))
        bt6.place(x=115, y=260, width=50, height=50)

        # 按钮7
        bt7 = tkinter.Button(self.root, text='7',
                             command=lambda:self.pressnum('7'))
        bt7.place(x=5, y=205, width=50, height=50)
        # 按钮8
        bt8 = tkinter.Button(self.root, text='8',
                             command=lambda:self.pressnum('8'))
        bt8.place(x=60, y=205, width=50, height=50)

        # 按钮9
        bt9 = tkinter.Button(self.root, text='9',
                             command=lambda:self.pressnum('9'))
        bt9.place(x=115, y=205, width=50, height=50)
        # 按钮0
        bt0 = tkinter.Button(self.root, text='0',
                             command=lambda:self.pressnum('0'))
        bt0.place(x=5, y=370, width=105, height=50)

        # 按钮.
        bt_point = tkinter.Button(self.root, text='.',
                                  command=lambda: self.pressnum('.'))
        bt_point.place(x=115, y=370, width=50, height=50)

        # 按钮+
        bt_plus = tkinter.Button(self.root, text='+'
                                 ,command=lambda: self.presscalculate('+'))
        bt_plus.place(x=170, y=370, width=50, height=50)
        # 按钮-
        bt_subtraction = tkinter.Button(self.root, text='-'
                                        ,command=lambda: self.presscalculate('-'))
        bt_subtraction.place(x=170, y=315, width=50, height=50)
        # 按钮*
        bt_multiplication = tkinter.Button(self.root, text='*'
                                           ,command=lambda: self.presscalculate('*'))
        bt_multiplication.place(x=170, y=260, width=50, height=50)
        # 按钮/
        bt_division = tkinter.Button(self.root, text='/'
                                     ,command=lambda: self.presscalculate('/'))
        bt_division.place(x=170, y=205, width=50, height=50)

        # 按钮%
        bt_remainder = tkinter.Button(self.root, text='%'
                                      ,command=lambda: self.presscalculate('%'))
        bt_remainder.place(x=225, y=205, width=50, height=50)

        # 画圆
        bt_mc = tkinter.Button(self.root, text='圆'
                               ,command = self.yuan)
        bt_mc.place(x=5, y=95, width=50, height=50)

        # 画线
        bt_mr = tkinter.Button(self.root, text='线'
                               ,command = self.xian)
        bt_mr.place(x=60, y=95, width=50, height=50)

        # 画方
        bt_ms = tkinter.Button(self.root, text='矩形'
                               ,command = self.rectangle)
        bt_ms.place(x=115, y=95, width=50, height=50)

        # 画椭圆
        bt_mjia = tkinter.Button(self.root, text='椭圆'
                                 ,command = self.polygon)
        bt_mjia.place(x=170, y=95, width=50, height=50)


        # 按钮←
        bt_zuo = tkinter.Button(self.root, text='←',
                                command = self.delet)
        bt_zuo.place(x=5, y=150, width=50, height=50)

        # 按钮CE
        bt_ce = tkinter.Button(self.root, text='CE',
                               command = lambda:self.result.set(0))
        bt_ce.place(x=60, y=150, width=50, height=50)

        # 按钮C
        bt_c = tkinter.Button(self.root, text='C'
                              ,command=self.c_c)
        bt_c.place(x=115, y=150, width=50, height=50)

        # 按钮±
        bt_zf = tkinter.Button(self.root, text='±'
                               ,command=self.zf)
        bt_zf.place(x=170, y=150, width=50, height=50)

        # 按钮√
        bt_kpf = tkinter.Button(self.root, text='√'
                                ,command=self.kpf)
        bt_kpf.place(x=225, y=150, width=50, height=50)

        # 功能按钮1/x
        bt_reciprocal = tkinter.Button(self.root, text='1/x',
                                       command=self.ds)
        bt_reciprocal.place(x=225, y=260, width=50, height=50)

        # 按钮=
        bt_equal = tkinter.Button(self.root, text='='
                                  , command=lambda: self.pressequal())
        bt_equal.place(x=225, y=315, width=50, height=105)


    def pressnum(self, num):
        # 全局化变量
        # 判断是否按下了运算符号
        if num =='1':
            button1_music.play()
        if num =='2':
            button2_music.play()
        if num =='3':
            button3_music.play()
        if num =='4':
            button4_music.play()
        if num == '5':
            button5_music.play()
        if num =='6':
            button6_music.play()
        if num =='7':
            button7_music.play()
        if num =='8':
            button8_music.play()
        if num =='9':
            button9_music.play()
        if num =='0':
            button0_music.play()

        if self.ispresssign == False:
            pass
        else:
            self.result.set(0)
            # 重置运算符号的状态
            self.ispresssign = False
        if num == '.':
            num = '0.'
        # 获取面板中的原有数字
        oldnum = self.result.get()
        # 判断界面数字是否为0
        if oldnum == '0':
            self.result.set(num)
        else:
            # 连接上新按下的数字
            newnum = oldnum + num
            # 将按下的数字写到面板中
            self.result.set(newnum)

    def presscalculate(self, sign):
        # 保存已经按下的数字和运算符号
        # 获取界面数字
        num = self.result.get()
        self.lists.append(num)
        # 保存按下的操作符号
        self.lists.append(sign)
        # 设置运算符号为按下状态
        self.ispresssign = True

    # 获取运算结果
    def pressequal(self):
        # 获取所有的列表中的内容
        # 获取当前界面上的数字
        curnum = self.result.get()
        # 将当前界面的数字存入列表
        self.lists.append(curnum)
        # 将列表转化为字符串
        calculatestr = ''.join(self.lists)
        # 使用eval执行字符串中的运算即可
        endnum = eval(calculatestr)

        # 将运算结果显示在界面中
        self.result.set(str(endnum)[:10])
        self.result2.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()

#添加负号
    def zf(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)

#√按键功能
    def kpf(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == '0':
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()

        # 1/x按键功能
    def ds(self):
        dsnum = 1 / int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
             self.ispresssign = True
             # 清空运算列表
             self.lists.clear()

#C按键功能,清除列表中储存的数字
    def c_c(self):
        self.lists.clear()
        self.result.set(0)

    # ←按键功能
    def delet(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    def lsjl(self):
        top = Toplevel()
        top.title('历史记录')
        top.minsize(200, 200)
        top.maxsize(200, 200)
        text1 = tkinter.Label(top,font=('宋体', 20),
                                   textvariable=self.result2)
        text1.place(x=5, y=5, width=270, height=45)

#计算器菜单功能
    def myfunc(self):
        tkinter.messagebox.showerror('error','正在维护')

    def lookhelp(self):
        tkinter.messagebox.showerror('查看','很多功能尚未实现，后续关注githubsxr597403122')

    def aboutcalculator(self):
        tkinter.messagebox.showinfo('关于','calculator0.1')

#复制功能
    def copy(self):
        top = Toplevel()
        top.title('copy')
        top.minsize(200, 200)
        top.maxsize(200, 200)
        text1 = tkinter.Text(top, font=('宋体', 20),)
        text1.place(x=5, y=5, width=270, height=45)
        text1.insert('insert',self.result2)
        text1.event_generate("<<Copy>>")

#剪切功能
    def cut(self):
        top = Toplevel()
        top.title('cut')
        top.minsize(200, 200)
        top.maxsize(200, 200)
        text1 = tkinter.Text(top, font=('宋体', 20),)
        text1.place(x=5, y=5, width=270, height=45)
        text1.insert('insert',self.result2)
        text1.event_generate("<<Cut>>")

#粘贴功能
    def paste(event=None):
        top = Toplevel()
        top.title('paste')
        top.minsize(200, 200)
        top.maxsize(200, 200)
        text1 = tkinter.Text(top, font=('宋体', 20),)
        text1.place(x=5, y=5, width=270, height=45)
        text1.event_generate("<<Paste>>")

#画圆
    def yuan(self):
        canvas = tkinter.Canvas(self.root, bg='white')
        x, y, x1, y1 = 110, 5, 150, 40
        oval = canvas.create_oval(x, y, x1, y1, fill='red')
        canvas.place(x=5,y=50, width=270, height=45)

#画线
    def xian(self):
        canvas = tkinter.Canvas(self.root, bg='white')
        x, y, x1, y1 = 110, 5, 150, 40
        line = canvas.create_line(x, y, x1, y1,fill = 'red')
        canvas.place(x=5, y=50, width=270, height=45)

#画矩形
    def rectangle(self):
        canvas = tkinter.Canvas(self.root, bg='white')
        x, y, x1, y1 = 110, 5, 150, 40
        rectangle = canvas.create_rectangle(x, y, x1, y1,fill = 'red')
        canvas.place(x=5, y=50, width=270, height=45)

#画椭圆
    def polygon(self):
        canvas = tkinter.Canvas(self.root, bg='white')
        x, y, x1, y1 = 110, 5, 150, 40
        rectangle = canvas.create_oval(70,5,200,40,fill = 'red')
        canvas.place(x=5, y=50, width=270, height=45)

    def qctx(self):
        canvas = tkinter.Canvas(self.root, bg='pink')
        x, y, x1, y1 = 110, 5, 150, 40
        line = canvas.create_line(x, y, x1, y1, fill='pink')
        canvas.place(x=5, y=50, width=270, height=45)
    def normal(self):
        top = Toplevel()
        top.title('标准计算器')
        top.minsize(150, 149)
        top.maxsize(200, 200)
        frm = Frame(top, bg='pink')  # 新建框架
        frm.pack(expand=YES, fill=BOTH)  # 放置框架
        display = StringVar()
        e = Entry(frm, textvariable=display)  # 添加输入框
        e.grid(row=0, column=0, sticky=N, columnspan=4, rowspan=2)  # 放置输入框位置

        def print_jia():
            e.insert(INSERT, '+')

        def print_jian():
            e.insert(INSERT, '-')

        def print_cheng():
            e.insert(INSERT, '*')

        def print_chu():
            e.insert(INSERT, '/')

        def print_dengyu():
            e.insert(INSERT, '=')

        Button(frm, text='1', width=3, bg='yellow', command=lambda: e.insert(INSERT, '1')).grid(row=2, column=0,
                                                                                                sticky=W)
        Button(frm, text='2', width=3, bg='yellow', command=lambda: e.insert(INSERT, '2')).grid(row=2, column=1)
        Button(frm, text='3', width=3, bg='yellow', command=lambda: e.insert(INSERT, '3')).grid(row=2, column=2)
        Button(frm, text='4', width=3, bg='yellow', command=lambda: e.insert(INSERT, '4')).grid(row=3, column=0,
                                                                                                sticky=W)
        Button(frm, text='5', width=3, bg='yellow', command=lambda: e.insert(INSERT, '5')).grid(row=3, column=1)
        Button(frm, text='6', width=3, bg='yellow', command=lambda: e.insert(INSERT, '6')).grid(row=3, column=2)
        Button(frm, text='7', width=3, bg='yellow', command=lambda: e.insert(INSERT, '7')).grid(row=4, column=0,
                                                                                                sticky=W, rowspan=2)
        Button(frm, text='8', width=3, bg='yellow', command=lambda: e.insert(INSERT, '8')).grid(row=4, column=1,
                                                                                                rowspan=2)
        Button(frm, text='9', width=3, bg='yellow', command=lambda: e.insert(INSERT, '9')).grid(row=4, column=2,
                                                                                                rowspan=2)
        Button(frm, text='/', width=4, bg='white', command=print_chu).grid(row=5, column=3, sticky=E)
        Button(frm, text='*', width=4, bg='white', command=print_cheng).grid(row=4, column=3, sticky=E)
        Button(frm, text='-', width=4, bg='white', command=print_jian).grid(row=3, column=3, sticky=E)
        Button(frm, text='+', width=4, bg='white', command=print_jia).grid(row=2, column=3, sticky=E)
        Button(frm, text='=', width=4, bg='white', command=lambda: cal(display)).grid(row=6, column=3, sticky=E)
        Button(frm, text='clear', width=3, bg='red', command=lambda: display.set('')).grid(row=6, column=0, sticky=W)
        Button(frm, text='0', width=3, bg='red', command=lambda: e.insert(INSERT, '0')).grid(row=6, column=2)
        Button(frm, text='.', width=3, bg='red', command=lambda: e.insert(INSERT, '.')).grid(row=6, column=1)
        def cal(display):
            display.set(eval(display.get()))
        print('OK')

    def kexue(self):
        top = Toplevel()
        top.title('科学计算器（假）')
        top.minsize(400, 400)
        top.maxsize(450, 450)
        game_music.play()
        number = random.randint(1, 100)
        label1 = tkinter.Label(top, fg='black', text="猜数字", font=('宋体', 35, 'bold'))
        label1.grid(padx=75)
        label2 = tkinter.Label(top, fg='black', text="游戏规则：\n从1到100中猜数字！！", font=('宋体', 15, 'bold'))
        label2.grid(padx=10, pady=10)
        label3 = tkinter.Label(top, fg='black', text="请输入你所猜测的数字：", font=('宋体', 15, 'bold'))
        label3.grid(padx=10, pady=10)
        text = tkinter.Entry(top, width=30)
        text.grid(padx=100)
        def compare():
            use = int(text.get())
            if use == '':
                tkinter.messagebox.showerror('警告', '输入不能空！！！')
            elif use > number:
                tkinter.messagebox.showinfo('不正确', '大了，老哥！')
            elif use < number:
                tkinter.messagebox.showinfo('不正确', '小了，老弟！')
            elif use == number:
                tkinter.messagebox.showinfo('正确', '哎呦，你咋这么聪明的呢！')
            else:
                tkinter.messagebox.showerror('警告', '输入不正确！！！')
        button1 = tkinter.Button(top, text='确定', command=compare, width=10, font=('微软雅黑', 10,))
        button1.grid(padx=10, pady=10)
        button2 = tkinter.Button(top, text='退出游戏', command=top.quit, width=10, bg='yellow', font=('微软雅黑', 10,))
        button2.grid(padx=10, pady=10)
mycalculator = calculator()




