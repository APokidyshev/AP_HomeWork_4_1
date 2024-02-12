# Задачи №№1-4 (с доработкой):
class Student:  # Студенты
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):  # Завершенные курсы у студентов
        self.finished_courses.append(course_name)
        print(f'Студент {self.name} {self.surname} завершил(а) курс(ы): {", ".join(course_name)}')

    def rate_lec(self, lecturer, course, grade):  # Студенты выставляют оценки лекторам
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # Вывод информации о студентах
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum([x for l in list(self.grades.values()) for x in l]) / len([x for l in list(self.grades.values()) for x in l])}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses[0])}\n'


class Mentor:  # Менторы (родительский класс)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):  # Лекторы (дочерний класс)
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):  # Вывод информации о лекторах
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum([x for l in list(self.grades.values()) for x in l]) / len([x for l in list(self.grades.values()) for x in l])}\n'


class Reviewer(Mentor):  # Эксперты (дочерний класс)
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):  # Эксперты выставляют оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # Вывод информации о экспертах
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


class Rates(float):  # Средние оценки студентов (за домашние задания), лекторов (за леции)
    def __init__(self, value):
        self.value = value

    def __eg__(self, other):  # Сравнение средних оценок студентов, лекторов
        return self.value == other.value

    def __gt__(self, other):  # Сравнение средних оценок студентов, лекторов
        return self.value > other.value
    # Также по аналогии могут быть добавлены и другие "магические методы" сравнения (например, __ne()__ или __lt()__), но для данной задачи они избыточны, т.к. фактически не внесут никакой новой информации при сравнении тех же значений


# def rat_comparison_lec(lec_name_1, lec_name_2): # Сравнение лекторов по средним оценкам - через операторы сравнения (доп. опция, в итоговом варианте решения задачи не используется)
#     rat_lec_1=sum([x for l in list(lec_name_1.grades.values()) for x in l])/len([x for l in list(lec_name_1.grades.values()) for x in l])
#     rat_lec_2=sum([x for l in list(lec_name_2.grades.values()) for x in l])/len([x for l in list(lec_name_2.grades.values()) for x in l])
#     if rat_lec_1>rat_lec_2:
#       print(f'Средняя оценка лектора {lec_name_1.name} {lec_name_1.surname} выше, чем у лектора {lec_name_2.name} {lec_name_2.surname}')
#     elif rat_lec_1<rat_lec_2:
#       print(f'Средняя оценка лектора {lec_name_1.name} {lec_name_1.surname} ниже, чем у лектора {lec_name_2.name} {lec_name_2.surname}')
#     elif rat_lec_1==rat_lec_2:
#       print(f'Средняя оценка лектора {lec_name_1.name} {lec_name_1.surname} равна средней оценке лектора {lec_name_2.name} {lec_name_2.surname}')


# def rat_comparison_stu(stu_name_1, stu_name_2): # Сравнение студентов по средним оценкам - через операторы сравнения (доп. опция, в итоговом варианте решения задачи не используется)
#     rat_stu_1=sum([x for l in list(stu_name_1.grades.values()) for x in l])/len([x for l in list(stu_name_1.grades.values()) for x in l])
#     rat_stu_2=sum([x for l in list(stu_name_2.grades.values()) for x in l])/len([x for l in list(stu_name_2.grades.values()) for x in l])
#     if rat_stu_1>rat_stu_2:
#       print(f'Средняя оценка студента {stu_name_1.name} {stu_name_1.surname} выше, чем у студента {stu_name_2.name} {stu_name_2.surname}')
#     elif rat_stu_1<rat_stu_2:
#       print(f'Средняя оценка студента {stu_name_1.name} {stu_name_1.surname} ниже, чем у студента {stu_name_2.name} {stu_name_2.surname}')
#     elif rat_stu_1==rat_stu_2:
#       print(f'Средняя оценка студента {stu_name_1.name} {stu_name_1.surname} равна средней оценке студента {stu_name_2.name} {stu_name_2.surname}')


def rat_av_stu(stu_name):  # Средняя оценка студента
    rats_stu = sum([x for l in list(stu_name.grades.values()) for x in l]) / len(
        [x for l in list(stu_name.grades.values()) for x in l])
    # print(f'Средняя оценка студента {stu_name.name} {stu_name.surname} равна: {rats_stu}')
    return rats_stu


def rat_av_lec(lec_name):  # Средняя оценка лектора
    rats_lec = sum([x for l in list(lec_name.grades.values()) for x in l]) / len(
        [x for l in list(lec_name.grades.values()) for x in l])
    return rats_lec


def rat_average_stu(students, course):  # Средняя оценка за домашние задания по каждому курсу
    stu_grades_list = []
    for stu_grade in stu_grades:
        course_grade = stu_grade.get(course)
        if course_grade != None:
            stu_grades_list.append(course_grade)
    rat_average = sum([x for l in stu_grades_list for x in l]) / len([x for l in stu_grades_list for x in l])
    print(f'Средняя оценка за домашние задания по курсу {course} составляет: {rat_average}')


def rat_average_lec(lecturers, course):  # Средняя оценка за лекции по каждому курсу
    lec_grades_list = []
    for lec_grade in lec_grades:
        course_grade = lec_grade.get(course)
        if course_grade != None:
            lec_grades_list.append(course_grade)
    rat_average = sum([x for l in lec_grades_list for x in l]) / len([x for l in lec_grades_list for x in l])
    print(f'Средняя оценка за лекции по курсу {course} составляет: {rat_average}')


# Создание объектов (студенты)
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_2 = Student('Ivan', 'Ivanov', 'Male')
student_3 = Student('Mary', 'Petrova', 'Female')
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Git']
student_3.courses_in_progress += ['Python', 'Git']
student_1_finished_courses = ['Введение в программирование', 'Основы SQL']
student_2_finished_courses = ['HTML', 'CSS']
student_3_finished_courses = ['Нет завершенных курсов']

# Создание объектов (лекторы)
lecturer_1 = Lecturer('Mr.', 'First')
lecturer_2 = Lecturer('Mr.', 'Second')
lecturer_3 = Lecturer('Mr.', 'Third')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Git']
lecturer_3.courses_attached += ['Python', 'Git']

# Создание объектов (эксперты)
reviewer_1 = Reviewer('Best', 'Reviewer')
reviewer_2 = Reviewer('Grand', 'Reviewer')
reviewer_3 = Reviewer('Super', 'Reviewer')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Git']
reviewer_3.courses_attached += ['Python', 'Git']

# ПРОВЕРКА ("ПОЛЕВЫЕ ИСПЫТАНИЯ")
# "Завершенные курсы у студентов (метод add_courses)"
print('ЗАВЕРШЕННЫЕ КУРСЫ У СТУДЕНТОВ:')
student_1.add_courses(student_1_finished_courses)
student_2.add_courses(student_2_finished_courses)
student_3.add_courses(student_3_finished_courses)
print()

# "Оценки студентам" (метод rate_hw)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_3.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_3.rate_hw(student_3, 'Python', 8)
print('СТУДЕНТЫ:')
print(student_1.name, student_1.surname, student_1.grades)
print(student_2.name, student_2.surname, student_2.grades)
print(student_3.name, student_3.surname, student_3.grades)
print()

# "Вывод информации о студентах (метод __str__)"
print(student_1)
print(student_2)
print(student_3)
print()

# "Средняя оценка студента (метод rat_av_stu)"
print(f'Средняя оценка студента {student_1.name} {student_1.surname} равна: {rat_av_stu(student_1)}')
print(f'Средняя оценка студента {student_2.name} {student_2.surname} равна: {rat_av_stu(student_2)}')
print(f'Средняя оценка студента {student_3.name} {student_3.surname} равна: {rat_av_stu(student_3)}')
print()

# "Сравнение студентов по средним оценкам" - через "магические методы"
rat_student_1 = Rates(rat_av_stu(student_1))
rat_student_2 = Rates(rat_av_stu(student_2))
rat_student_3 = Rates(rat_av_stu(student_3))

print('СРАВНЕНИЕ СТУДЕНТОВ ПО СРЕДНИМ ОЦЕНКАМ ЗА ДОМАШНИЕ ЗАДАНИЯ ("магические методы"):')
print(
    f'Средняя оценка студента {student_1.name} {student_1.surname} выше, чем средняя оценка студента {student_2.name} {student_2.surname}: {rat_student_1 > rat_student_2}')
print(
    f'Средняя оценка студента {student_2.name} {student_2.surname} выше, чем средняя оценка студента {student_3.name} {student_3.surname}: {rat_student_2 > rat_student_3}')
print(
    f'Средняя оценка студента {student_3.name} {student_3.surname} выше, чем средняя оценка студента {student_1.name} {student_1.surname}: {rat_student_3 > rat_student_1}')

print(
    f'Средняя оценка студента {student_1.name} {student_1.surname} равна средней оценке студента {student_2.name} {student_2.surname}: {rat_student_1 == rat_student_2}')
print(
    f'Средняя оценка студента {student_2.name} {student_2.surname} равна средней оценке студента {student_3.name} {student_3.surname}: {rat_student_2 == rat_student_3}')
print(
    f'Средняя оценка студента {student_3.name} {student_3.surname} равна средней оценке студента {student_1.name} {student_1.surname}: {rat_student_3 == rat_student_1}')
print()

# # "Сравнение студентов по средним оценкам (метод rat_comparison_stu)" - через операторы сравнения (доп. опция, в итоговом варианте решения задачи не используется)
# rat_comparison_stu(student_1,student_2)
# rat_comparison_stu(student_2,student_3)
# rat_comparison_stu(student_1,student_3)
# print()


# "Оценки лекторам" (метод rate_lec)
student_1.rate_lec(lecturer_1, 'Python', 10)
student_2.rate_lec(lecturer_1, 'Git', 10)
student_3.rate_lec(lecturer_2, 'Python', 8)
student_1.rate_lec(lecturer_3, 'Python', 10)
student_2.rate_lec(lecturer_2, 'Git', 8)
student_3.rate_lec(lecturer_1, 'Python', 10)
print('ЛЕКТОРЫ:')
print(lecturer_1.name, lecturer_1.surname, lecturer_1.grades)
print(lecturer_2.name, lecturer_2.surname, lecturer_2.grades)
print(lecturer_3.name, lecturer_3.surname, lecturer_3.grades)
print()

# "Вывод информации о лекторах (метод __str__)"
print(lecturer_1)
print(lecturer_2)
print(lecturer_3)
print()

# "Средняя оценка лектора (метод rat_av_lec)"
print(f'Средняя оценка лектора {lecturer_1.name} {lecturer_1.surname} равна: {rat_av_lec(lecturer_1)}')
print(f'Средняя оценка лектора {lecturer_2.name} {lecturer_2.surname} равна: {rat_av_lec(lecturer_2)}')
print(f'Средняя оценка лектора {lecturer_3.name} {lecturer_3.surname} равна: {rat_av_lec(lecturer_3)}')
print()

# "Сравнение лекторов по средним оценкам" - через "магические методы"
rat_lecturer_1 = Rates(rat_av_lec(lecturer_1))
rat_lecturer_2 = Rates(rat_av_lec(lecturer_2))
rat_lecturer_3 = Rates(rat_av_lec(lecturer_3))

print('СРАВНЕНИЕ ЛЕКТОРОВ ПО СРЕДНИМ ОЦЕНКАМ ЗА ЛЕКЦИИ ("магические методы"):')
print(
    f'Средняя оценка лектора {lecturer_1.name} {lecturer_1.surname} выше, чем средняя оценка лектора {lecturer_2.name} {lecturer_2.surname}: {rat_lecturer_1 > rat_lecturer_2}')
print(
    f'Средняя оценка лектора {lecturer_2.name} {lecturer_2.surname} выше, чем средняя оценка лектора {lecturer_3.name} {lecturer_3.surname}: {rat_lecturer_2 > rat_lecturer_3}')
print(
    f'Средняя оценка лектора {lecturer_3.name} {lecturer_3.surname} выше, чем средняя оценка лектора {lecturer_1.name} {lecturer_1.surname}: {rat_lecturer_3 > rat_lecturer_1}')

print(
    f'Средняя оценка лектора {lecturer_1.name} {lecturer_1.surname} равна средней оценке лектора {lecturer_2.name} {lecturer_2.surname}: {rat_lecturer_1 == rat_lecturer_2}')
print(
    f'Средняя оценка лектора {lecturer_2.name} {lecturer_2.surname} равна средней оценке лектора {lecturer_3.name} {lecturer_3.surname}: {rat_lecturer_2 == rat_lecturer_3}')
print(
    f'Средняя оценка лектора {lecturer_3.name} {lecturer_3.surname} равна средней оценке лектора {lecturer_1.name} {lecturer_1.surname}: {rat_lecturer_3 == rat_lecturer_1}')
print()

# # "Сравнение лекторов по средним оценкам (метод rat_comparison_lec)" - через операторы сравнения (доп. опция, в итоговом варианте решения задачи не используется)
# rat_comparison_lec(lecturer_1,lecturer_2)
# rat_comparison_lec(lecturer_2,lecturer_3)
# rat_comparison_lec(lecturer_1,lecturer_3)
# print()


# "Вывод информации о экспертах (метод __str__)"
print("ЭКСПЕРТЫ:")
print(reviewer_1)
print(reviewer_2)
print(reviewer_3)
print()

# "Средняя оценка за домашние задания по каждому курсу (метод rat_average_stu)"
stu_grades = [student_1.grades, student_2.grades, student_3.grades]
rat_average_stu(stu_grades, 'Python')
rat_average_stu(stu_grades, 'Git')
print()

# "Средняя оценка за лекции по каждому курсу (метод rat_average_lec)"
lec_grades = [lecturer_1.grades, lecturer_2.grades, lecturer_3.grades]
rat_average_lec(lec_grades, 'Python')
rat_average_lec(lec_grades, 'Git')
