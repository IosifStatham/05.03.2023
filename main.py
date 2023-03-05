class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and lecturer.prof == 'Lecturer':
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname, prof):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.prof = prof
        
class Reviewer(Mentor):
    def __init__(self, name, surname, prof):
        super().__init__(name, surname, prof)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
class Lecturer(Mentor):
    def __init__(self, name, surname, prof):
        super().__init__(name, surname, prof)
        self.grades = {}
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy', 'Reviewer')
cool_mentor.courses_attached += ['Python']
 
cool_mentor1 = Lecturer('Some1', 'Buddy1', 'Lecturer')
cool_mentor1.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lec(cool_mentor1,'Python', 9)

print(best_student.grades)
print(cool_mentor1.grades)

    

