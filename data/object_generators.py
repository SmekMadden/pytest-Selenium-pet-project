import random
from typing import Tuple

from data.data_generators import DataGenerator
from data.dataclasses.global_dc import Person


def generate_person(
    data_generator: DataGenerator,
    age_range: Tuple = (1, 99),
    salary_range: Tuple = (0, 999999),
):
    first_name = data_generator.gen_first_name()
    last_name = data_generator.gen_last_name()
    full_name = f"{first_name} {last_name}"

    return Person(
        first_name=first_name,
        last_name=last_name,
        full_name=full_name,
        age=random.randint(age_range[0], age_range[1]),  # noqa
        email=data_generator.gen_email(),
        current_address=data_generator.gen_address().replace("\n", " "),
        permanent_address=data_generator.gen_address().replace("\n", " "),
        salary=random.randint(salary_range[0], salary_range[1]),  # noqa
        department=random.choice(("Compliance", "Insurance", "Legal")),  # noqa
    )
