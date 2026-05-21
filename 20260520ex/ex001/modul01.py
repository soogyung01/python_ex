# Q) 단위환산 프로그램
# mm 단위의 길이를 입력하면 cm, m, inch, ft등으로 단위가 변환되어 
# 출력되는 프로그램 만들기(함수포함)

# def convertUnit(lenMn):

#     unitDic = {}

#     unitDic['cm'] = lenMn * .1
#     unitDic['m'] = lenMn * .001
#     unitDic['inch'] = lenMn * .03937
#     unitDic['ft'] = lenMn * .003281

#     return unitDic

# def printLength(lengths):
#     for len in lengths.keys():
#         print(f'{len}: {lengths[len]}{len}')

# inputMmData = int(input('길이(mm)를 입력하세요. '))
# resultData = convertUnit(inputMmData)
# printLength(resultData)



# Q) 할인된 상품 가격표 출력 프로그램
# DW마트는 고객 감사의 일환으로 ‘오늘의 할인’ 이벤트를 진행할 계획입니다. 아래
# 의 상품 가격표를 참고해서 ‘오늘의 할인율’을 입력하면 할인된 가격이 출력되는 프
# 로그램을 만들어 봅시다.
# 쌀: 9,900
# 상추: 1,900
# 고추: 2,900
# 마늘: 8,900
# 통닭: 5,600
# 햄: 6,900
# 치즈: 3,900

# standardPrice = {
#     '쌀': 9900,
#     '상추': 1900,
#     '고추': 2900,
#     '마늘': 8900,
#     '통닭': 5600,
#     '햄': 6900,
#     '치즈': 3900
# }

# def getDiscountPrice(rate):
#     dcPrice = {}

#     for goodsName in standardPrice.keys():
#         disPrice = int(standardPrice[goodsName] * (1 - (rate / 100)))
#         dcPrice[goodsName] = disPrice

#     return dcPrice

# def printPrice(priceList):
#     for goodsName, goodsPrice in priceList.items():
#         print(f'{goodsName}\t: {standardPrice[goodsName]}원---> {inputRateData}% DC({goodsPrice})원')    

# inputRateData = int(input('오늘의 할인율 입력: '))
# discountPrice = getDiscountPrice(inputRateData)
# printPrice(discountPrice)



# Q) 영어사전
englishDictionary = {
    'apple': '사과',
    'chair': '의자',
    'doll': '인형',
    'book': '책',
    'piano': '피아노',
    'clock': '시계',
}

def printWord(engWord):
    print(f'{engWord}: {englishDictionary[engWord]}')

printWord(input('찾고자 하는 영어 단어 입력: ')) 


