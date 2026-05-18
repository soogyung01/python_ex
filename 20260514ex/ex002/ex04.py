# CRUD
# C: Creete 생성, 추가
# R: Read   조회
# U: Update 수정
# D: Delete 삭제 

# 딕셔너리(Dictionary): {key: value}
student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'
}

print(f'student: {student}')
print(f'student type: {type(student)}')


# R: Read
sNo = student['학번']
print(f'sNo: {sNo}')
print(f'sNo type: {type(sNo)}')

# U: Update
sName = student['이름']
print(f'sName: {sName}')
student['이름'] = '홍길자'
sName = student['이름']
print(f'sName: {sName}')
print(f'sNametype: {type(sName)}')

# D: Delete
del student['연락처']
print(f'student: {student}')


# keys(), values(), items()
# keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다. 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')

for key in keys:
    print(f'key: value = {key}: {student[key]}')

# values(): 딕셔너리에서 벨류값들만 몽땅 뽑는다. 뽑은 벨류들은 리스트와 비슷한 데이터 타입이다.   
values = student.values()
print(f'values: {values}')
print(f'values type: {type(values)}')

for values in values:
    print(f'values: {values}')


items = student.items()
print(f'items: {items}')   #dict_items([('학번', 123456789), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])
for item in items:
    print(f'item: {item}')
    print(f'item[0], item[1]: {item[0]}, {item[1]}')

for key, value in items:    
    print(f'key: value = {key}: {value}')
    

# 구조분해할당
a, b = (10, 20)
print(f'a: {a}, b: {b}')

c = (10, 20)
a = c[0]
b = c[1]
print(f'a: {a}, b: {b}')

a = 10 
b = 20
# swapping --> a: 20, b: 10
# tamp = a
# a = b
# b = tamp

a, b = b, a

scores = [10, 20, 30, 40, 50, 60]
# a = 10
# b = 20
# c = [30, 40, 50, 60]

a, b, *c = scores
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
