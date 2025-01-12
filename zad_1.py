class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("Anna", [60, 70, 80])
student2 = Student("Jan", [30, 40, 50])

print(f"Czy {student1.name} zdane? {student1.is_passed()}")
print(f"Czy {student2.name} zdane? {student2.is_passed()}")
