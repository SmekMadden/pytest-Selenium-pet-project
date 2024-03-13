from abc import ABC, abstractmethod

from faker import Faker

# Strategy pattern


class DataGenerator(ABC):
    @abstractmethod
    def gen_full_name(self):
        ...

    @abstractmethod
    def gen_email(self):
        ...

    @abstractmethod
    def gen_address(self):
        ...


class FakerGenerator(DataGenerator):
    def __init__(self):
        self.fake = Faker()

    def gen_full_name(self):
        return self.fake.name()

    def gen_email(self):
        return self.fake.email()

    def gen_address(self):
        return self.fake.address()
