# # 지역변수 vs 전역변수 
# # 지역변수는 함수 내부에서 선언되며, 함수 내부에서만 사용 가능합니다.(외부에서 사용x)
# # 전역변수는 함수 외부에서 선언되며, 함수 외부/내부 모두  사용 가능합니다.

# num = 10        # 전역변수

# def fum():
#     num = 20    # 지역변수
#     print(f'num: {num}')

# print(f'num: {num}')  # 10, 전역변수

# fum()                 # 20, 지역변수     
    

# # global 키워드는 함수 내에서 전역변수의 값을 수정하고자 할때 반드시 명시하자.
# num = 10        # 전역변수

# def fum():
#     global num  # 전역변수 수정시 사용(global)
#     num += 1    # 데이터 수정(전역변수)
#     print(f'num: {num}')

# print(f'num: {num}')  # 10, 전역변수

# fum() 


# # Q) 웹사이트의 누적방문 횟수 출력 프로그램 만들기
# flag = True
# totalVisitor = 0

# def countVisitor():
#     global totalVisitor
#     totalVisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문  2.종료 '))

#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVisitor}')
#     else:
#         flag = False
#         print('Good bye~')

# # 매개변수(******************************************)
# # 매개: 둘 사이에서 양편의 '관계를 맺어' 줌
# # 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출하죠.
# # 이 때 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부라고 합니다.

# # 함수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고 합니다.
# # 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장합니다. 그리고 매개변수는 지역변수의 일종입니다.

# def greet():
#     print(f'홍길동님 안녕하세요.')

# greet()

# def greet(name, age):
#     # name = '홍길동' or '박찬호' or '박세리'
#     print(f'{name}님 안녕하세요. 나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)
# # greet('홍길동') 인수와 매개변수의 개수를 맞추지 않으면 에러..TypeError


# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다.')
#     print(f'최고 온도: {temp}도')
#     print(f'평균 습도: {humi}%')
#     print(f'최고 온도: {rain}%')
    
# forecastWeather(35, 70, 80)



# def printScoresForStudent(score1, score2, score3):
#     totalScore = score1 + score2 + score3
#     averageScore = totalScore / 3

#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

# printScoresForStudent(90, 80, 100)


# # 인수의 개수를 모르는 경우 
# # 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자(학생수 총 3명)


# def printScoresForStudent(*scores):
#     totalScore = 0
    
#     for score in scores:
#         totalScore += score 

#     averageScore = totalScore / (len(scores))

#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

# # score = int(input(f'점수를 입력하세요'))

# # printScoresForStudent(score)


# # 몇 명일지 모르는 학생의 점수를 입력할 때 총합과 평균을 구하는 함수를 만들고 이용하는 프로그램

# flag = True
# studentScores = []

# def printScoresForStudent(scores):
#     if len(scores) == 0:
#         print('학생수가 0명이라 총점과 평균을 구할 수 없습니다.')
#     else:
#         totalScore = 0
#         for score in scores:
#             totalScore += score

#         averageScore = totalScore / (len(scores)) 

#         print(f'총합: {totalScore}')
#         print(f'평균: {averageScore}')
     

# while flag:
#     selectedMenuNum = int(input('1.점수 입력    2.종료'))
#     if selectedMenuNum == 1:
#         score = int(input(f'점수를 입력하세요'))
#         studentScores.append(score)
#     else:
#         flag = False

# printScoresForStudent(studentScores)

# # quiz) SMS와 MMS 구별하기
# '''
# 문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
# 넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
# 과하는 프로그램을 만들어봅시다. 
# '''

# def sendUserMessage(str):
#     strLength = len(str)
#     print(f'사용자가 입력한 문자 길이: {strLength}')

#     if strLength <= 100:
#         print(f'sms 발송 완료!')
#         print('50원 부과')
#     else:
#         print(f'mms 발송 완료!')
#         print('100원 부과')

# inputData = input('문자 입력')
# sendUserMessage(inputData)


# # 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):
#     print(f'name\t: {name}')
#     print(f'email\t: {email}')
#     print(f'major\t: {major}')
#     print(f'grade\t: {grade}')
#     print('----------------------------------')

# # printMemberInfo('Hong Gildong', 'gildong@gmail.com', 'art', 1)
# printMemberInfo(email = 'gildong@gmail.com', 
#                 name = 'Hong Gildong', 
#                 major = 'art', 
#                 grade = 1)



# def printMemberInfo(Info):
#     print(f'name\t: {Info['name']}')
#     print(f'email\t: {Info['email']}')
#     print(f'major\t: {Info['major']}')
#     print(f'grade\t: {Info['grade']}')

# printMemberInfo({
#     'email' : 'gildong@gmail.com', 
#     'name' : 'Hong Gildong', 
#     'major' : 'art',            
#     'grade' : 1
#     })



# # 매개변수의 기본값 설정 (직원 급여 지금 프로그램)

# def setSalary(name, pay = 200):
#     print(f'{name}의 급여 {pay}원 지급')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택')   # 200 -> 기본값 적용 

# # 데이터 반환(return)
# # 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
# # 이때 사용하는 키워드가 return입니다.
# # 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램 만들기

# def printResult(value):
#     print(f'result: {value}')  # == print(f'result: {result}')


# def addFuntion(n1, n2):
#     sum = n1 + n2
#     # print(f'결과 값: {sum}')
#     printResult(sum)
#     return sum

# result = addFuntion(10, 20)
# # print(f'result: {result}')  # == print(f'결과 값: {sum}')




# def fun1():
#     print('1')
#     return
#     print('2')
#     print('3')

# fun1()



# DEV_MOD = False

# def fun1():
#     print('1')
#     if DEV_MOD == True:
#         print('2')
#         return
#     print('3')

# fun1()


# # 별탑 만들기
# def increaseStart(limitStarCount):
#     # print('*')
#     # print('**')
#     # print('***')
#     # print('****')
#     # print('*****')
#     # print('******')
#     # print('*******')
#     for n in range(1, 8):
#         print('*' * n)
#         if n == limitStarCount:
#             break

# increaseStart(5)        


# 처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
# 메뉴: 1.회원가입  2.로그인  3.특정 회원 정보 출력  4.모든 회원 정보 출력  99.종료
# 사용자가 
# '1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
# '2.로그인'을 선택하면 회원ID, 회원PW을 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
# '3.특정 회원 정보 출력'을 선택하면 회원ID, 회원PW을 입력받아 일치하면 회원 정보를 모두 출력한다.
# '4.모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
# '99.종료'을 선택하면 프로그램을 종료 시킨다.

# num = int(input('1.회원가입  2.로그인  3.특정 회원 정보 출력  4.모든 회원 정보 출력  99.종료'))


# memberList = []
# list = []

# def nums():
#     id = input('ID를 입력하세요.')  
#     pw = input('PW를 입력하세요.')
#     email = input('Email을 입력하세요.')
#     phone = input('Phone를 입력하세요.')
#     list = {'id': {id}, 'pw': {pw}, 'email': {email}, 'phone': {phone} } 
#     memberList.append(list)
#     print(f'list: {list}')
#     print(f'memberList: {memberList}')


# if num == 1:
#     nums()
# elif num == 2:
#     for list in list:
#         id = input('ID를 입력하세요.')
#         if id == list[0]:
#             pw = input('PW를 입력하세요.')
#             if pw == list[1]:
#                 print('로그인성공')
#             else:
#                 print('로그인실패')    
#         else:
#                 print('로그인실패')        


# elif num == 3:
#     pass
# elif num == 4:
#     pass
# elif num == 99:
#     print('프로그램을 종료합니다.')
    

# id, pw, email, phone

