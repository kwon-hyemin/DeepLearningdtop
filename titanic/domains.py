# context, name, train , test, id, label
from dataclasses import dataclass


@dataclass
class Dataset:
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def fname(self) -> str: return self._fname

    @property
    def train(self) -> str: return self._train

    @property
    def test(self) -> str: return self._test

    @property
    def id(self) -> str: return self._id

    @property
    def label(self) -> str: return self._label

    @fname.setter
    def fname(self, fname): self._fname = fname

    @train.setter
    def train(self, train): self._train = train

    @test.setter
    def test(self, test): self._test = test

    @id.setter
    def id(self, id): self._id = id

    @label.setter
    def label(self, label): self._label = label
