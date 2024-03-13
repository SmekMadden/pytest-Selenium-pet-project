from data.data_generators import DataGenerator
from data.dataclasses import Person


def generate_person(data_generator: DataGenerator):
    return Person(
        fullname=data_generator.gen_full_name(),
        email=data_generator.gen_email(),
        current_address=data_generator.gen_address().replace("\n", " "),
        permanent_address=data_generator.gen_address().replace("\n", " "),
    )
