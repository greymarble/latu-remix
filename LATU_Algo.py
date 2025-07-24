from LATU_Obj import *

"""
    CREATING STUDENT + USER OBJECTS FOR COMPARISON
"""

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


"""
    COMPARISON FUNCTIONS
"""

def compare(one: Person, another: Person) -> tuple[int, int, int]:
    """Return an integer that represents the compatibility score between 
    Person objects 'one' and 'another'.

    Returns the confidence, and the score.

    a returned value of <describe thresholds>

    """
    common_questions = get_common_questions(one, another)
    score = 0
    #45 is the max number of options a given *student* can comme-nt on.
    # they should have ONE question in common, right..?
    confidence = len(common_questions)/45
    if common_questions == 0:
        raise InsufficientDataError

    for map in common_questions.items():
        ans_set = map[1]
        if len(ans_set) == 1:
            score += 2
             
        #len(ans_set) == 2
        elif ('Y' in ans_set and 'G' in ans_set) or ('O' in ans_set and 'R' in ans_set):
            score += 1.5
        elif 'Y' in ans_set and 'O' in ans_set:
            score += 0.5
        elif ('O' in ans_set and 'G' in ans_set) or ('Y' in ans_set and 'R' in ans_set):
            score += 0.25
        #GR
        else:
            pass

    # print(f'confidence: {len(common_questions)/45}')
    # print(f'score: {score}')
    return confidence, score

def rank_all(students: list[Person], focus: Person | str = None) -> list[tuple[tuple[Person, Person], tuple[int, int]]]:
    """
    Compare all the students and rank them by score or confidence.

    FULL NAME 
    """
    rankBy = input('Rank by score \'S\' or confidence \'C\'? ')

    while not rankBy == 'S' and not rankBy == 'C':
        print('please try again')
        rankBy = input('Rank by score \'S\' or confidence \'C\'? ')

    all_compare = compare_all(students)

    if focus:
        if isinstance(focus, Person):
            focus = focus.name
        
        all_compare = [elem for elem in all_compare if focus in elem[0]]


    if rankBy == 'S':
        #sort by score
        print('****** RANKING BY SCORE ******')
        all_compare.sort(key = lambda e: e[1][1], reverse=True)

        return all_compare
    else:
        print('****** RANKING BY CONFIDENCE ******')
        all_compare.sort(key = lambda e: e[1][0], reverse=True)

        return all_compare

def compare_all(students: list[Person]) -> list[tuple[tuple[Person, Person], tuple[int, int]]]:
    """
    """
    all = []

    i = 0
    for _ in range(len(students) - 1):
        currList = students[i:]

        for index in range(len(currList) - 1):
            # prefix = "\n\n" + f"{currList[0].name} and {currList[index + 1].name} | "

            people = (currList[0].name, currList[index + 1].name)
            comparison = compare(currList[0], currList[index + 1])

            all.append( (people, comparison) )

        i += 1

    return all

"""
    HELPER FUNCTIONS FOR COMPARISON
"""

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

def InsufficientDataError(Exception):
    def __str__(self) -> str:
        return '\'compare\' was called on people with no questions in commmon! What am I supposed to analyze!?'

"""
create user
"""             

def get_all_student_questions(students: list[Person]) -> list[str]:
    av, din, lib, gym, court = set(), set(), set(), set(), set()

    for student in students:
        for location in student.prefs:
            for i in range(len(location.dates)):
                for option in location.dates[i]:

                    # ...
                    if location.name == 'AV':
                        av.add(f'{option.question},{location.name},{i+1}')
                    elif location.name == 'Dining':
                        din.add(f'{option.question},{location.name},{i+1}')
                    elif location.name == 'Library':
                        lib.add(f'{option.question},{location.name},{i+1}')
                    elif location.name == 'Gym':
                        gym.add(f'{option.question},{location.name},{i+1}')
                    else:
                        court.add(f'{option.question},{location.name},{i+1}')
    
    all_q = []
    for loc in [av, din, lib, gym, court]:
        all_q.extend(_format_gasq(loc))

    return all_q

def _format_gasq(location: set) -> list[str]:
    l = list(location)
    l.sort(key=lambda elm: elm[-1])

    return l

def get_user_answers(questions: list[str]) -> list[str]:
    """
    Get the user's answers to the list of questions <questions>.
    """
    user_ans = []

    for i in range(len(questions)):
        q, loc, dateNum = questions[i].rsplit(',', maxsplit=2)

        ans = input(f'at the {loc}, on date {dateNum}: {q}: ').capitalize()

        while ans not in {'G', 'Y', 'R', 'O'}:
            ans = input(f'please try again. \nat the {loc}, on date {dateNum}: {q}: ').capitalize()

        user_ans.append(questions[i] + f',{ans}\n')

    return user_ans


def createUser(name: str) -> None:
    """Handles all 
    """
    with open(f'studentData/{name}pref.csv', 'w') as f:
        f.writelines(get_user_answers(get_all_student_questions(create_all_students())))

def readUserCSV(name: str) -> Person:
    with open(f'studentData/{name}pref.csv', 'r') as file:
        User = Person(name)

        currLine = file.readline().strip()
        prevLocation = ''
        prevDate = ''

        locIndex = 0
        dateIndex = 0

        while currLine:
            q, loc, date, ans = currLine.rsplit(',', maxsplit=3)
            
            if not prevLocation:
                prevLocation = loc
                prevDate = date
            else:
                if prevLocation != loc:
                    locIndex += 1
                    prevLocation = loc
                if prevDate != date:
                    dateIndex = (dateIndex + 1) % 3
                    prevDate = date

            User.prefs[locIndex].dates[dateIndex].add(Option(q, ans))

            currLine = file.readline().strip()

    return User

def main():
    ...

if __name__ == '__main__':
    main()