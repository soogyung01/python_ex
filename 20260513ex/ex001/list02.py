# 리스트 정렬
# sort() 함수는 리스트의 아이템을 정렬하는데 사용합니다.
# reverse 옵션이 False면 오름차순(ASC), True면 내림차순(DESC)으로 정렬합니다

numbers = [5, 1, 3, 4, 2, 6]
print(f'numbers: {numbers}')

# 오름차순(ASC)
numbers.sort()      # == numbers.sort(reverse=False)
print(f'numbers: {numbers}')

# 내림차순(DESC)
numbers.sort(reverse=True)
print(f'numbers: {numbers}')

scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
print(f'scores: {scores}')
scores.sort()
print(f'scores: {scores}')
scores.sort(reverse=True)
print(f'scores: {scores}')

# Q) 회의 참석자 정렬하기
# 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
names.sort()
print(f'names: {names}')
names.sort(reverse=True)
print(f'names: {names}')

# 리스트 순서 뒤집기
# reverse() 함수를 이용하면 리스트의 아이템을 역순으로 뒤집을 수 있다
vegetables = ['당근', '오이','양파','감자', '고구마']
vegetables.reverse()
print(f'vegetables: {vegetables}')


# 리스트 슬라이싱(**************************)  [시작 인덱스 값 : 끝 인덱스 값+1]
# 슬라이싱이란, 리스트에서 필요한 부분의 아이템만 뽑아내는 것을 말합니다.
# [n:m] -> n 인덱스부터 m-1 인덱스 까지의 아이템을 슬라이싱(추출)한다. 

animals = ['호랑이', '사자', '곰', '여우', '늑대']
print(f'animals: {animals}')

print(f'animals[1:4]: {animals[1:4]} ')  # ['사자', '곰', '여우']
print(f'animals: {animals}')             # ['호랑이', '사자', '곰', '여우', '늑대']

animals = ['호랑이', '사자', '곰', '여우', '늑대']
print(f'{animals[:3]}') # ['호랑이', '사자', '곰']
# 인덱스 0부터 2(3-1)까지의 아이템 슬라이싱

print(f'{animals[3:]}') # ['여우', '늑대']
# 인덱스 3부터 끝까지의 아이템 슬라이싱

# 뒤에서 2개의 아이템
print(f'{animals[len(animals)-2:]}') # ['여우', '늑대']

print(f'{animals[:-1]}')             # ['호랑이', '사자', '곰', '여우']
print(f'{animals[1:-1]}')            # ['사자', '곰', '여우']

print(f'{animals[::2]}')             # ['호랑이', '곰', '늑대'] 스템


# Q) 역순으로 리스트 출력
#   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alphabet.reverse()
print(f'alphabet: {alphabet }')  # ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

# Q) 리스트를 슬라이싱하시오
#  - 인덱스 2부터 5까지의 아이템을 출력하시오.
#  - 인덱스 0부터 4까지의 아이템을 출력하시오.
#  - 인덱스 3부터 7까지의 아이템을 출력하시오.
#  - 인덱스 5부터 끝까지의 아이템을 출력하시오.
#  - 인덱스 3부터 8까지의 아이템을 출력하시오.
#  - 뒤에서 4개 아이템을 출력하시오.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f'{alphabet[2:6]}')  
print(f'{alphabet[:5]}')   
print(f'{alphabet[3:8]}')
print(f'{alphabet[5:]}')
print(f'{alphabet[3:9]}')
print(f'{alphabet[len(alphabet)-4:]}') # == print(f'{alphabet[-4:]}')
