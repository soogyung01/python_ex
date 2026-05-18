fruit1 = '사과'
fruit2 = '포도'
fruit3 = '복숭아'

fruits = ['사과', '포도', '복숭아']
print(f'fruits: {fruits}')
print(f'fruits of type: {type(fruits)}')

# list(리스트), tuple(튜플), dictionary(딕셔너리)
# list(리스트) 정의(선언 + 초기화)
fruits = ['사과', '포도', '복숭아']

# 인덱스(index): 아이템에 부여된 아이템 식별 번호 
#    0       1       2
# ['사과', '포도', '복숭아']

#아이템 조회
print(f'fruits[1]: {fruits[1]}')
print(f'fruits[2]: {fruits[2]}')
print(f'fruits[0]: {fruits[0]}')
# print(f'fruits[3]: {fruits[3]}')  # IndexError

# 리스트의 길이
cnt = len(fruits)
print(f'cnt: {cnt}')

# 리스트의 마지막 아이템의 인덱스 값은 '리스트의 길이 -1' 이다
print(f'len data: {fruits[len(fruits)-1]}')
print(f'first data: {fruits[0]}')

# 리스트의 전체 데이터 조회
# 반복가능한 객체(데이터) -> 이터러블한 데이터
for fruit in fruits:
    print(f'fruit: {fruit}')

for idx, fruit in enumerate(fruits):
    print(f'index: {idx}, fruit: {fruit}')    

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

# 아이템 삽입(+마지막에)    
fruits = ['사과', '포도', '복숭아']
fruits.append('수박')
print(f'fruits: {fruits}')   #['사과', '포도', '복숭아', '수박']

# (특정위치에)
fruits.insert(2, '메론')
print(f'fruits: {fruits}')   #['사과', '포도', '메론', '복숭아', '수박']

# 리스트 연결
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list1.extend(list2)        # [1, 2, 3, 10, 20, 30]
print(f'list1: {list1}')   # [1, 2, 3, 10, 20, 30]
print(f'list2: {list2}')   # [10, 20, 30]

# 리스트 연결 +
list3 = list1 +list2       # 새로운 메모리 공간에 만들어진다 [1, 2, 3, 10, 20, 30]
print(f'list3: {list3}')

# 아이템 삭제하기(+마지막 데이터)
sports = ['football', 'baseball', 'volleyball', 'basketball']   
sports.pop()
print(f'sports: {sports}')

# (특정위치에)
sports.pop(1)
print(f'sports: {sports}')

# pop()과 비슷하게 사용할 수 있는 키워드 del
del sports[1]
print(f'sports: {sports}')

# pop() vs del
nums = [1, 2, 3, 4, 5, 6]
deletedNum = nums.pop(3)
print(f'deletedNum: {deletedNum}')

# 특정 아이템 삭제 by 아이템
languages = ['c/c++', 'c#', 'java', 'python']
# languages.pop(2)

languages.remove('java')
print(f'languages: {languages}')

# remove()를 이용해서 아이템을 삭제할 때 삭제하려는 아이템의 개수가 2개 이상일 때?
languages = ['c/c++', 'c#', 'java', 'python', 'java']
languages.remove('java')
print(f'languages: {languages}')  #['c/c++', 'c#', 'java', 'python']
# -> 처음 아이템만 삭제됨

# Q) 과일 리스트에서 야채를 찾아 삭제하기
# 냉장고에 있는 과일 리스트다
# ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
# 이중 '당근', '토마토'를 찾아 삭제하기
fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
print(f'fruits: {fruits}')

for item in fruits:
    if item == '당근' or item == '토마토':
        fruits.remove(item)
print(f'fruits: {fruits}')    

# Q) 합격 여부 판정
# 다음은 홍길동 수험생의 2020년 공인중개사 자격증 시험 성적표입니다.
# 아래 합격 기준에 만족하는지 구하는 프로그램을 만들어봅시다.
#  - 매 과목 100점을 만점으로 하여 매 과목 40점 이상
#  - 전 과목 평균 60점 이상 득점

# 홍길동 수험생 성적표
# 부동산 개론: 55점
# 민법:       35점
# 공법:       40점
# 공시법:     70점
# 세법:       65점
# 중개사법:    30점

scores = [55, 35, 40, 70, 65, 30]
total        = 0           # 총점
underSubject = 0           # 과락 과목 개수
average      = 0           # 평균

for score in scores:
    if score < 40:         # 과락 과목 개수
        underSubject += 1

    total += score         # 총합  

print(f'40점 미만 과목 수: {underSubject}')    
average = total / len(scores)
print(f'평균: {average:.2f}') # {total / len(scores)}지향!={total / 6}지양..!

# 합격 여부
if underSubject > 0 or average < 60:
    print(f'아쉽습니다. 다음 기회에...')
else:
    print(f'축! 합격!!')    
