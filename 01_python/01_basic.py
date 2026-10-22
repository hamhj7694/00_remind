#1. print()
print('안녕하세요. 오랜만에 파이썬 print 코드를 실행합니다.')

#2. 변수 선언
name= "함형준" # 문자열
age= 27 # 정수
height= 175.5 # 실수
is_student= True # 논리값

print(name, age, height, is_student)
print(f"{name}님의 나이는 {age}살입니다.")

#자료형 확인하기(함수) - type()
print(type(name), type(age), type(height), type(is_student))

#키보드로 사용하는 입력 데이터 받기 input()
# user_name= input("이름을 입력하세요: ").strip() or "학생"
# print(f"환영합니다! {user_name}님!")

#2. 연산자와 문자열 유용한 기능
a,b= 10,3
print('사칙연산 :', a+b, a-b, a*b, a/b)
print('정수 나눗셈 :', a//b)
print('나머지 :', a%b)
print('거듭제곱 :', a**b)

#비교, 논리 연산자
print('비교 연산자 :', a>b, a<b, a==b, a!=b)
print('논리 연산자 :', a>5 and b<5, a>5 or b<5, a>5 and not b<5)

#문자열 관련 유용한 기능 (원본 불변)
message= "     Python Review, Python    "
print(message)
print(message.strip().lower()) # 양쪽 공백 제거 and 소문자 변환
print(message.replace("Python", "파이썬")) # 문자열 치환

print('사과,바나나,오렌지'.split(',')) #응답 결과는 리스트
print("Py" in message) # 문자열 포함 여부 확인 -- true
print("딸기" in message) # 문자열 포함 여부 확인 -- false

print(len(message)) # 문자열 길이 확인 == 글자수

#3.제어문(조건, 반복)
# 제어문 따른 학점 산출
score= 51
if score >=90:
    grade= "A"
elif score >=80:
    grade= "B"
else:
    grade= "C"
print(f"점수: {score}, 학점: {grade}")

#반복문
for i in [1,2,3,4,5]: #1부터 5까지 반복
    print(i, end=' ')

print() #줄바꿈

for i in range(1,6): #1부터 5까지 반복
    if i==3:
        break #반복문 종료 -- 1 2
    print(i, end=' ')

for i in range(1,6): #1부터 5까지 반복
    if i==3:
        continue #반복문 건너뛰기 -- 1 2 4 5
    print(i, end=' ')

print() #줄바꿈

count= 0
while count < 3:
    print(count, end=' ')
    count += 1

print() #줄바꿈

#-----
#4. (중요) 리스트, 튜플, 딕셔너리, Set, 커프리헨션
fruits= ["사과", "바나나", "오렌지"] #리스트
print(fruits)
fruits.append("딸기") #리스트에 요소 추가
print(fruits)
fruits[1]="키위"
print(fruits)

point= (10,20) #튜플 - 요소 수정 불가
print(point)
print(point[0], point[1])
#point[0]= 30 #튜플은 요소 수정 불가 -- 오류 발생

student= {"name":"SAM", "age":25, "score":90}
print(student)
student["score"]= 30
print(student["score"], student.get("nam","없음")) #nam은 변수 이름 오타를 의도로 유도함. 만약 변수가 없으면 자동으로 뒤에꺼가 나옴

#중복 데이터를 허용하지 않는 Set 타입
fruits= ["사과", "바나나", "오렌지", "사과", "바나나"]
unique_fruits= set(fruits) # list->set : 중복 제거(중복 허용 안 함... 유니크 할 때 많이 사용) / 단, 순서가 바뀔 수 있다..
print(unique_fruits)

#1부터 5의 제곱값을 저장하는 리스트 생성
squares= [n**2 for n in range(1,6)] # 제곱해, n의 값들을, 1부터 5까지
print(squares)

passing= [n for n in [65, 16, 76, 90, 100] if n>80] # 80점 이상만 필터링
print(passing)

#-----
#5. 함수, lambda
def greet(person, greeting="안녕하세요."):
    return f"{greeting} {person}님!"

print(greet("영희"))
print(greet("철수", "반갑습니다."))

def average(numbers):
    return sum(numbers)/len(numbers)

print(average([10,20,30,40,50]))

# 제곱해 주는 기능 함수 -- 람다함수로 만들기
square= lambda x: x**2
print(square(5))

# 내장함수 중에서 자주 사용
print('정렬:', sorted([3,1,4,2,5]))
print(min([3,1,4,2,5]), max([3,1,4,2,5]))

#----------------------------------------------------------------------------
#6. 파일 입출력 기능
#현재 파일이 있는 폴더에 결과 txt 문서 저장하기
from pathlib import Path
BASE_DIR= Path(__file__).resolve().parent # resolve() 절대 경로로 변환... Path(__file__)만 하면 상대 경로임. 이거의 부모 parent를 가져오면 현재 파일이 있는 폴더가 됨 (parent 안 쓰면 현재 파일명까지 나옴)
# BASE_DIR= Path(__file__).resolve().parent == C:\Users\mbc\Desktop\학생방\함형준\00. 심화 학습 전 리마인드 수업\01_python
# BASE_DIR= Path(__file__).resolve() == C:\Users\mbc\Desktop\학생방\함형준\00. 심화 학습 전 리마인드 수업\01_python\01_basic.py

file_path= BASE_DIR / "output.txt" # 현재 파일이 있는 폴더에 output.txt 파일 생성

file= open(file_path, "w", encoding="utf-8") # w: write(쓰기), r: read(읽기), a: append(추가)

file.write("파이썬 복습\n파일 입출력 예제 \n")

file.close() # 파일 닫기

with open(file_path, "r", encoding="utf-8") as file: # with open() as file: -- 파일을 열고 닫는 것을 자동으로 처리해줌
    content= file.read() # 파일 읽기
    print(content)

#예외처리
try:
    number= int("80abc")
    print(number) # 오류 발생 -- ValueError: invalid literal for int() with base 10: '80abc'
except ValueError as error:
    print("오류 발생:", error)
finally:
    print("예외 처리와 상관없이 무조건 실행")