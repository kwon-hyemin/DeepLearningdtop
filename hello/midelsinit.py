from hello import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps


if __name__ == '__main__':
    while True:
        menu = input('0.Exit 1.계산기 (+, -,*,/) 2.bmi 3.Grade 4.AutoGrade 5.Dice '
                     '6.RandomGenerator 7.RandomChoice 8.Rps 9.GetPrime 10.LeapYear '
                     '11.NumberGolf 12.Lotto 13.Bank 14.Gugudan')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫번째 수')), str(input('연산자')), int(input('두번째 수')))
            res = f'{q1.num1} {q1.op} {q1.num2} = {q1.calc()}'
        elif menu == '2':
            m = Member()
            q2 = Quiz02Bmi()
            m.name = input('이름을 입력하세요')
            m.height = float(input('키를 입력하세요'))
            m.weight = float(input('몸무게를 입력하세요'))
            res = q2.getBmi(m)
            res = f' 이름 :{m.name}, 키: {m.height} 몸무게:{m.weight}  BMI 상태:{q2.getBmi(m)}'
        elif menu == '3':
            pass
        elif menu == '4':
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                res = i
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            # grade =Grade(name,kor,eng,math)
            # print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')
        elif menu == '5':
            res = f'{Quiz05Dice.cast()}'
        elif menu == '6':
            q6 = None
            res = f'{q6.ran()}'

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            res = f'{q7.choiceMember()}'
        elif menu == '8':
            q8 = Quiz08Rps(int(input('1.가위 2.바위 3.보')))
            res = f'User : {q8.rps[q8.user - 1]} Com:{q8.com - 1} 결과:{q8.battle()}'

        elif menu == '9':
            pass
        elif menu == '10':
            pass
        elif menu == '11':
            pass
        elif menu == '12':
            pass
        elif menu == '13':
            pass
        elif menu == '14':
            pass
        elif menu == '15':
            pass
        else:
            res = f'잘못된 선택입니다.'
        print(res)
