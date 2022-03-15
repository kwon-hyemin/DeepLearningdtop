from context.domains import Dataset
from context.models import Model
from icecream import ic


class TitanicView:
    model = Model()
    dataset = Dataset()

    def modeling(self, train, test):
        model = self.model

    def preprocess(self, train, test) -> object:
        pass
