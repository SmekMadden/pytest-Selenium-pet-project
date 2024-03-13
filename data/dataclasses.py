from dataclasses import dataclass


@dataclass
class Person:
    fullname: str | None = None
    email: str | None = None
    current_address: str | None = None
    permanent_address: str | None = None
