from __future__ import annotations
from collections import OrderedDict

class Option():
    """Records a preference to a specific senario

    attributes:
        -- question: str
        -- rating: str
    """    
    question: str
    rating: str

    def __init__(self, question: str = None, rating: str = None) -> None:
        self.question, self.rating = '', ''
        if question:
            self.question = question
        if rating: 
            self.rating = rating

    def set_question(self, quest: str) -> None:
        """
        Set the question for this Option instance.
        """
        self.question = quest

    def set_rating(self, rate: str) -> None:
        """
        Set the rating for this Option instance.

        precondition: rating is either 'G', 'Y', 'O', 'R"
        """
        self.rating = rate

    def __repr__(self):
        return f"{self.question}: {self.rating}"
    

class Location():
    """
    ABSTRACT | A given location in salmon team.
    You have three dates at a given location.

    This is an abstract class: 
    Do Not Instantiate!

    attributes: 
    - date1: set[Option]
    - date1: set[Option]
    - date1: set[Option]

    Representation Invariants:
    --- len(self.date1) ==
        len(self.date2) ==
        len(self.date3) ==
        3
        for the drv3 students
    """
    dates: list[set[Option]]

    def __init__(self):
        # initialize the three dates
        self.dates = [set(), set(), set()]

    def __repr__(self) -> str:
        rep = f'\n{type(self).__name__}: '

        for i in range(len(self.dates)):
            rep += (f'\nDate {i}: ' + 
                    f'{list(self.dates[i])}')
            
        return rep


class AV(Location):
    """
    AV | Extend superclass Location
    """
    dates: list[set[Option]]

class Dining(Location):
    """
    Dining | Extend superclass Location
    """
    dates: list[set[Option]]

class Library(Location):
    """
    Library | Extend superclass Location
    """
    dates: list[set[Option]]

class Gym(Location):
    """
    Gym | Extend superclass Location
    """
    dates: list[set[Option]]

class Courtyard(Location):
    """
    Court | Extend superclass Location
    """
    dates: list[set[Option]]


class Person(): 
    """
    A person in DRv3's LATU. 

    attributes:
        name: the person's name
        prefs: a collection of preferences to given situations

    RI:
        len(self.prefs) <= 5
    """
    name: str
    prefs: OrderedDict[str, Location]

    def __init__(self, name: str):
        self.name = name
        self.prefs = [AV(), Dining(), Library(), Gym(), Courtyard()]

    def compare(self, other: Person):
        ...