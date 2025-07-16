from __future__ import annotations

class Option():
    """Records a preference to a specific senario

    attributes:
        -- question: str
        -- rating: str
    """    
    question: str
    rating: str

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
    """
    date1: set[Option]
    date2: set[Option]
    date3: set[Option]

    def __init__(self):
        self.date1, self.date2, self.date3 = {}, {}, {}

class AV(Location):
    """
    AV | Extend superclass Location
    """
    date1: set[Option]
    date2: set[Option]
    date3: set[Option]

class Dining(Location):
    """
    Dining | Extend superclass Location
    """
    date1: set[Option]
    date2: set[Option]
    date3: set[Option]

class Library(Location):
    """
    Library | Extend superclass Location
    """
    date1: set[Option]
    date2: set[Option]
    date3: set[Option]

class Courtyard(Location):
    """
    Court | Extend superclass Location
    """
    date1: set[Option]
    date2: set[Option]
    date3: set[Option]

class Gym(Location):
    """
    Gym | Extend superclass Location
    """
    date1: set[Option]
    date2: set[Option]
    date3: set[Option]

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
    prefs: list[Location]

    def __init__(self, name: str):
        self.name = name
        self.prefs = [AV(), Dining(), Library(), Gym(), Courtyard()]

    def compare(self, other: Person):
        ...