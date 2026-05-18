# 프로그래밍의 함수 또한 수학의 함수와 동일하게 값을 넣어주면 
# 특정 기능을 수행한 연산 결과를 출력합니다. 
# 여기서 특정 기능이란 덧셈 같은 비교적 간단한 연산부터 
# 네트워크 연결, 회원 인증, 메일 발송과 같이 복잡하고 어려운 작업까지 모두 포함합니다. 

# ex)
# 정수1, 정수2 -> 정수1+정수2 -> 덧셈 결과
# 네트워크 주소 -> 네트워트 연결 기능 -> 연결 결과
# 아이디, 패스워드 -> 기능 -> 인증 결과

# 믹서기에 사과를 넣으면 사과 주스가 되고, 오렌지를 넣으면 오렌지 주스가 되듯이 사용자는 
# 함수에 값만 집어넣으면 원하는 결과를 얻을 수 있습니다.


# 함수의 종류: (내장 함수 vs 사용자 함수)
# 내장 함수: print(), len() 

# 코드(기능) 재사용 -> 함수 사용
# 데이터 재사용 -> 변수 사용

# 모듈화
# 모듈은 특정 기능의 작은 프로그램을 뜻합니다. 
# 함수를 사용한다는 것은 특정 기능을 모듈화한다는 것으로, 특정 기능이 
# 함수로 모듈화되면 다른 프로그램에 쉽게 이식하여 사용할 수 있습니다. (시간 단축)

# 코드 수정 용이

# 함수(function)
# python에서는 함수가 꽃이다.

# 함수 정의하기
# 사용자 함수를 만든다는 것을 '함수를 정의한다.'라고 합니다.
# 함수를 정의할 때 def 키워드를 사용합니다. 그리고 함수명, 콜론(:), 실행부를 이용합니다.

# def 함수명():
#     실행부(함수기능)

def greet():
    print('안녕하세요.')
    print('반갑습니다.')
    print('저는 홍길동입니다.')


# 함수명 규칙
# 1. 내장함수명과 동일하면 안된다.
# 2. 첫 글자는 주로 소문자로 시작한다.
# 3. 첫 글자는 숫자를 사용할 수 없다.    1greet():x, g1reet():o, greet1():o
# 4. 특수문자는 사용할 수 없지만 언더바(_)는 사용 가능하다.
# 5. 두 개이상의 단어가 조합되는 경우 스네이크, 카멜표기법을 사용한다.
#                           send_message():  sendMessage():

# 온도센서 작동 시스템
# 온도센서 작동을 시작하고 멈추는 함수를 정의해봅시다.
# 함수명은 함수의 기능을 이해하기 좋도록 짓습니다.

def startTemperatureSensor():
    print('온도센서 작동을 시작합니다.')
    
def stopTemperatureSensor():
    print('온도센서 작동을 중지합니다.')

# 함수 호출
startTemperatureSensor()
stopTemperatureSensor()

# Q) 내 노트북은 몇 인치일까?
# 사이즈 표에 인치로만 표시되어있습니다. cm를 인치로 바꿔주는 함수를 만들어봅시다.(1inch = 0.393701cm)

def convertUnit():
    lengthCM = float(input('길이(cm) 입력: '))
    print(f'{lengthCM * 0.393701}inch')

convertUnit()


# Q) 이동 거리를 계산하는 함수
# 길동이는 5시간 동안 3km/h의 속도로 등산을 했습니다.
# 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는 프로그램을 함수를 이용하여 만들어봅시다.

def calculateDistance():
    print(f'이동거리: {hourData * speedData}km')

hourData = float(input('이동 시간: '))
speedData = float(input('이동 속도: '))
 
calculateDistance()

# pass 키워드
def calculateNumber():
    pass

calculateNumber()

# 함수 내에서 또 다른 함수 호출
def fun1():
    print('fun1() CALLED!!')

def fun2():
    print('fun2() CALLED!!')

def fun3():
    fun1()
    fun2()
    print('fun3() CALLED!!')

fun3()

# 재귀 함수
# def fun4():
#     print('fun4() CALLED!!')
#     fun4()

# fun4() -> RecursionError: maximum recursion depth exceeded


# Q) 다국어 인사말 프로그램 by 함수
# 출신 국가를 선택하면 해당하는 국가의 인사말이 출력되는 프로그램을 함수를 이용해서 만들어봅시다.
# 1.한국  2.USA  3.Japan

def introKor():
    print('안녕')

def introEng():
    print('Hello')

def introJapan():
    print('こんにちは')

selectedMenuNum = int(input('Where are you from? 1.한국  2.USA  3.Japan '))

if selectedMenuNum == 1:
    introKor()

elif selectedMenuNum == 2:
    introEng()

elif selectedMenuNum == 3:
    introJapan()


# Q) 계산기 프로그램 by 함수
# 사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램을 함수를 이용해서 만들어봅시다.

def add():
    print(f'덧셈 결과: {inputNumber1 + inputNumber2}')

def sub():
    print(f'뺄셈 결과: {inputNumber1 - inputNumber2}')

def mul():
    print(f'곱셈 결과: {inputNumber1 * inputNumber2}')

def div():
    print(f'나눗셈 결과: {inputNumber1 / inputNumber2}')


def calculator():
    if selectedOperator == 1:
        add()

    elif  selectedOperator == 2:
        sub()

    elif  selectedOperator == 3: 
        mul()

    elif  selectedOperator == 4:  
        div()

inputNumber1 = float(input('숫자를 입력하세요.'))
selectedOperator = int(input('연산자를 입력하세요. 1.+  2.-  3.*  4./ '))
inputNumber2 = float(input('숫자를 입력하세요.'))

calculator()





