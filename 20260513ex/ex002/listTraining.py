# 이번에 만들 출석부 관리 시스템은 리스트를 이용해서 학급의 학생 명단을 
# 관리하는 프로그램으로, 시나리오에 따라 프로그래밍을 전개합니다. 
# 예제가 쉬운 만큼 시나리오만 보고 직접 코딩해 보는 것을 추천합니다

# [[ 시나리오 ]]
 #1 :  학급 학생수가 10명(정우람, 박으뜸, 배힘찬, 천영웅, 신석기, 
 #     배민규, 전민수, 박건우, 박찬호, 이승엽)인 리스트를 만든다.
 #2 :  ‘가나다’ 순으로 정렬한다.
 #3 :  ‘박찬호’ 학생이 전학을 가게 되었다. 출석부에서 삭제한 후 전체
 #      학생과 학생 수를  출력한다.
 #4 :  선생님을 돕기 위한 학생으로 앞에서 3명을 뽑는다.
 #5 :  새로운 친구가 전학 왔다. 이름은 ‘이병규’이다.
 #6 :  자리를 바꾸기 위해서 학생 순서를 역순으로 뒤집는다.
 #7 :  ‘정우람’ 학생이 이름을 ‘정잘남’으로 개명했다.

#1
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', 
            '배민규', '전민수', '박건우', '박찬호', '이승엽']
print(f'students: {students}')
print(f'students of type: {type(students)}')


#2
students.sort()
print(f'students: {students}')

#3
students.remove('박찬호')
print(f'students: {students}')
print(f'students count: {len(students)}')

#4
studentsForHelp = students[:3]
print(f'studentsForHelp: {studentsForHelp}')

#5
students.append('이병규')
students.sort()
print(f'students: {students}')
print(f'students count: {len(students)}')

#6
students.reverse()
print(f'students: {students}')

#ex)
import random
random.shuffle(students)
print(f'students: {students}')

#7
idx = students.index('정우람')
students[idx] ='정잘남'
print(f'students: {students}')

idx = 0
for student in students:
    if student == '정우람':
        students[idx] ='정잘남'
    idx += 1

# 혈액 보관 시스템
# 10명의 기부자에게 혈액을 받아 리스트
# 혈액형을 종류별로 몇 팩씩 보유하고 있는지

LOOP_COUNT = 3
bloods = []
for i in range(LOOP_COUNT):
    print('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요. (a, b, ab, o)')
    bloods.append(input())

print(f'bloods: {bloods}')

print(f'a형\t: {bloods.count('a')}')
print(f'b형\t: {bloods.count('b')}')
print(f'ab형\t: {bloods.count('ab')}')
print(f'o형\t: {bloods.count('o')}')


