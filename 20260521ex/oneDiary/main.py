from config_dir.dir import config
from member import session
from db import member_db
from member import member_dumy
from db import diary_db
import copy
if config.DEV_MOD:
    member_dumy.dumyInit()
    print(f'memberDB: {member_db.memberDB}')
    print(f'diaryDB: {diary_db.diaryDB}')

flag = True

while flag:
    if session.signInedMemberId == '':
    # sign-out
        menuNum = int(input('1.sign-up  2.sign-in  6.write  7.read  99.end'))
    else:
    # sign-in
        menuNum = int(input('3.modify  4.delete  5.sign-out  6.write  7.read  99.end'))
    

    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('Please input new member ID: ')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')
       
        member_db.memberDB[uId] = {
            'uId' : uId,
            'uPw' : uPw,
            'uMail' : uMail,
            'uPhone' : uPhone
        }
           

        print('New member sign-up success!')

        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')
        # print(f'memberDB: {member_db.memberDB}')
        diary_db.diaryDB[uId] = []
        if config.DEV_MOD:
            print(f'diaryDB: {diary_db.diaryDB}')
        # print(f'diaryDB: {diary_db.diaryDB}')


    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('Please input member ID: ')
        uPw = input('Please input member PW: ')
        
        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!')
                session.signInedMemberId = uId
                
            else:
                print('sign-in fail!-- PW error')
        else:
            print('sign-in fail!-- ID error')
    
    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        # id, pw, mail, phone 이중에서 어떤 정보들만 수정가능하게 할 것인지 정해야 합니다.
        # id:x, 또한 이미 탈퇴한 회원의 id라도 절대 변경 사용할 수 없습니다. 
        # pw:절대 수정이 불가하지는 않습니다. 하지만 쉽게 변경할 수는 없습니다. 
        # mail:비교적 단순하게 수정할 수 있습니다.
        # phone:비교적 단순하게 수정할 수 있습니다.
        uPw = input('Please input member PW: ')
        uMail = input('Please input member MAIL: ')
        uPhone = input('Please input member PHONE: ')
        
        currentSignInedMemberID = session.signInedMemberId
        memberInfo = member_db.memberDB[currentSignInedMemberID]

        if config.DEV_MOD: print(f'memberInfo: {memberInfo}')

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD: print(f'after modify: memberInfo: {memberInfo}')

    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
        # 현재 로그인 되어 있는 ID를 session.signInedMemberId에서 가져와서
        # 해당하는 회원의 정보를 member_db.memberDB에 삭제 합니다.
        currentSignInedMemberID = session.signInedMemberId
        del member_db.memberDB[currentSignInedMemberID]
        print('Member info deleted!')
        session.signInedMemberId = ''
        if config.DEV_MOD: print(f'member_db.memberDB: {member_db.memberDB}')

    elif menuNum == config.SIGN_OUT:
        print('5.sign-out')
        print('sign-out success!')
        session.signInedMemberId = ''

    elif menuNum == config.DIARY_WRITE:
        print('6.write')
        if session.signInedMemberId == '':
            print('Sorry! Please sign-in!')
        else:
            while True: 
                diaryTxt = input('10글자 이하의 짧은 일기를 작성하세요')
                if len(diaryTxt) > 10:
                    print(f'10글자 초과 했어요.({len(diaryTxt)})')
                else:
                    diary_db.diaryDB[session.signInedMemberId].append(diaryTxt)
                    if config.DEV_MOD: print(f'diary_db.diaryDB: {diary_db.diaryDB}')
                    break

    elif menuNum == config.DIARY_READ:
        print('7.read')
        if session.signInedMemberId == '': 
            print('Sorry! Please sign-in!')
        else:
            currentSignInedMemberID = session.signInedMemberId
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]

            deepCopyedDiaries = copy.deepcopy(myDiaries)
            deepCopyedDiaries.reverse()
            print(f'deepCopyedDiaries: {deepCopyedDiaries}')

            for idx, diaryTxt in enumerate(deepCopyedDiaries):
                print(f'({idx+1}): {diaryTxt}')

    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False