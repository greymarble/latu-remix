from LATU_Obj import *
from LATU_Const import *

def create_student_obj(student: str) -> Person:
    """
    Create a person object of the student <student>. The Salmon data is included in 
    a <student>pref.csv file under the directory studentData. 


    csv file has 45 lines
    """
    with open(f'studentData/{student}pref.csv', 'r') as file:
        person = Person(file.readline().strip().split(',')[1])

        currLine = file.readline().strip()
        lineNum = 1

        locationIndex = 0
        dateIndex = 0

        while currLine:
            currLine = currLine.rsplit(',', maxsplit=1)

            prefMap = Option(currLine[0], currLine[1])
            person.prefs[locationIndex].dates[dateIndex].add(prefMap)
            # print(list(person.prefs[locationIndex].dates[dateIndex]))

            if lineNum % 3 == 0:
                dateIndex = (dateIndex + 1) % 3
            if lineNum % 9 == 0:
                locationIndex += 1

            lineNum += 1
            currLine = file.readline().strip()

        
        return person
    
def create_all_students() -> list[Person]:
    """
    Returns a list of all students as Person objects, containing 
    their preferences.
    """
    all_students = ['angie', 'gonta', 'himiko', 'k1-b0', 
                    'kaede', 'kaito', 'kirumi', 'kokichi', 
                    'korekiyo', 'maki', 'miu', 'rantaro', 
                    'ryoma', 'tenko', 'tsumugi']
    
    all_student_obj = []
    
    for student in all_students:
        all_student_obj.append(create_student_obj(student))

    return all_student_obj

def compare(one: Person, another: Person) -> int:
    """Return an integer that represents the compatibility score between 
    Person objects 'one' and 'another'.

    a returned value of <describe thresholds>
    """
    common_questions = get_common_questions(one, another)
    score = 0

def get_answers(student: Person, questions: list[str]) -> list[str]:
    """Return the list of student <student>'s ordered answers to the 
    given questions <questions>.
    """
    
    


def get_common_questions(one: Person, another: Person) -> list[str]:
    one_maps, another_maps = get_mappings(one), get_mappings(another)
    common = {}

    for item in one_maps.items():
        if item[0] in another_maps:
            common.update({item[0]: [item[1], another_maps[item[0]]]})

    return common

    
def get_mappings(student: Person) -> dict[str, str]:
    """
    Get the list of valid questions:preference mappings
    that student <student> has commented on.
    """
    mappings = {}

    for location in student.prefs:
        for date in location.dates:
            for option in date:
                mappings.update(option.to_dict())

    return mappings



def main():
    create_all_students()

if __name__ == '__main__':
    main()