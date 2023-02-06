class Person:
    li1 = []  # 클래스 변수

    def __init__(self, sp):
        self.li = []  # 인스턴스 변수
        self.li.append(sp)
        Person.li1.append(sp)

    def disp(self):
        print(self.li)
        print(self.li1)


p1 = Person('우유')
p1.disp()
p2 = Person('쥬스')
p2.disp()
p3 = Person('콜라')
p3.disp()
