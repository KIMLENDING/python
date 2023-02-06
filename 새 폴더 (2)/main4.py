class Person:
    def __init__(self):
        self.name = '홍길동'
        self.age = 25

    def say(self):
        print()


class Koren(Person):  # 상속
    def __init__(self):
        super().__init__()
        self.lang = '한국어'

    def say(self):  # 부모와 자식이 같은 메소드가 있다면 자식의 메소드를 사용한다 -- 오버라이딩
        print('안녕')


class Japen(Person):  # 상속
    def __init__(self):
        super().__init__()
        self.lang = '일본어'

    def say(self):
        print('こんにちは')


p1 = Person()
print(p1.name, p1.age)

k1 = Koren()
print(k1.name, k1.age, k1.lang)
k1.say()

j1 = Japen()
print(j1.name, j1.age, j1.lang)
j1.say()
