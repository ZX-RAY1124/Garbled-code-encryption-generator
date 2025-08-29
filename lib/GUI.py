import tkinter as tk
from lib.coding import *
from tkinter import messagebox
from tkinter import ttk
from code_mode import *


class GUI(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.center_window(self.root, 600, 350)
        self.root.resizable(width=False, height=False)
        self.root.title("乱码加密系统")
        self.section_1 = tk.LabelFrame(self.root,text="待转化文本",padx=10, pady=0)
        self.section_2 = tk.LabelFrame(self.root,text="转换编码选择",padx=10, pady=5)
        self.section_3 = tk.LabelFrame(self.root,text="操作",padx=2, pady=5)
        self.section_4 = tk.LabelFrame(self.root,text="操作预览",padx=2, pady=5)
        self.coding = ""
        self.CAESAR_MODE = False
        self.CODE_MODE = True
        self.root.iconbitmap("code.ico")

        self.frame_1 = tk.Frame(self.section_3)
        self.frame_2 = tk.Frame(self.section_3)
        self.frame_1.pack()
        self.frame_2.pack()
        # Control
        self.label_0 = tk.Label(self.root, text="乱码加密系统 v1.0")
        self.label_1 = tk.Label(self.section_1,text="所有操作均不可撤销",anchor='w', justify='left',highlightcolor='red',font=("微软雅黑",10 ,"bold"))
        self.label_2 = tk.Label(self.section_2,text="纯英文文本请选择Caesar")
        self.label_intro = tk.Label(self.root,text="欢迎使用乱码加密系统，对于utf-8文本，可以对16进制进行特定操作，然后用另外一种编码进行读取生成乱码\n对于英文文本，使用凯撒密码进行加密生成乱码       Credits: Program made by ZX_RAYER",anchor='w', justify='left')
        self.button_1 = tk.Button(self.section_1,text="从text中读取",width=10,height=1,command=self.readfromtext)
        self.button_2 = tk.Button(self.section_1, text="清除", width=10, height=1,command=self.clear)



        self.button_3 = tk.Button(self.frame_1,text="替换", width=10, height=1,command=self.replace)
        self.button_4 = tk.Button(self.frame_1, text="删除", width=10, height=1,command=self.delete)
        self.button_5 = tk.Button(self.frame_1, text="输出", width=10, height=1,command=self.c_out)
        self.button_6 = tk.Button(self.section_1,text="确定", width=10, height=1,command=self.init)
        self.button_3.config(state=tk.DISABLED)
        self.button_4.config(state=tk.DISABLED)
        self.button_5.config(state=tk.DISABLED)


        self.label_3 = tk.Label(self.frame_2,text="偏移量（凯撒模式）:")
        self.entry_1 = tk.Entry(self.frame_2, width=2,justify='left')


        self.text_1 = tk.Text(self.section_1, width=40,height=17)
        self.text_2 = tk.Text(self.section_4, width=30,height=9)

        self.combobox = ttk.Combobox(self.section_2, width=10, height=6, values=['GBK','Shift-JIS','GB2312','Big-5','Caesar','code mode'])

        with open("text.txt","r",encoding="utf-8") as f:
            self.txt = f.readline()
            self.text_1.insert(tk.INSERT,self.txt)
        # Pack
        self.label_intro.place(relx=0.5, rely=0.94, anchor="center")
        self.section_1.place(relx=0.28, rely=0.45, anchor="center")
        self.section_2.place(relx=0.77, rely=0.1, anchor="center")
        self.section_3.place(relx=0.77, rely=0.3, anchor="center")
        self.section_4.place(relx=0.77, rely=0.65, anchor="center")
        self.label_1.pack(side="top")

        self.text_1.pack(side="top")
        self.button_1.pack(side="left",expand=True)


        self.combobox.pack(side="left",expand=True)
        self.label_2.pack(side="top")
        self.label_3.pack(side="left", expand=True)
        self.button_3.pack(side="left",expand=True,padx=2)
        self.button_4.pack(side="left", expand=True,padx=2)
        self.button_5.pack(side="left", expand=True,padx=2)
        self.button_2.pack(side="left",expand=True,padx=2)
        self.button_6.pack(side="left", expand=True)
        self.entry_1.pack(side="left")
        self.text_2.pack(expand=True)


        self.combobox.bind("GBK",self.opt_GBK())
        self.combobox.bind("Shift-JIS",self.opt_ShiftJIS())



    def show(self):
        self.root.mainloop()

    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)
        print(size)



    def readfromtext(self):
        with open("text.txt","r",encoding="utf-8") as f:
            self.txt = f.readline()
            self.text_1.delete("1.0",tk.END)
            self.text_1.insert(tk.INSERT,self.txt)
    def cmd_mode(self):
        self.root.destroy()
        code_mode().code_mode()


    def init(self):
        self.text = self.text_1.get("1.0", tk.END)
        if messagebox.askyesno("是否确认？","确认后文本将无法更改"):
            if str(self.text) == 'code_mode\n':
                messagebox.showinfo("信息","您已切换至命令行模式")
                self.cmd_mode()
                return 0
            if self.combobox.get() == "":
                messagebox.showerror("错误","请先确认编码")

            elif self.combobox.get() == "Caesar":
                messagebox.showinfo("信息","您已选择凯撒密码加密")
                self.text_2.insert(tk.INSERT,"Caesar mode")
                self.text_1.config(state=tk.DISABLED)
                self.button_1.config(state=tk.DISABLED)
                self.button_2.config(state=tk.DISABLED)
                self.button_3.config(state=tk.DISABLED)
                self.button_4.config(state=tk.DISABLED)
                self.button_6.config(state=tk.DISABLED)
                self.combobox.config(state=tk.DISABLED)
                self.main = Coding(self.text_1.get(1.0, tk.END), self.coding)
                self.main.initialtive()
                self.CAESAR_MODE = True
            else:
                self.text_1.config(state=tk.DISABLED)
                self.combobox.config(state=tk.DISABLED)
                self.button_1.config(state=tk.DISABLED)
                self.button_2.config(state=tk.DISABLED)
                self.button_6.config(state=tk.DISABLED)
                self.button_3.config(state=tk.NORMAL)
                self.button_4.config(state=tk.NORMAL)
                self.button_5.config(state=tk.NORMAL)
                self.main = Coding(self.text_1.get(1.0, tk.END),self.coding)
                self.main.initialtive()
    def clear(self):
        self.text_1.delete("1.0", tk.END)
    def replace(self):
        try:
            self.a = self.main.replace()
            self.text_2.insert("1.0", self.a + "\n")
        except Exception:
            messagebox.showerror("错误","请先确定文本")
    def delete(self):
        try:
            self.a = self.main.delete()
            self.text_2.insert("1.0", self.a + "\n")
        except Exception:
            messagebox.showerror("错误","请先确定文本")
    def c_out(self):
        if self.CAESAR_MODE:
            try:
                self.main.Caesar(int(self.entry_1.get()))
                self.CAESAR_MODE = False
                self.output()
                self.text_2.delete("1.0", tk.END)
                self.reinit()
                return 0
            except ValueError:
                messagebox.showerror("错误", "请输入偏移量(偏移量仅能为整数)")
                self.reinit()
                self.CAESAR_MODE = False
                return 0
        try:
            self.reinit()
            self.main.output()
            self.output()

            return 0

        except Exception as e:
            messagebox.showerror("错误","请先进行操作后输出")
            print(e)

    def output(self):
        messagebox.showinfo("信息", "文本已输出至text.txt")
        self.form_1 = tk.Tk()
        self.center_window(self.form_1, 400, 250)
        self.text_3 = tk.Text(self.form_1,font=("微软雅黑",10))
        with open("Output.txt", "r", encoding="utf-8") as f:
            self.read = f.read()
            self.text_3.insert("1.0", self.read + "\n")
            f.close()
        self.form_1.title("文本展示")
        self.text_3.pack(side="top")
        self.text_2.delete("1.0", tk.END)
        self.form_1.mainloop()

    def reinit(self):
        self.combobox.config(state=tk.NORMAL)
        self.text_1.config(state=tk.NORMAL)
        self.button_1.config(state=tk.NORMAL)
        self.button_2.config(state=tk.NORMAL)
        self.button_3.config(state=tk.DISABLED)
        self.button_4.config(state=tk.DISABLED)
        self.button_5.config(state=tk.DISABLED)
        self.button_6.config(state=tk.NORMAL)

    def opt_GBK(self): self.coding = "GBK"
    def opt_ShiftJIS(self): self.coding = "Shift-JIS"
    def opt_GB2312(self): self.coding = "GB2312"
    def opt_BIG5(self): self.coding = "Big5"







