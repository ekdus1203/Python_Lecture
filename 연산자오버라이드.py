#연산자 오버라이드 
class NumBox:
	#초기화
	def __init__(self, num):
		self.Num = num
	#+연산자 ==> 일반 인스턴스 메서드
	def __add__(self, num):
		self.Num += num
	#-연산자
	def __sub__(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(100) 
print(n.Num)
n.remove(110)
print(n.Num)

#인스턴스 생성
#n = NumBox(40)
#n + 100 
#print(n.Num)
#n - 110 
#print(n.Num)

