# # 나눗셈 연산자(/)_실수
# print(10 / 2)         # 5.0
# print(3.14 / 0.5)     # 6.28 (0생략가능 .5=0.5)

# num1 = 100
# num2 = 10
# print(f'num1 / num2 = {num1 / num2}')

# # Q) 신체질량지수(BMI) 구하기
# # BMI = 몸무게(kg) / 신장(m)의 제곱

# weight = float(input('몸무게(kg): '))
# height = float(input('신장(m): '))
# bmi = weight / (height * height)
# print(f'BMI: {bmi:.2f}')

# # 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다.
# print(0 / 123)         #0.0

# # 어떤 숫자를 0으로 나눌 수 없다. 에러
# print(10 / 0)

# # 나머지, 몫, 거듭제곱
# print(10 % 2)
# print(10 % 3)

# # Q) 홀짝 게임하기
# # 짝수는 0, 홀수는 1을 출력
# inputData = int(input('손 안에 동전 수를 입력하세요.'))
# result = inputData % 2
# print(result)

# # 몫(//)_정수
# print(10 // 3)    #3

# # Q) 빵을 나누어 줄 수 있는 학생 수 구하기
# bread = 97
# breakCnt = 3
# maxFriendCnt = bread // breakCnt
# print(f'빵을 나누어 줄 수 있는 학생 수: {maxFriendCnt}')

# resBreadCnt = bread % breakCnt
# print(f'남는 빵 개수: {resBreadCnt}')

# # 거듭제곱(**)_정수
# print(2 ** 2)    # 4
# print(2 ** 3)    # 8
# print(2 ** 10)   # 1024

# # Q) 전염병 예상 감염자 수 구하기
# # 하루에 한 사람이 한 명씩 감염시키는 것으로 나타남
# # 확진자 한 사람이 나올 경우 30일 이후 몇 명의 감염자가 나오는지 구하시오
# man = 2
# date = 30
# total = man ** date
# print(f'{date}일 이후 예상 감염자 수: {total}')

