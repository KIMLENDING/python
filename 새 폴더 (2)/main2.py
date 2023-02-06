class Person:
    def __init__(self):  # 초기자  속성
        self.name = input('이름:')  # 인스턴스변수 = 매개변수
        self.age = int(input('나이:'))

    def disp(self):  # 합수
        print(self.name + ' ' + str(self.age))


li = []
for i in range(3):
    li.append(Person())

for i in li:
    i.disp()


