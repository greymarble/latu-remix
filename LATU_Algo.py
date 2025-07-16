from LATU_Obj import Person
from LATU_Const import *

def init_all_empty() -> list[Person]:
    all_people = []

    for name in ...:
        all_people.append(Person(name))

    return all_people

def add_all_locations(all_people: list[Person]):
    for person in all_people:
        for location in ALL_LOCATIONS:
            person.add_location(location)


# compare function


def main():
    all_people = init_all_empty()
    add_all_locations(all_people)