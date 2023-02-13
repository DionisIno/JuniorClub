from dataclasses import dataclass


@dataclass
class Person:
    username: str = None
    first_name: str = None
    last_name: str = None
    double_first_name: str = None
    double_last_name: str = None
    email: str = None
    password: str = None