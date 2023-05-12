groupmates = [
    {
        "name": "Александр",
        "surname": "Каргашинский",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Руслан",
        "surname": "Магомедов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Иван",
        "surname": "Родичев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 4, 5]
    },
        {
        "name": "игорь",
        "surname": "Соломинов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
        {
        "name": "Михаил",
        "surname": "Мамонтов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 3, 4]
    },
        {
        "name": "Полина",
        "surname": "Тюрина",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 3, 3]
    },
            {
        "name": "Аня",
        "surname": "Поваркова",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 3]
    },
]

# Функция для вывода пользевутелю списка студентов
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
         student["surname"].ljust(10),
         str(student["exams"]).ljust(30),
         str(student["marks"]).ljust(20))
print_students(groupmates)
print()
print("Введите число от 1 до 5, по которому мы приведем фильтрацию студентов, чей средний балл равен или выше заданого вами числа")

# Функция для проверки ввода.
def get_number_user():
    while True:
        try:
            num = float(input("Введите число: "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
val_students = get_number_user()
        
#  Функция для фильтрации списка студентов, чей балл выше или равен заданому
def students_avg(students, n):
    """возвращает учащихся со средней оценкой > n"""
    # return filter(lambda s: sum(s['marks'])/len(s['marks']) > n, students)
    return [s for s in students if sum(s['marks'])/len(s['marks']) >= n]
 

print()
print("Список студентов, чей балл выше или равен заданому")
print_students(students_avg(groupmates, val_students))


