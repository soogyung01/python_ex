# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''

'''
print('정수를 입력하세요.')
inputInteger = input()     #6
print(inputInteger)        #6   
print(type(inputInteger))  #Int x str o
'''

'''
print('실수 입력하세요.')
inputFloat = input()       #3.14
print(inputFloat)          #3.14
print(type(inputFloat))    #str
'''

'''
print('논리형 데이터 입력하세요', end='')   #논리형 데이터 입력하세요 (자동개행)
inputBoolean = input()          #True
print(inputBoolean)             #True
print(type(inputBoolean))       #str



inputBoolean = input('논리형 데이터 입력하세요.\n')
print(inputBoolean)          #True
print(type(inputBoolean))    #str
'''

# , end='' (자동개행 실행 안됨) \n (개행 실행됨)

#자료형을 변환해야 합니다.

# userInputData = input('사용자~~ 정수 입력~')  #10
# print(userInputData)                        #10
# print(type(userInputData))                  #str
# userInputData = int(userInputData)          #str-->int
# print(type(userInputData))                  #int


# str -> boolean
# userInputData = input('True or False 입력하세요.')
# print(userInputData)                              #True
# print(type(userInputData))                        #str
# userInputData = bool(userInputData)
# print(type(userInputData))                        #boolean


#str -> float
# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData = float(userInputData)
# print(type(userInputData))

# x = 3          #int   3
# y = float(x)   #int -> float
# print(y)       #3.0


x = 3.141592
y = int(x)
print(y)          #3
print(float(y))   #3.0
