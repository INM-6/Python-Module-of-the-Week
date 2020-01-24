from dataclasses import dataclass, field, fields
from datetime import datetime
from pprint import pprint


@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int
    name: str
    gender: str
    salary: int = field(hash=False, repr=False, metadata={"units": "bitcoin"})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append((viewer_id, datetime.now()))


e1 = Employee(emp_id='3536465054',
              name='Rachel Hettinger',
              gender='female',
              salary=22,
              age=0x30,
              )

e2 = Employee(emp_id='4054646353',
              name='Martin Murchison',
              gender='male',
              salary=20,
              age=0x30,
              )

e1.access('Roger Wastun')
e1.access('Shelly Summers')
pprint(e1.viewed_by)
pprint(sorted([e1, e2]))
assignments = {e1: 'gather requirements', e2: 'write tests'}
pprint(assignments)
fields(e1)[3]
"""
"""


# Generated Code:
"""


from dataclasses import _HAS_DEFAULT_FACTORY


def __init__(
    self,
    emp_id: int,
    name: str,
    gender: str,
    salary: int,
    age: int,
    viewed_by: list = _HAS_DEFAULT_FACTORY,
) -> None:
    self.emp_id = emp_id
    self.name = name
    self.gender = gender
    self.salary = salary
    self.age = age
    self.viewed_by = list() if viewed_by is _HAS_DEFAULT_FACTORY else viewed_by


def __repr__(self):
    return (
        self.__class__.__qualname__
        + f"(emp_id={self.emp_id!r}, name={self.name!r}, gender={self.gender!r}, age={self.age!r})"
    )


def __eq__(self, other):
    if other.__class__ is self.__class__:
        return (self.emp_id, self.name, self.gender, self.salary, self.age) == (
            other.emp_id,
            other.name,
            other.gender,
            other.salary,
            other.age,
        )
    return NotImplemented


def __lt__(self, other):
    if other.__class__ is self.__class__:
        return (self.emp_id, self.name, self.gender, self.salary, self.age) < (
            other.emp_id,
            other.name,
            other.gender,
            other.salary,
            other.age,
        )
    return NotImplemented


def __le__(self, other):
    if other.__class__ is self.__class__:
        return (self.emp_id, self.name, self.gender, self.salary, self.age) <= (
            other.emp_id,
            other.name,
            other.gender,
            other.salary,
            other.age,
        )
    return NotImplemented


def __gt__(self, other):
    if other.__class__ is self.__class__:
        return (self.emp_id, self.name, self.gender, self.salary, self.age) > (
            other.emp_id,
            other.name,
            other.gender,
            other.salary,
            other.age,
        )
    return NotImplemented


def __ge__(self, other):
    if other.__class__ is self.__class__:
        return (self.emp_id, self.name, self.gender, self.salary, self.age) >= (
            other.emp_id,
            other.name,
            other.gender,
            other.salary,
            other.age,
        )
    return NotImplemented


def __hash__(self):
    return hash((self.emp_id, self.name, self.gender))

"""
