import lib.coding
a = "你知道我是谁"
i = 0
with open("text.txt","r",encoding="utf-8") as f:
    text = f.read()
print("欢迎使用乱码加密系统")
Coding = lib.coding.Coding
codelists = ["GBK","GB2312","Shift-JIS","Big5"]
for code in codelists:
    print("{}:".format(i) + code)
    i = i + 1
while True:
    try:
        coding = int(input("请选择输出编码:"))
    except ValueError:
        print("请输入数字")
        continue
    if coding >= len(codelists):
        print("超出选择范围，请在给出的范围内选择")
    else: break

b = Coding(text, codelists[coding])
b.initialtive()
print("\n""r"":替换\n""d"":删除（最好仅使用一次，会增大解密难度）\n""s"":输出至Output\n""q:""退出\n""v"":turn into English mode")

keepgoing = True
while keepgoing:
    answer = input("请输入接下来的操作:")
    if answer == "r":
        print("已替换")
        b.replace()
    elif answer == "d":
        print("已删除")
        b.delete()
    elif answer == "s":
        print("文本已输出至Output.txt")
        b.output()
    elif answer == "v":
        print("Turned into English mode\nPlese enter the index:")
        try:
            index = int(input())
            b.Caesar(index)
        except ValueError:
            print("Plese enter a number")
            continue

    elif answer == "q":
        keepgoing = False
    else:
        print("请输入正确的操作")



