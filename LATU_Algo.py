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

def InsufficientDataError(Exception):
    def __str__(self) -> str:
        return '\'compare\' was called on people with no questions in commmon! What am I supposed to analyze!?'

def compare(one: Person, another: Person) -> tuple[int, int, int]:
    """Return an integer that represents the compatibility score between 
    Person objects 'one' and 'another'.

    Returns the confidence, the score, and the scaled score.

    a returned value of <describe thresholds>

    """
    common_questions = get_common_questions(one, another)
    score = 0
    #45 is the max number of options a given *student* can comment on.
    # they should have ONE question in common, right..?
    confidence = len(common_questions)/45
    if common_questions == 0:
        raise InsufficientDataError

    for map in common_questions.items():
        ans_set = map[1]
        if len(ans_set) == 1:

            el = list(ans_set)[0]
            if el == 'G' or el == 'R':
                score += 2
            # must be 'Y' or 'O'
            else:
                score += 1.5
        #len(ans_set) == 2
        elif ('Y' in ans_set and 'G' in ans_set) or ('O' in ans_set and 'R' in ans_set):
            score += 1.75
        elif ('O' in ans_set and 'G' in ans_set) or ('Y' in ans_set and 'R' in ans_set):
            score += 0.25
        elif 'Y' in ans_set and 'O' in ans_set:
            score += 0.5
        #GR
        else:
            pass

    # print(f'confidence: {len(common_questions)/45}')
    # print(f'score: {score}')
    return confidence, score, score * confidence

def rank_all(students: list[Person]):
    """
    Compare all the students and rank them by 
    """
    rankBy = print('Rank by score \'S\' or confidence \'C\'? ')
    while not rankBy == 'S' and not rankBy == 'C':
        print('please try again')
        rankBy = print('Rank by score \'S\' or confidence \'C\'? ')

def compare_all(students: list[Person]):
    
    ...
    


def compare_debug(one: Person, another: Person) -> int:
    """Return an integer that represents the compatibility score between 
    Person objects 'one' and 'another'.

    a returned value of <describe thresholds>

    """
    common_questions = get_common_questions(one, another)
    score = 0

    for map in common_questions.items():
        print(f'{map[0]} |', end='')

        ans_set = map[1]
        if len(ans_set) == 1:

            el = list(ans_set)[0]
            if el == 'G' or el == 'R':
                print(f'two {el}s. score += 2')
                score += 2
            # must be 'Y' or 'O'
            else:
                print(f'two {el}s. score += 1.5')
                score += 1.5
        #len(ans_set) == 2
        elif ('Y' in ans_set and 'G' in ans_set) or ('O' in ans_set and 'R' in ans_set):
            print(f'A: {list(ans_set)[0]}, B: {list(ans_set)[1]}. generally pos. score += 1.75')
            score += 1.75
        elif 'Y' in ans_set and 'O' in ans_set:
            print(f'A: {list(ans_set)[0]}, B: {list(ans_set)[1]}. slight conflict. score += 0.5')
            score += 0.5
        elif ('O' in ans_set and 'G' in ans_set) or ('Y' in ans_set and 'R' in ans_set):
            print(f'A: {list(ans_set)[0]}, B: {list(ans_set)[1]}. generally conflicting. score += 0.25')
            score += 0.25
        #GR
        else:
            print(f'A: {list(ans_set)[0]}, B: {list(ans_set)[1]}. SKULL.... score += 0')
            pass

    return score
        
        

def get_common_questions(one: Person, another: Person) -> dict[str]:
    one_maps, another_maps = get_mappings(one), get_mappings(another)
    common = {}

    for item in one_maps.items():
        if item[0] in another_maps:
            common.update({item[0]: {item[1], another_maps[item[0]]}})

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