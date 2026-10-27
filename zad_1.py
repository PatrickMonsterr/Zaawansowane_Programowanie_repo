class Student:
    def __init__(self, name: str, marks: list[float]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        return (sum(self.marks) / len(self.marks)) > 50


s1 = Student("Anna", [60, 70, 80])
s2 = Student("Jan", [10, 20, 30])

print(s1.is_passed())
print(s2.is_passed())
