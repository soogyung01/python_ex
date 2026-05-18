# # 제어문
# # -조건문: 특정 조건에 의해서 프로그램이 분기된는 것(if, if~else, if~elit)
# # -반복문: 특정 상황에 

# # if 조건식
# #     실행문
# num5 = 50
# if num5 > 10:
#     print('num은 10보다 크다')

# # if키워드: 조건문을 선언하기 위한 키워드로 '만약~라면'의 뜻을 가지고 있다.
# # 조건식: 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정된다.
# # 콜론: 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.
# # 실행문: 조건식의 결과가 참(True)인 경우 실행하는 명령문입니다. 
# #        조건식이 거짓(False)이면 실행문이 실행되지 않는다. 
# #        pass 입력시 오류x (나중에 수정할 때 사용)

# # 사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램을 만들어 봅시다.
# num = int(input('please input integer number'))

# if num > 10:
#     print(f'{num}은 10보다 크다.')

# if num == 10:
#     print(f'{num}은 10과 같다.')

# if num < 10:
#     print(f'{num}은 10보다 작다.')    

# # Q) 속도위반 경고하기
# # 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램을 만드시오

# carSpeed = int(input('속도를 입력하세요. '))
# if carSpeed > 50:
#     print(f'속도 위반!!')

# if carSpeed <= 50:
#     print(f'정상 운행')
                         
#     print(f'정상 운행')    



# carSpeed = 40
# if carSpeed <= 50: print(f'좋아요!!') #실행문이 하나면 바로 뒤에 붙여서 사용가능

# num = 5
# if num > 0:
#     pass         #pass 입력시 오류x (나중에 수정할 때 사용)

# myScore = 70
# if myScore >= 90:
#     print('용돈 획득!')

# if myScore < 90:
#     print('빠따')   

# #if~else
# if myScore >= 90:
#     print('용돈 획득!')
# else:
#     print('빠따')


# # 점수 90점 이상 'A'출력
# # 점수 80점 이상 ~ 90점 미만 'B'출력
# # 점수 70점 이상 ~ 80점 미만 'C'출력
# # 점수 60점 이상 ~ 70점 미만 'D'출력

# #if~elif
# myScore = int(input('점수 입력: '))
# if myScore >= 90:
#     print('A')
# elif myScore >= 80:
#     print('B')   
# elif myScore >= 70:
#     print('C') 
# elif myScore >= 60:
#     print('D')  
# else:
#     print('F')       

# #순서가 달라지면 순차적으로 처리하기 때문에 and 연산자로 정확한 구간을 정해주면 된다.
# myScore = int(input('점수 입력: ')) #65 입력했을 때 and를 사용하지 않으면 'D'가 출력되기 때문에 
# if myScore >= 90:
#     print('A')
# elif (myScore >= 80) and (myScore < 70):
#     print('B')
# elif (myScore >= 60) and (myScore < 50):
#     print('D')       
# elif (myScore >= 70) and (myScore < 60):
#     print('C')   
# else:
#     print('F')    

# # Q) 다국어를 지원하는 식당 자동 주문 시스템(1번: 한국어, 2번: 영어, 3번: 중국어, 그 외: 영어)

# # 1.대한민국   2.USA   3.中國 
# # 1: 주문하시겠습니까?
# # 2: Would you like to place an order?
# # 3: 您要点单吗？ 
# # 그외: Would you like to place an order? 

# KOREA_NUMBER = 1
# USA_NUMBER = 2
# CHINA_NUMBER = 3

# selectedNumber = int(input('1.대한민국   2.USA   3.中國'))

# if selectedNumber == KOREA_NUMBER:
#     print('주문하시겠습니까?')
# elif selectedNumber == USA_NUMBER:
#     print('Would you like to place an order?')    
# elif selectedNumber == CHINA_NUMBER:
#     print('您要点单吗？') 
# else:
#     print('Would you like to place an order?')    

# # Q) 국가재난지원금 수령액 조회
# # 1인 가구: 400,000원
# # 2인 가구: 600,000원 
# # 3인 가구: 800,000원
# # 4인이상 가구: 1,000,000원    

# num1 = 1
# num2 = 2
# num3 = 3

# household = int(input('가구원 수를 입력하세요. '))
# if household == num1:
#     print('400,000원')
# elif household == num2:
#     print('600,000원')  
# elif household == num3:
#     print('800,000원')
# else:
#     print('1,000,000원')        
     

# # Q) if~elif문을 이용
# # BMI 지수를 입력
# # BMI 지수가 90 이하면 '저체중'을 출력
# # BMI 지수가 90 초과~110 이하면 '정상 체중'을 출력 
# # BMI 지수가 110 초과~120 이하면 '과체중'을 출력    
# # BMI 지수가 120 초과~140 이하면 '비만'을 출력 
# # BMI 지수가 140 초과면 '고도 비만'을 출력  
# BMI = int(input('BMI 지수를 입력하세요. '))
# if BMI <= 90:
#     print('저체중')
# elif (BMI > 90) and (BMI <= 110):
#     print('정상 체중')  
# elif (BMI > 110) and (BMI <= 120):
#     print('과체중')
# elif (BMI > 120) and (BMI <= 140):
#     print('비만')    
# else:
#     print('고도 비만')

# # 중첩 조건문
# # 조건문 내에 또 다른 조건문을 쓸 수 있는데 이를 중첩 조건문이라 한다.
# # 사용자가 입력한 정수에서 양수(0포함)인지를 판단하고 양수라면 홀/짝인지 구분하자

# myInteger = int(input('정수 입력: '))     
# if myInteger >= 0:
#     print('양수!')
#     if myInteger % 2 == 0:
#         print('짝수!')
#     else:
#         print('홀수!')   
# else:
#     print('음수!')


# # # Q) 짝수/홀수
# num = int(input('양의 정수 입력~'))
# if num > 0:
#     if num % 2 == 0:
#         print('짝수!!')
#     else:
#         print('홀수!')
# else:
#     print('0 또는 음수 입니다')    

# # Q) 출생연도 끝자리(endBirthYear)와 나이(age)를 입력 요구사항에 맞춰 마스크 구매 가능 요일을 출력
# #   공적마스크 판매 관련 출생년도 끝자리를 이용한 5부제
# # - 1,6 => 월
# # - 2,7 => 화
# # - 3,8 => 수
# # - 4,9 => 목
# # - 5,0 => 금 
# # - 만 65세 이상 어르신은 언제든지 구매 가능

# endBirthYear = int(input('출생연도 끝자리 입력: '))
# age = int(input('나이 입력: '))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear ==6:
#         print('월요일에 구매 가능합니다. ')
#     elif endBirthYear == 2 or endBirthYear ==7:
#         print('화요일에 구매 가능합니다. ')    
#     elif endBirthYear == 3 or endBirthYear ==8:
#         print('수요일에 구매 가능합니다. ')
#     elif endBirthYear == 4 or endBirthYear ==9:
#         print('목요일에 구매 가능합니다. ')
#     elif endBirthYear == 5 or endBirthYear ==0:
#         print('금요일에 구매 가능합니다. ')   
# else:
#     print('언제나 구매 가능합니다. ')           

# # 날짜 관련 모듈: datetime
# import operator
# from datetime import datetime
# # 현재 일 구하기
# # print(datetime.today().weekday)  #4  (0=월, 1=화, 2=수, 3=목....)
# print(datetime.today().day)     #8

# today = int(datetime.today().day)
# carNumber = int(input('차량 번호 4자리를 입력하세요. '))
# print(f'오늘 날짜: {today} 일')

# if (today % 2) == 0:
#     print('오늘 입차: 번호가 짝수인 차량') 
# else:
#     print('오늘 입차: 번호가 홀수인 차량')  
# if (today % 2) == (carNumber % 2):
#     print('입차 가능')
# else:
#     print('입차 불가능')    

# # Q) 심정지 환자에게 자동 심장 충격기를 사용했을 때 최초로 시행한 시간에 따른 생존율
# #    장비를 사용하기까지 걸린 시간을 입력하면 생존율이 출력되는 프로그램을 만들자
# # 시간 - 60초, 생존율 - 85%
# # 시간 - 120초, 생존율 - 76%
# # 시간 - 180초, 생존율 - 66%
# # 시간 - 240초, 생존율 - 57%
# # 시간 - 300초, 생존율 - 47%
# # 시간 - 300초 초과, 생존율 - 25%

# time = int(input('최초 장비를 사용하기까지 걸릴 시간(초)을 입력하세요.'))
# print(f'최초 장비를 사용하기까지 걸릴 시간(초)을 입력하세요. {time}')
# if (time <= 60):
#     print('생존율: 85%')
# elif (time <= 120):
#     print('생존율: 76%')
# elif (time <= 180):
#     print('생존율: 66%') 
# elif (time <= 240):
#     print('생존율: 57%')
# elif (time <= 300):
#     print('생존율: 47%') 
# else:
#     print('생존율: 25% 미만')              

# 전기를 많이 사용하면 누진세가 붙어 단가와 기본요금이 올라감
# 전기 사용량을 입력하면 전기료가 출력되는 프로그램
# 사용량(kwh)-200이하  , 단가(원)-99.3  , 기본요금(원)-910
# 사용량(kwh)-201~400이하  , 단가(원)-187.9  , 기본요금(원)-1600
# 사용량(kwh)-400초과  , 단가(원)-280.6  , 기본요금(원)-7300


baseFee1 = 910
baseFee2 = 1600
baseFee3 = 7300

unitPrice1 = 99.3 
unitPrice2 = 187.9
unitPrice3 = 280.6

electricity = int(input('전기 사용량을 입력하세요.'))
print(f'전기 사용량을 입력하세요. {electricity} ')

if electricity <= 200:
    print(f'사용량 : {electricity} kwh')
    print(f'기본요금 : {baseFee1} 원')
    print(f'단가 : {unitPrice1} 원')
    print(f'전기 요금 : {baseFee1 + electricity * unitPrice1}원')
elif electricity <= 400:
    print(f'사용량 : {electricity} kwh')
    print(f'기본요금 : {baseFee2} 원')
    print(f'단가 : {unitPrice2} 원')
    print(f'전기 요금 : {baseFee2 + electricity * unitPrice2}원')  
else:
    print(f'사용량 : {electricity} kwh')
    print(f'기본요금 : {baseFee3} 원')
    print(f'단가 : {unitPrice3} 원')
    print(f'전기 요금 : {baseFee3 + electricity * unitPrice3}원')
      
height = int(input('신장 입력: '))
if height >= 120 and height <= 160:
    print('탑승 가능!')
else:
    print('탑승 불가능!')     

testScore = int(input('시험 점수 입력: '))
result = 'success' if testScore >= 85 else 'fail'   
print(f'result: {result}') 

testScore = int(input('시험 점수 입력: '))
if testScore >=85:
    print('success')
else:
    print('fail')    

import random  #난수 발생 모듈

random.randint(1, 3)  #1부터 3까지의 정수중에서 하나는 발생한다.

ranNum = random.randint(1, 3)
myNum = input('1.가위 2.바위 3.보 를 선택하세요. ')   

if ranNum == myNum:
    print('무승부')
elif (ranNum == 1  and myNum == 2) or (ranNum == 2  and myNum == 3) or (ranNum == 3  and myNum == 1):
    print('사용자 승')
elif (ranNum == 1  and myNum == 3) or (ranNum == 2  and myNum == 1) or (ranNum == 3  and myNum == 2):
    print('컴퓨터 승')    

# Q) 사용자가 입력한 문자 메시지 길이에 따라 SMS 또는 MMS의 발송을 결정하는 프로그램  
#    (단, 메시지 길이가 50 이하면 SMS발송, 그렇지 않으면 MMS를 발송한다. )  


str = 'hello    '
print(f'str: {str}')
print(f'str length: {len(str)}')

useMessage = input('메시지를 입력하세요. ')
msgLen = len(useMessage)

if msgLen <= 50:
    print('SMS 발송')
else:
    print('MMS 발송')


