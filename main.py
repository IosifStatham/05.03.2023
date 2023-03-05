class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_Lectur(self, student, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
           if course in lecturer.grades:
               lecturer.grade[course] += [grade]
           else:
               lecturer.grade[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname, proff):
        self.name = name
        self.surname = surname
        self.proff = proff
        self.courses_attached = []
       
       
class Reviewer(Mentor): 
        def rate_hw(self, student, course, grade):
            if self.proff == "Reviewer":
                if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                    if course in student.grades:
                            student.grades[course] += [grade]
                    else:
                            student.grades[course] = [grade]
                else:
                    return 'Ошибка'
            else:
                return 'вы не можете ставить оценку'
class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}
 
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 

cool_reviewer= Reviewer('Some', 'Body', "Reviewer")
cool_reviewer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)


    

