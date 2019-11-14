from babsonperson import BabsonPerson
from person import Person


class Student(BabsonPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        BabsonPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return BabsonPerson.speak(self, " Yo G, " + utterance)


class Grad(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


def main():
    s1 = UG("Arteen Zahiri", 2020)
    s2 = UG("Shirley Ying", 2020)
    s3 = UG("Shaun Tan", 2021)
    s4 = Grad("Matt Damon")

    studentList = [s1, s2, s3, s4]

    print(s1)

    print(s1.getClass())

    print(s1.speak("where is the quiz?"))

    print(s2.speak("I have no clue!"))

    print(s4.speak("I am not sure why I am here."))

    print(isStudent(s1))

    p1 = Person("Taylor Swift")
    print(isStudent(p1))


if __name__ == "__main__":
    main()