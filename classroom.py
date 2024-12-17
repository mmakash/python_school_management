class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.subjects = []
    def add_students(self,student):
        roll_no = f"{self.name}-{len(self.students)+1}"
        student.id = roll_no
        self.students.append(student)
    def add_subject(self,subject):
        self.subjects.append(subject)
    def semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_grade()
        