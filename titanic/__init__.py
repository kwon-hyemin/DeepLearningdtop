import pandas as pd
# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.models import TitanicModel
from titanic.views import TitanicView

if __name__ == '__main__':
    def print_menu():
        return '1.템플릿 2.모델 3. 러닝'


    while 1:
        menu = input(print_menu())
        if menu == '1':
            print(' #### 1. 템플릿 #### ')
            templates = TitanicModel('train.csv')
            templates.visualize()
        elif menu == '2':
            print(' #### 2. 모델 #### ')
            model = TitanicModel()
            model.preprocess(train='train.csv', test='test.csv')

        elif menu == '3':
            print(' #### 3. 러닝 #### ')
            model = TitanicModel()
            model.learning(train='train.csv', test='test.csv')
        break
