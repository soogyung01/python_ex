#비교 연산자
# == (같다.) -> True or False
# != (같지 않다.) -> True or False
# > (보다 크다.) -> True or False
# >= (보다 크거나 같다.) -> True or False
# < (보다 작다.) -> True or False
# <= (보다 작거나 같다.) -> True or False

# num1 = 10; num2 = 20

# print(num1 == num2)    #False
# print(num1 != num2)    #True
# print(num1 > num2)     #False
# print(num1 >= num2)    #False
# print(num1 < num2)     #True
# print(num1 <= num2)    #True

# Q) 범퍼카 탑승 가능 판별하기
# 신장이 120cm 이상인 어린이만 탑승할 수 있다.
# 사용자가 신장을 입력하면 범퍼카를 탑승할 수 있는지 여부를 출력하는 프로그램을 만들자.
# True: 탑승 가능, False: 탑승 불가능
# height = int(input('어린이의 신장을 입력하세요. '))
# print(height >= 120)

# 문자 비교 (문자 vs 문자)  -> 아스키코드
# print('a' == 'b')     #False
# print('a' < 'b')      #True
# print('a' > 'b')      #False

# 문자열 비교
# str1 = 'hello'
# str2 = 'hello'
# print(str1 == str2)    #True
# print(str1 != str2)    #False
# print(str1 > str2)     #False
# print(str1 < str2)     #False

# str1 = 'hello'
# str2 = 'hello '
# print(str1 == str2)    #False
# print(str1 != str2)    #True