from abc import ABC, abstractmethod

from data.data_generators import DataGenerator, FakerGenerator


class DataGeneratorFactory(ABC):
    @abstractmethod
    def create_generator(self) -> DataGenerator:
        ...


class FakerGeneratorFactory(DataGeneratorFactory):
    def create_generator(self) -> DataGenerator:
        return FakerGenerator()
