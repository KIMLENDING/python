class Sj:
    def __init__(self):
        self.kor = 90
        self.__eng = 59  # __ 접근 제한
        self.math = 64

    def disp(self):
        print(self.__eng)  # __를 사용하면 클래스 안에서는 접근 가능 그러면 클래스 밖에서는 disp로만 eng에 접근 할 수 있다.

    def geteng(self):
        return self.__eng

    def seteng(self, eng):
        self.__eng = eng


sj = Sj()
print(sj.math)
sj.disp()
sj.seteng(100)
print(sj.geteng())
