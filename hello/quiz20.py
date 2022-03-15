import random
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from quiz00 import Quiz00
from domains import myRandom


class Quiz20:

    def quiz20list(self) -> str:
        return None

    def quiz21tuple(self) -> str:
        return None

    def quiz22dict(self) -> str:
        ls = [i + j for i in range(5) for j in range(5)]
        dt = {i + j for i in range(5) for j in range(5)}

        return None

    def quiz23listcom(self) -> str:
        print('---------- legacy ----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('---------- comprehension ----------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        a = [i if i == 0 or i == 0 else i for i in range(1)]
        b = [i if i == 0 or i == 0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = {i: j for i, j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        print(d1)
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)
        return d

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dt = {}
        for i in range(0, len(ls1)):
            print(type(f'타입: {ls1[i]}'))
            dt[ls1[i]] = ls2[i]
        print(dt)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dt = {}
        for i, j in enumerate(ls1):
            dt[j] = ls2[i]
        print(dt)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dt = {}
        for i, j in zip(ls1, ls2):
            dt[i] = j
        print(dt)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print(f'{i}위 : {j}')
            print('#' * 100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]

    def quiz25dictcom(self) -> str:
        # quiz06memberChoice() 를 import 해서 문제해결. 이것이 1명인데 5명 추출
        # scores 는 0 ~ 100점 사이에서 랜덤
        q = Quiz00()
        c = set([q.quiz06member_choice() for i in range(5)])
        while len(c) != 5:
            c.add(q.quiz06member_choice())
        students = list(c)
        scores = [myRandom(0, 101) for i in range(5)]
        return {i: j for i, j in zip(students, scores)}

    def quiz26map(self) -> str:
        a = [myRandom(0, 3) for i in range(3)]
        print(a)
        b1 = ['a', 'b', 'c', 'd']
        b2 = []
        for b1 in b1:
            b2.append(b1)
        print(b1)
        print(b2)
        b = [(i, j) for i, j in enumerate([b1])]
        print(b)
        c1 = ['정', '민']
        c = [c1 for i in range(2)]
        print(c)
        d1 = ['바', '보']
        d2 = ['1', '2']
        d = [(d1, d2) for i, j in enumerate([d2])]
        print(d)
        e1 = [1, 2, 3, 4, 5]
        e = [e1 for i in range(2)]
        print(e)

        print('------------------------------------------------------------------')

        f = ('권혜민', 48, 7, 4, 45)
        f1 = [0]
        f2 = [4]
        f3 = [2, 4]
        f4 = f*3
        f5 = len(f)
        print(f'{f1},{f2},{f3},{f4},{f5}')

        return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        '''
        a = [i if i == 0 or i ==0 else i for i in range()]
        b = [ i if i ==0 or i ==0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = ''.join([])
        e = {i:j for i, j zip (l1, l2)} 
        e2 = dict(zip(l1, l2))
        f = list(zip(l1, l2))
        '''
        return None

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        # dict1 = self.quiz27melon()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('C:/workspace/melon.csv', sep=',', na_rep='NaN')

    '''
    데이터프레임 문제 Q01.
    홀짝을 구분하는 리스트컴프리헨션과 zip()으로 딕셔너리를 결합시킨
    로직으로 작성하시오. 다음 결과가 출력되야 한다.
        a   b   c
    1   1   3   5
    2   2   4   6 

    '''

    def quiz29_pandas_df(self) -> object:
        d = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d, index=[1, 2])
        d2 = {"1": [1, 3, 5], "2": [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2, orient='index', columns=['a', 'b', 'c'])
        columns = [chr(i) for i in range(97, 100)]  # ['a','b','c']
        e = [i if i == 0 else i for i in range(1, 7)]
        d3 = {"1": [1, 3, 5]}
        d4 = {"2": [2, 4, 6]}

        df3 = pd.DataFrame.from_dict(d2, orient='index', columns=columns)
        print(df3)
        return None
