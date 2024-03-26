from dataclasses import dataclass


@dataclass
class Person:
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None
    age: int | None = None
    email: str | None = None
    current_address: str | None = None
    permanent_address: str | None = None
    salary: int | None = None
    department: str | None = None
