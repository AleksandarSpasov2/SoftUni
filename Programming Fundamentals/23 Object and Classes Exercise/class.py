class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0.00  # handle the case where there are no grades to avoid division by zero
        average_grade = sum(self.grades) / len(self.grades)
        return float(f"{average_grade:.2f}")

    def __repr__(self):
        students_str = ", ".join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students_str}. Average grade: {average_grade}"

