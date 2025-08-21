import random

class Coding:

    def __init__(self,code,coding):
        self.z = None
        self.code = code
        self.coding = coding
        self.transform = b''
        self.final = str()
        self.MIDDLE = b"??"
        self.ERROR = b'?'
        self.changedlist = []
        print("文本："+self.code)
    def replace(self):
        self.id = self.coded[random.randint(0, len(self.coded))-1]
        self.id_1 = self.coded[random.randint(0,len(self.coded))-1]
        self.coded = self.coded.replace(self.id_1.to_bytes(), self.MIDDLE)
        self.coded = self.coded.replace(self.id.to_bytes(), self.id_1.to_bytes())
        self.coded = self.coded.replace(self.MIDDLE, self.id.to_bytes())
        self.changedlist.append(str(self.id.to_bytes()) + " <-> " + str(self.id_1.to_bytes()))
        return self.coded

    def delete(self):
        self.id = self.coded[random.randint(0, len(self.coded)) - 1]
        self.coded = self.coded.replace(self.id.to_bytes(), self.ERROR)
        self.changedlist.append(str(self.id.to_bytes()) + " -> " + "?")
        return self.coded

#使用前必须先调用initialtive方法
    def initialtive(self):
        self.coded = self.code.encode("utf-8")

    def output(self):
        self.final = self.coded.decode(self.coding, errors="replace")
        self.data = ''.join(format(i, '08b') for i in self.coded)
        print(self.final)
        print(self.coded)
        for i in self.changedlist: print(i)
        with open("Output.txt", "w", encoding="utf-8") as f:
            f.writelines(self.final+"\n")
            for i in self.changedlist: f.write("{}\n".format(i))
            f.write("utf-8 -> {}\n".format(self.coding))
            f.write("防数据丢失比对："+self.data)
    #English Only
    def Caesar(self,index):
        self.index = index
        try:
            self.code = self.code.upper()
        except Exception as e:
            print(e)
            print("Your word is not pure English,PLease try again")
        self.coded = self.code.encode("ASCII")
        print(self.coded)
        #65 -> 90
        for self.i in self.coded:
            self.z = int(self.i) + self.index
            if self.z > 90:
                self.z = (self.z - 90) + 64
            elif self.z == self.index + 32 or self.z == self.index + 46 or self.z == self.index + 44:
                self.z = self.z - self.index
            self.transform = self.transform + self.z.to_bytes(1, "little")
        print(self.transform)
        with open(f"Output.txt", "w", encoding="utf-8") as f:
            f.write(self.transform.decode("ASCII") + "\nIndex:{}".format(self.index))




