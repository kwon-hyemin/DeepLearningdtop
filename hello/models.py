import random
import statistics
from random import randrange, randint

from hello.domains import Member


class Quiz01Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        if self.op == '+':
            return self.num1 + self.num2
        elif self.op == '-':
            return self.num1 - self.num2
        elif self.op == '*':
            return self.num1 * self.num2
        elif self.op == '/':
            return self.num1 / self.num2


class Quiz02Bmi(object):
    @staticmethod
    def getBmi(Member):
        this = Member
        bmires = this.weight / (this.height * this.height) * 10000
        if bmires > 25:
            return f'비만'
        elif bmires > 23:
            return f'과체중'
        elif bmires > 18.5:
            return f'정상'
        else:
            return f'저체중'


class Quiz03Grade:
    def __init__(self, name, eng, kor, math):
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math

    def sum(self):
        return self.eng + self.kor + self.math

    def avg(self):
        return self.eng + self.kor + self.math / 3


class Quiz04GradeAuto:
    def __init__(self, name, eng, kor, math):
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math

    def sum(self):
        return self.eng + self.kor + self.math

    def avg(self):
        return self.eng + self.kor + self.math / 3

    def getGrade(self):
        pass

    def chkPass(self):
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz07RandomChoice(object):
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def choiceMember(self):
        ran = myRandom(0, 24)
        return self.members[ran]


class Quiz08Rps(object):
    def __init__(self, user):
        self.user = user
        self.rps = ['가위', '바위', '보']
        self.com = random.randint(1, 3)

    def battle(self):
        if self.user == self.com:
            return f'Draw'
        elif (self.user - 1) == self.com % 3:
            return f'Win'
        else:
            return f'Lose'


class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self):
        pass


class Quiz11NumberGolf(object):
    def __init__(self):
        pass


class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object):  # 책받침구구단
    def __init__(self):
        pass



