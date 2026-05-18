# CRUD란 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)를 말한다.

dicContainer = {
    '이름': '홍길동',
    '나이': 25,
    '주소': '대전 중구',
    '취미': ['축구', '수영', '조깅'],
    '몸무게': 87.5
}
print(f'dicContainer: {dicContainer}')

# 삽입(Create)
dicContainer['연락처'] = '010-1234-5678'
print(f'dicContainer: {dicContainer}')

# 조회(Read)
print(f'이름: {dicContainer["이름"]}')

# 수정(Update)
dicContainer['몸무게'] = 50
print(f'몸무게: {dicContainer["몸무게"]}')

# 삭제(Delete)
del dicContainer['몸무게']
print(f'dicContainer: {dicContainer}')  
# 부가 기능들
# 아이템 개수 조회
print(f'아이템 개수: {len(dicContainer)}')

# 전체키 & 밸류 조회
# 전체키
dicKeys = dicContainer.keys()
print(f'dicKeys: {dicKeys}')

# 전체밸류
dicValues = dicContainer.values()
print(f'dicValues: {dicValues}')

# 키와 밸류를 한방에 조회
for key, val in dicContainer.items():
    print(f'key: {key}, val: {val}')



# create, read, update, delete
# + 부가 기능
# 아이템 개수 조회
# 전체키 & 밸류 조회
# 전체밸류
# 키와 밸류를 한방에 조회