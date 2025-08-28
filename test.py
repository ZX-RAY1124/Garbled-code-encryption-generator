'''
a = '浠庝粖尋╄捣铼邃綘瑕亴仛涓�涓紝垢绂忕殑浜猴�邃笉尶厡湪鎰忎粬浜虹殑璇借挨寬鍖槻绗戯�鍖仛浣犺嚰尫憋�邃綘鏄�鐙�涓�鏃犱哄鐨剬厜'
a = a.encode("GBK","replace")
print(a)
b = "从今天起，你要做一个幸福的人，不必在意他人的诽谤和嘲笑，做你自己，你是独一无二的光".encode("utf-8","replace")
print(b)
c = b'DRSC DSWO S LVYYW'
print(str(c))
'''
import tkinter
import tkinter as tk
from hmac import compare_digest

# 创建主窗口
root = tk.Tk()
root.title("Tkinter LabelFrame with Place Layout")
root.geometry("400x300")
def ok():
    a = text.get("1.0", tk.END)
    b = "idle\n"
    print(a == b)
text = tkinter.Text(root)
button = tkinter.Button(root,command=ok)
text.pack()
button.pack()
root.mainloop()