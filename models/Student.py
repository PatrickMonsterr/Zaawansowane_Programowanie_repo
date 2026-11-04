class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return (
            f"Student: {self.name}, marks: {self.marks}"
        )
