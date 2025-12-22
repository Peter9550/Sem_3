from operator import itemgetter


class Student:
    def __init__(self, id, name, grade, group_id):
        self.id = id
        self.name = name
        self.grade = grade
        self.group_id = group_id


class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class StudentGroup:
    def __init__(self, group_id, student_id):
        self.group_id = group_id
        self.student_id = student_id


groups = [
    Group(1, 'Группа 101'),
    Group(2, 'Группа 102'),
    Group(3, 'Группа 103'),
    Group(11, 'Группа 201'),
    Group(22, 'Группа 202'),
    Group(33, 'Группа 203'),
]

students = [
    Student(1, 'Иванов', 4.5, 1),
    Student(2, 'Петров', 3.8, 2),
    Student(3, 'Сидоров', 5.0, 3),
    Student(4, 'Козлов', 4.2, 3),
    Student(5, 'Морозов', 3.5, 3),
]

students_groups = [
    StudentGroup(1, 1),
    StudentGroup(2, 2),
    StudentGroup(3, 3),
    StudentGroup(3, 4),
    StudentGroup(3, 5),
    StudentGroup(11, 1),
    StudentGroup(22, 2),
    StudentGroup(33, 3),
    StudentGroup(33, 4),
    StudentGroup(33, 5),
]


def get_one_to_many(students, groups):
    return [(s.name, s.grade, g.name)
            for g in groups
            for s in students
            if s.group_id == g.id]


def get_many_to_many(students, groups, students_groups):
    many_to_many_temp = [(g.name, sg.group_id, sg.student_id)
                         for g in groups
                         for sg in students_groups
                         if g.id == sg.group_id]

    return [(s.name, s.grade, group_name)
            for group_name, group_id, student_id in many_to_many_temp
            for s in students if s.id == student_id]


def solve_task_b1(one_to_many):
    return sorted(one_to_many, key=itemgetter(0))


def solve_task_b2(one_to_many, groups):
    res_unsorted = []
    for g in groups:
        g_students = list(filter(lambda i: i[2] == g.name, one_to_many))
        if len(g_students) > 0:
            res_unsorted.append((g.name, len(g_students)))

    return sorted(res_unsorted, key=itemgetter(1), reverse=True)


def solve_task_b3(many_to_many, students):
    res = {}
    for s in students:
        if s.name.endswith('ов'):
            s_groups = list(filter(lambda i: i[0] == s.name, many_to_many))
            s_group_names = [x for _, _, x in s_groups]
            res[s.name] = s_group_names
    return res


def main():
    one_to_many = get_one_to_many(students, groups)
    many_to_many = get_many_to_many(students, groups, students_groups)

    # Выполнение и вывод заданий
    print('Задание Б1')
    print(solve_task_b1(one_to_many))

    print('\nЗадание Б2')
    print(solve_task_b2(one_to_many, groups))

    print('\nЗадание Б3')
    print(solve_task_b3(many_to_many, students))


if __name__ == '__main__':
    main()
