#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그가 발생~~ 
        #print(str)
        print(self.str) #으로 수정함

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
