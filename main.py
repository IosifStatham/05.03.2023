def avg_grade_in_course(students, course):
    all_grades_in_course_final = 0
    qun = 0
    for el in students:
        all_grades_in_course = 0
        grad = el.grades
        keys = grad.keys()
        for key in keys:
        
           if key == course:
             val = grad.get(key)
             for number in val:
                 qun += 1
                 all_grades_in_course += number
        all_grades_in_course_final = all_grades_in_course + all_grades_in_course_final
    
    all_grades_in_course_final1 = all_grades_in_course_final / qun           
    return f'Cредняя оценка по курсам {course}: {all_grades_in_course_final1}'
        
def сomparison (people1, people2): 
    if (isinstance(people1, Lecturer) and isinstance(people2, Lecturer)) or (isinstance(people1, Student) and isinstance(people2, Student)):
       result_сomparison = average_rating(people1) > average_rating(people2)
       if result_сomparison == True:
          return (f'У  {people1.name} {people1.surname} средняя оценка выше чем у {people2.name} {people2.surname}')
       else:
          return (f'У  {people2.name} {people2.surname} средняя оценка выше чем у {people1.name} {people1.surname}')   
    else:
      return ('Введите только студентов или только преподавателей')


def average_rating(some_lecturer1):
    rating = []
    aver = some_lecturer1.grades
    rating = aver.values()
    average_rating_final = 0
    summ = 0
    qun = 0
    for i in rating:
        for b in i:
            summ += b
            qun += 1
    average_rating_final = summ/qun
    return average_rating_final       

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
        
    def __str__ (self):
        courses_in_progress1 = ', '.join(self.courses_in_progress)
        finished_courses1 = ', '.join(self.finished_courses)
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{average_rating(self)}\nКурсы в процессе изучения:{courses_in_progress1}\nЗавершенные курсы:{finished_courses1}'    
        return res 
        
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
        
    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}' 
        return res   
 
class Lecturer(Mentor):
    def __init__(self, name, surname, prof):
        super().__init__(name, surname, prof)
        self.grades = {}
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{average_rating(self)}'    
        return res
 
all_students = []

all_lecturer = []      
 
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
all_students.append(some_student)


some_student_1 = Student('Ruoy1', 'Eman1', 'your_gender')
some_student_1.courses_in_progress += ['Git']
some_student_1.finished_courses += ['Python']
all_students.append(some_student_1)
 
some_reviewer = Reviewer('Some', 'Buddy', 'Reviewer')
some_reviewer.courses_attached += ['Python']
 
some_reviewer_1 = Reviewer('Some1', 'Buddy1', 'Reviewer')
some_reviewer_1.courses_attached += ['Git']
 

 
some_lecturer = Lecturer('Buddy', 'Some', 'Lecturer')
some_lecturer.courses_attached += ['Python']
all_lecturer.append(some_lecturer)

some_lecturer_1 = Lecturer('Buddy1', 'Some1', 'Lecturer')
some_lecturer_1.courses_attached += ['Git']
all_lecturer.append(some_lecturer_1)



some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 6)

some_reviewer_1.rate_hw(some_student, 'Git', 9)
some_reviewer_1.rate_hw(some_student, 'Git', 6)
some_reviewer_1.rate_hw(some_student, 'Git', 7)

some_reviewer.rate_hw(some_student_1, 'Python', 9)
some_reviewer.rate_hw(some_student_1, 'Python', 8)
some_reviewer.rate_hw(some_student_1, 'Python', 7)

some_reviewer_1.rate_hw(some_student_1, 'Git', 9)
some_reviewer_1.rate_hw(some_student_1, 'Git', 8)
some_reviewer_1.rate_hw(some_student_1, 'Git', 6)




some_student.rate_lec(some_lecturer,'Python', 9)
some_student.rate_lec(some_lecturer,'Python', 8)
some_student.rate_lec(some_lecturer,'Python', 8)

some_student_1.rate_lec(some_lecturer_1,'Git', 9)
some_student_1.rate_lec(some_lecturer_1,'Git', 7)
some_student_1.rate_lec(some_lecturer_1,'Git', 6)




print(some_student.grades)
print('-------------------------------')
print(some_student_1.grades)
print('-------------------------------')
print(some_lecturer.grades)
print('-------------------------------')
print(some_lecturer_1.grades)
print('-------------------------------')
print(some_reviewer)
print('-------------------------------')
print(some_reviewer_1)
print('-------------------------------')
print(some_lecturer)
print('-------------------------------')
print(some_lecturer_1)
print('-------------------------------')
print(some_student)
print('-------------------------------')
print(some_student_1)
print('-------------------------------')
print(сomparison(some_student, some_student_1))
print('-------------------------------')
print(сomparison(some_lecturer, some_lecturer_1))
print('-------------------------------')
print(avg_grade_in_course(all_students, "Git"))
print('-------------------------------')
print(avg_grade_in_course(all_lecturer, "Git"))