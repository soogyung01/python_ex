# # # 컨테이너 자료형_자료형(데이터를 묶어서 표현하는 것)
# # # 데이터 집합_데이터를 하나씩 저장하여 사용하기보다 여러 데이터를 묶어서 저장하고 관리하는게 편하다

# # # list(리스트), tuple(튜플), dictionary(딕셔너리)_(**********)

# # # 리스트(list)는 같은 유형의 데이터를 나열한 것
# # # 리스트를 선언할 때는 대괄호[]를 이용하여 데이터를 묶고, 데이터 사이는 쉼표,로 구분한다.
# # # ex) [사과, 포도, 수박, 참외], [한국, 미국, 일본, 중국]
# # #     변수명 = ['사과', '포도', '수박', ...]

# # fruits = ['사과', '수박', '메론', '참외', '배', '자두', '복숭아', '바나나']
# # print(f'fruits: {fruits}')
# # print(f'type of fruits: {type(fruits)}')

# # # 리스트와 데이터
# # # 리스트에 포함되는 데이터는 어떤 자료형이든 상관없다.
# # # (정수, 실수, 문자(열)이 하나의 리스트로 묶일 수 있다.) 

# # complexList = [10, 3.14, 'a', 'hello']
# # # 이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는 
# # # python과 javascript 뿐이다. java는 안된다.

# member = []
# print(f'member: {member}')
# print(f'type of member: {type(member)}')

# # # Q) 다음 회의 참석자 명단을 리스트로 선언하고 attendList 변수에 담아보자
# # attendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']

# # # how to 리스트의 아이템 조회
# # # 특정 아이템 조회
# # # 인덱스(index)
# # #   ->      0      1       2      3      4      5      6         7 
# # fruits = ['사과', '수박', '메론', '참외', '배', '자두', '복숭아', '바나나']
# # print(f'fruits[1]: {fruits[1]}')
# # print(f'fruits[7]: {fruits[7]}')

# # # 리스트에 존재하지 않는 인덱스를 참조하면 에러가 발생 (IndexError: list index out of range)
# # # print(f'fruits[8]: {fruits[8]}') 

# # # 리스트 길이란 리스트의 아이템 개수를 뜻하는 것으로 len() 함수를 사용하면 알 수 있다
# # # len()
# # number = [1, 2, 3, 4, 5]
# # print(f'number: {number}')
# # print(f'number length: {len(number)}')

# # number = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
# # print(f'첫 번째 데이터: {number[0]}')
# # print(f'마지막 데이터: {number[len(number)-1]}')

# # # len() 함수는 문자열의 길이를 조회하는데에도 사용
# # str = "hell lll lll  llll        lllo"
# # print(len(str))

# # # 입력한 글자 수 확인하기
# # # 사용자로부터 메시지를 입력 받고, 입력받은 문자열의 길이를 출력하는 프로그램
# # msg = input('메시지를 입력하세요')
# # msgLen = len(msg)
# # print(f'msgLen: {msgLen}')

# # # 리스트 전체 데이터 조회
# # balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# # # print(f'{balls[0]}')
# # # print(f'{balls[1]}')
# # # print(f'{balls[2]}')
# # # print(f'{balls[3]}')
# # # print(f'{balls[4]}')
# # idx = 0
# # for item in balls:                           # item = 야구공, item = 축구공, item = 탁구공, 
# #     print(f'item:{item}, index: {idx}')    
# #     idx += 1

# # for (idx, item) in (enumerate(balls)):   ->enumerate 반복문 돌릴 때 인덱스와 값을 같이 가져오는 함수
# # for idx, item in enumerate(balls):           # item = 야구공 idx = 0, item = 축구공 idx = 1, item = 탁구공 idx = 2, 
# #     print(f'item:{item}, index: {idx}')    

# # balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']

# # i = 0
# # while i < len(balls):
# #     print(f'item: {balls[i]}, index: {i}')
# #     i += 1

# # Q) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오
# # sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
# # lenVer = len(sports)-1
# # print(sports[lenVer])

# # Q) 리스트에서 'python' 문자열의 인덱스 값을 출력하는 프로그램
# languages = ['c/c++', 'c#', 'python', 'java']
# for (idx, item) in enumerate(languages):
#     if str == 'python':
#         print(f'python idx: {idx}')

# targetIdx = languages.index("python")  
# print(f'targetIdx: {targetIdx}')      

# # 아이템 기존 리스트에 삽입
# # 리스트 마지막에 삽입
# sports = ['football', 'baseball', 'volleyball']
# print(f'sports: {sports}')

# sports.append('basketball')
# print(f'sports: {sports}')
# print(f'sports lenght: {len(sports)}')

# # Q) 취미 추가하기 그리고 총 취미의 개수를 출력
# hobbies = []
# flag =True
# while flag:
#     hobby = input('취미 입력: ')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')
#     selectedMenuNnmber = int(input('1.취미 추가   2.종료'))
#     if selectedMenuNnmber == 2:
#         print(f'총 개수: {len(hobbies)}')
#         flag = False

# # 원하는 위치에 
# sports = ['football', 'baseball', 'volleyball']
# sports.insert(1, 'basketball')
# print(f'sports: {sports}')

# # 누락된 숫자 추가
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers.insert(5, 6) 
# print(f'numbers: {numbers}')
# numbers.append(10)
# print(f'numbers: {numbers}')

# # 리스트 연결
# # 리스트에 또 다른 리스트를 연결할 때는 extend() 함수를 사용
# list1 = [1, 2, 3]
# print(f'list1: {list1}')  #[1, 2, 3]

# list2 = [10, 20, 30]
# print(f'list2: {list2}')  #[10, 20, 30]

# list1.extend(list2)
# print(f'list1: {list1}')  #[1, 2, 3, 10, 20, 30]
# print(f'list2: {list2}')  #[10, 20, 30]

# list3 = list1 + list2
# print(f'list1: {list1}')  
# print(f'list2: {list2}')  
# print(f'list3: {list3}')

# 리스트 아이템 삭제하기
# 리스트 마지막 아이템 삭제하기
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports: {sports}')  #['football', 'baseball', 'volleyball', 'basketball']
# sports.pop()
# print(f'sports: {sports}')  #['football', 'baseball', 'volleyball']
# sports.pop(1)
# print(f'sports: {sports}')  #['football', 'volleyball']

# removedItem = sports.pop()
# print(f'removedItem: {removedItem}')   #['volleyball']

# # pop() 대신 del 키워드를 이용해서 아이템을 삭제할 수 있다 _pop는 저장도 가능하지만 del은 저장이 안된다
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# del sports[2]
# print(f'sports: {sports}')  #['football', 'baseball', 'basketball']

# 'volleyball' 삭제하기
sports = ['football', 'baseball', 'volleyball', 'basketball']
volleyballIdx = sports.index('volleyball')
sports.pop(volleyballIdx)
print(f'sports: {sports}') 