from sklearn.datasets import load_iris
import numpy as np  # 넘파이 패키지 임포트
import matplotlib.pylab as plt  # 맷플롯립 패키지 임포트
from sklearn.datasets import load_iris


class Iris:
    def __init__(self):
        self.iris = load_iris()
        self.x1 = np.array([[5.1], [3.5], [1.4], [0.2]])

    def main(self):
        print(self.iris.data[0, :])
        print('main')

    def solution(self):
        print(self.x1)



if __name__ == '__main__':
    Iris().main()
    Iris().solution()
