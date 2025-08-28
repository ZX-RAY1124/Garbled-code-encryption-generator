import lib.coding

class code_mode:
    def code_mode(self):
        self.a = "你知道我是谁"
        self.i = 0
        with open("text.txt", "r", encoding="utf-8") as f:
            self.text = f.read()
        print("欢迎使用乱码加密系统")
        self.Coding = lib.coding.Coding
        self.codelists = ["GBK", "GB2312", "Shift-JIS", "Big5"]
        for code in self.codelists:
            print("{}:".format(self.i) + code)
            self.i = self.i + 1
        while True:
            try:
                self.coding = int(input("请选择输出编码:"))
            except ValueError:
                print("请输入数字")
                continue
            if self.coding >= len(self.codelists):
                print("超出选择范围，请在给出的范围内选择")
            else:
                break

        b = self.Coding(self.text, self.codelists[self.coding])
        b.initialtive()
        print(
            "\n""r"":替换\n""d"":删除（最好仅使用一次，会增大解密难度）\n""s"":输出至Output\n""q:""退出\n""v"":turn into English mode")

        self.keepgoing = True
        while self.keepgoing:
            self.answer = input("请输入接下来的操作:")
            if self.answer == "r":
                print("已替换")
                b.replace()
            elif self.answer == "d":
                print("已删除")
                b.delete()
            elif self.answer == "s":
                print("文本已输出至Output.txt")
                b.output()
            elif self.answer == "v":
                print("Turned into English mode\nPlese enter the index:")
                try:
                    self.index = int(input())
                    self.b.Caesar(self.index)
                except ValueError:
                    print("Plese enter a number")
                    continue

            elif self.answer == "q":
                self.keepgoing = False
            else:
                print("请输入正确的操作")
