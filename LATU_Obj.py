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

    def to_dict(self) -> dict[str, str]:
        return {self.question: self.rating}
        
    def __repr__(self):
        return f"{self.question}: {self.rating}"
    

class Location():
    """
    ABSTRACT | A given location in salmon team.
    You have three dates at a given location.

    This is an abstract class: 
    Do Not Instantiate!

    attributes: 
    - name: the name of the location
    - dates: contains the preference 
      mapping for each date.

    Representation Invariants:
    --- len(self.dates) == 3
    """
    name: str
    dates: list[set[Option]]

    def __init__(self, name: str):
        # initialize the three dates
        self.name = name
        self.dates = [set(), set(), set()]
        

    def __repr__(self) -> str:
        rep = f'\n{self.name}: '

        for i in range(len(self.dates)):
            rep += (f'\nDate {i}: ' + 
                    f'{list(self.dates[i])}')
            
        return rep

class Person(): 
    """
    A person in DRv3's LATU. 

    attributes:
        name: the person's name
        prefs: a collection of preferences 
        to given situations

    RI:
        len(self.prefs) <= 5
    """
    name: str
    prefs: list[Location]

    def __init__(self, name: str):
        self.name = name
        self.prefs = [Location('AV'), Location('Dining'), Location('Library'), Location('Gym'), Location('Courtyard')]

    def __repr__(self) -> str:
        return f'\n\n{self.name} | \n{self.prefs}'