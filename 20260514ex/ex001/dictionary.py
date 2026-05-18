# 딕셔너리(dictionary)
# 딕셔너리는 인덱스 대신 키(key)를 이용하여 아이템을 참조합니다.
# (리스트는 인덱스를 이용하여 아이템을 참조)

# 딕셔너리 정의
# 딕셔너리는 선언할 때는 중괄호{}를 이용하여 데이터를 묶고, 키(key):값(value)

# ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43}
# print(f'ages: {ages}')
# print(f'ages type: {type(ages)}')

# scores = {'c/c++': 'A', 'java': 'B+', '네드워킹': 'C', '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
# print(f'scores: {scores}')


# 마지막 내용: **********************************
# list(리스트), tuple(튜플), dictionary(딕셔너리)

# listVar = [3, 3.14, 'hello']
# print(f'listVar: {listVar}')

# tupleVar = (3, 3.14, 'hello')
# print(f'tupleVar: {tupleVar}')

# dictVar = {'홍길동': 10, '박찬호': '열살', '박세리': 3.14}
# print(f'dictVar: {dictVar}') 

# listVar1 = [1, 2, 3]
# listVar2 = [1, 2, 3, listVar1]

# print(f'listVar1: {listVar1}')  # [1, 2, 3]
# print(f'listVar2: {listVar2}')  # [1, 2, 3, [1, 2, 3]]

# print(listVar2[3][1])           # [1, 2, 3] -> 2

# print(type(listVar2[3]))        # list
# print(type(listVar2[3][1]))     # int


# dicts = {
#     'name': '박찬호',
#     'age': 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구']
# }

# print(f'dicts: {dicts}')
# # {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 'hobby': ['축구', '농구', '배구']}

# print(dicts['hobby'][1])


# 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''

# -1
scores = {
    'C/C++':'A',
    'Java': 'B+',
    '모바일': 'C', 
    '보안': 'A+',
    '해킹': 'F', 
    '시스템': 'C+'
}

# -2
print(f'Java: {scores['Java']}')    # B+
print(f'시스템: {scores['시스템']}')  # C+

# -3
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(f'scores: {scores}')

# -4
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores: {scores}')

# -5
creditScores = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'F': 0.0,
}

totalScore = 0
averageScore = 0

for key in scores.keys():
    totalScore += creditScores[scores[key]]
    print(f'{key}:\t{scores[key]}')     # A+ > 4.5, A > 4.0, B+ > 3.5 ... 

print(f'totalScore: {totalScore}')      # 23.0
averageScore = totalScore / len(scores)
print(f'averageScore: {averageScore}')  # 2.875

'''
C/C++:  A       4.0
Java:   F       0.0
모바일: C        2.0
보안:   A+       4.5
해킹:   F        0.0
시스템: A        4.0
파이썬: A        4.0
OS:     A+      4.5

A+      : 4.5
A       : 4.0
B+      : 3.5
B       : 3.0
C+      : 2.5
C       : 2.0
F       : 0.0
'''