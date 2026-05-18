# 수학시험 프로그램
'''
다음은 수학시험 문제 및 정답입니다.
튜플에 문제를 저장하고 사용자가 답을 입력하면 채점하는 프로그램을 만들어 봅시다.
---------------------------------------
문제                    정답        점수
---------------------------------------
3 + 2                   5          3점
5 ÷ 2의 몫              2           5점
10 - 2                  8          3점
100 * 2                 200         5점
1-(10 ÷ 4의 나머지)      -1          5점
2의 4제곱                16          3점
4 ÷ 2                   2           3점
---------------------------------------
'''

# quiz = (
#     ['3 + 2', 5, 3],
#     ['5 ÷ 2의 몫', 2, 5],
#     ['10 - 2', 8, 3],
#     ['100 * 2', 200, 5],
#     ['1-(10 ÷ 4의 나머지)', -1, 5],
#     ['2의 4제곱', 16, 3],
#     ['4 ÷ 2', 2, 3],
# )

# answerCount = 0
# wrongCount = 0
# totalScore = 0

# for item in quiz:
#     print(f'문제: {item[0]}')
#     answer = int(input('정답 입력: '))
#     if answer == item[1]:
#         answerCount += 1
#         totalScore += item[2]
#     else:
#         wrongCount += 1

# print('-' * 25)
# print(f'맞춘개수: {answerCount}')
# print(f'틀린개수: {wrongCount}')
# print(f'총점: {totalScore}')
# print('-' * 25)





# flag = True

# members = {}

# while flag:
#     selectedMenuNum = int(input('1. 회원가입   2. 프로그램 종료'))

#     if selectedMenuNum == 1:
#         id = input('아이디: ')
#         pw = input('비밀번호: ')
#         members[id] = pw

#     elif selectedMenuNum == 2:
#         flag =  False
   
#         for key in members.keys():
#             print(f'ID: {key}, PW: {members[key]}')
  

classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 
            'Java':'5학점', 'Javascript':'3학점'}

for key in classes:
    if classes[key] == '3학점':
        classes[key] = '5학점'
print(classes)


'''
members = {
    '2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스, 수영', 0],
    '2019-052004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
    '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50]
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]}, {value[2]}')
'''

members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],
        '할인율': 0
    },
    '2019-052004': {
        '이름': '박용택',
        '나이': 65,
        '성별': 'M',
        '연락처': '010-9012-3456',
        '이용서비스': ['수영'],
        '할인율': 50
    },
    '2019-052003': {
        '이름': '박세리',
        '나이': 70,
        '성별': 'W',
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50
    }
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름', '성별', '이용서비스' 그리고 이용서비스개수 만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별, 이용서비스, 이용서비스개수): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')




    