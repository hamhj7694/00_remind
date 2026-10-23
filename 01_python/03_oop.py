# object oriented programming : 객체 지향 프로그래밍

# 연관있는 변수를 묶어서 관리, 이 변수를 제어하는 기능함수도 함께 그룹화 - 클래스로 설계하고 객체를 만들어 사용

class Person:
    def __init__(self, name='익명', age=0, address='무연고자'):
        self.name= name
        self.age= age
        self.address= address

    # 출력 기능 함수 설계
    def show(self):
        print('이름:', self.name)
        print('나이:', self.age)
        print('주소:', self.address)

# 위에서 만든 설계도(class)를 사용하려면..
p1= Person() #초기화 함수 발동
print(p1.name, p1.age, p1.address)

p2= Person('함형준', 27, '서울')
p2.show()
print('---')

# ---------- 상속 ---------- 기존에 있는 클래스를 가져아서 필요한 멤버만 추가하여 설계하는 간편한 문법
# 이름, 나이, 주소, 전공 정보를 가진 학생 데이터 필요... 이 데이터를 묶어서 관리하기 위해 클래스 설계
class Student(Person): # Person 클래스의 이름, 나이, 주소 멤버변수 보유하게 됨(상속 받음)
    def __init__(self, name, age, address, major):
        super().__init__(name, age, address) #부모 클래스에서 알아서 멤버에 값을 대입해줌.
        self.major= major

    # 상속 받은 show 기능 다시 구현하기(오버라이드)
    def show(self):
        super().show()
        print('major:',self.major)

stud= Student('robin', 22, 'busan', 'ai')
stud.show()