# print('회원정보를 입력하세요')

# userName = input('이름 : ')
# userMail = input('메일 : ')
# userId = input('아이디 : ')
# userPw = input('비빌번호 : ')

# print('-------------------')
# print('To. ' + userMail)
# print('▶아이디 및 비밀번호 확인')
# print(userName + ' 고객님 안녕하세요.')
# print(userName + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
# print('아이디 : ' + userId)
# print('비밀번호 : ' + userPw)
# print('감사합니다.')
# print('Naver 담당자.')
# print('-------------------')

userMail = 'gildong@gmail.com'
print('To. gildong@gmail.com')
print('To. ' + userMail)
print('To.',  userMail)

print("이름:", "홍길동", "나이:", 20)    #이름: 홍길동 나이: 20 (*****)
print("2026", "05","06", sep="-")     #2026-05-06 (**)

print("Hello", end=" ")        #Hello World   (자동개행x)
print("World")

print("Hello", end="")        #HelloWorld
print("World")

#f-string (가장 많이 사용) (**********)
name = '철수'
age = 25

#이름은 철수, 나이는 25입니다.
print('이름은 ' + name + ', 나이는 ' + str(age) + '입니다.')
print(f'이름은 {name}, 나이는 {age}입니다')      #EL표기법

#print(f"이름은 {name}, 나이는 {age}입니다.")

#format (두 번째로 많이 사용) (*********)
print("이름은 {}, 나이는 {}입니다.".format(name, age))

print("이름은 {1}, 나이는 {0}입니다.".format(age, name))   
#.format(0,1,2,3......){}안에 숫자로 자리를 지정하여 넣을 수 있다




koreanScore = input('국어 점수')
englishScore = input('영어 점수')
mathScore = input('수학 점수')

print(f'국어 점수 : {koreanScore}')
print(f'영어 점수 : {englishScore}')
print(f'수학 점수 : {mathScore}')

   
num1 = int(input('정수를 입력하세요.'))
num2 = int(input('정수를 입력하세요.'))

print(f'합: {num1 + num2}')
print(f'평균: {(num1 + num2) / 2}')

var1 = 10
var2 = 20

print(f'var1: {var1}, var2: {var2}')

tamp = var1
var1 = var2
var2 = tamp
print(f'var1: {var1}, var2: {var2}') 


 