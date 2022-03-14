from random import random

from hello import Member
from hello.domains import my100, myRandom, members, myMember


def member():
    return ['홍정명', '노홍주', '전종현', '정경준', '양정오',
            "권혜민", "서성민", "조현국", "김한슬", "김진영",
            '심민혜', '권솔이', '김지혜', '하진희', '최은아',
            '최민서', '한성수', '김윤섭', '김승현',
            "강 민", "최건일", "유재혁", "김아름", "장원종"]


class Quiz00:
    def quiz00calculator(self):
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        ran = myRandom(0, 4)

        if o[ran] == '+':
            print(self.add(a, b))
        elif o[ran] == '-':
            print(self.sub(a, b))
        elif o[ran] == '*':
            print(self.mul(a, b))
        elif o[ran] == '/':
            print(self.div(a, b))
        elif o[ran] == '%':
            print(self.mod(a, b))

        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        name = members()
        ran = myRandom(0, 23)
        print(name[ran])
        height = myRandom(100, 200)
        weight = myRandom(30, 100)
        res = weight / (height * height) * 10000

        if res > 25:
            print(f'비만{res}')
        elif res > 23:
            print(f'과체중{res}')
        elif res > 18.5:
            print(f'정상{res}')
        else:
            print(f'저체중{res}')

    def quiz02dice(self):
        return myRandom(1, 6)

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'
        print(res)
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        y = myRandom(2000, 2022)
        # s1 = "윤년" if y % 4 == 0 and y % 100 != 0 else "평년"
        # s2 = "윤년" if y % 400 == 0 else "평년"
        # s = "윤년" if y % 4 == 0 and y % 100 != 0 else "평년"
        # java style => String s = : () ? : ;
        # s3 = (y % 4 == 0 && y % 100 != 0) ? "윤년": (y % 400 == 0 ) ? "윤년" : "평년" ;
        # Python style => s = "" if else ""
        s = "윤년" if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "평년"

        print(f'{y}년은 {s}입니다.')
        return None

        pass

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.agv(kor, eng, math)
        grade = self.getGrade()
        self.passChk()
        return [sum, avg, grade, self.passChk]

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def grade(self):
        pass

    def passChk(self):  # 60점이상이면 합격
        pass

    def quiz06member_choice(self):

        return members()[myRandom(0, 23)]

    def quiz07lotto(self):

        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Acconunt.main()

    def quiz09gugudan(self):  # 책받침구구단
        pass


'''
08번 문제해결을 위한 클레스는 다음과 같다 
[요구사항 RFP]
은행 이름은 비트은행이다
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성한다.
123 - 12 - 123456
금액은 100 ~ 999 사이로 랜덤하게 입금된다 (단위는 만단위로 암묵적으로 판단한다)
'''


class Acconunt(object):
    def __init__(self, name, account_number, money):
        self.name = myMember() if name is None else name
        self.BANK_NAME = '비트은행'
        self.money = myRandom(100, 999) if money is None else money
        # self.a = f'{myRandom(0, 999) :0>3}-{myRandom(0, 99):0>2}-{myRandom(0, 999999):0>6}'
        self.account_number = Acconunt.create_account_number() if account_number is None else account_number

    def to_string(self):
        return f'은행 : {self.BANK_NAME} ' \
               f'입금자 : {self.name}' \
               f'계좌번호: {self.account_number} ' \
               f'금액: {self.money}만원'

    @staticmethod
    def create_account_number():
        # ls = [str(myRandom(0,999)) for i in range(1)]
        # ls.append("-")
        # ls += [str(myRandom(0, 99)) for i in range(1)]
        # ls.append("-")
        # ls += [str(myRandom(0, 999999)) for i in range(1)]
        #
        # return "".join(ls)
        return ''.join('-' if i == 3 or i == 6 else str(myRandom(0, 9)) for i in range(13))

    @staticmethod
    def find_account(ls, account_number):
        # return ''.join([j.to_string() if j.account_number == account_number else '찾는계좌없음' for i, j in enumerate(ls)])
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                return ls[i]


    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def deposit_account(ls, account_number, money):
        for x, y in enumerate(ls):
            if y.account_number == account_number:
                return ls[x]
        for i, j in enumerate(ls):
            if j.money == money:
                return ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0 종료 , 1. 계좌개설 2. 계좌내용 3. 입금 4. 출금 5. 계좌해지 6.계좌조회 7 테스트')
            if menu == '0':
                break
            if menu == '1':
                acc = Acconunt(None, None, None)
                print(f'{acc.to_string()} ... 개설되었습니다')
                ls.append(acc)
            elif menu == '2':
                # [print(Acconunt.to_string(i)) for i in ls]
                a = '\n'.join(i.to_string() for i in ls)
                print(a)
                # [Acconunt.main(i) for i in ls]
            elif menu == '3':
                # deposit = int(input('입금액'))
                # account_number = input('입금할 계좌번호')
                Acconunt.deposit_account(ls, input())


                print()
                # Acconunt.deposit_account(ls, int(input('입금액')))
                # 힌트 a.money + deposit
            elif menu == '4':
                input('출금할 계좌번호')
                money = input('출금액')
                # 추가 코드완성
            elif menu == '5':
                Acconunt.del_account(ls, input('탈퇴할 계좌번호'))
            elif menu == '6':

                print(Acconunt.find_account(ls, input('검색할 계좌번호')))
            elif menu == '7':
                pass
            else:
                print('Wrong Number.. Try Again')
                continue
