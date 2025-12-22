import unittest
from main import Student, Group, StudentGroup, get_one_to_many, get_many_to_many, solve_task_b1, solve_task_b2, \
    solve_task_b3


class TestRK2(unittest.TestCase):
    def setUp(self):
        self.groups = [
            Group(1, 'Группа А'),
            Group(2, 'Группа Б'),
            Group(3, 'Группа В'),
        ]

        self.students = [
            Student(1, 'Алексеев', 4.0, 1),  # Заканчивается на 'ев'
            Student(2, 'Борисов', 3.5, 2),  # Заканчивается на 'ов'
            Student(3, 'Ветров', 5.0, 1),  # Заканчивается на 'ов'
        ]

        self.students_groups = [
            StudentGroup(1, 1),
            StudentGroup(1, 3),  # Ветров в Группе А
            StudentGroup(2, 2),
            StudentGroup(2, 3),  # Ветров также в Группе Б (многие-ко-многим)
        ]

        self.one_to_many = get_one_to_many(self.students, self.groups)
        self.many_to_many = get_many_to_many(self.students, self.groups, self.students_groups)

    def test_task_b1(self):
        result = solve_task_b1(self.one_to_many)

        self.assertEqual(result[0][0], 'Алексеев')
        self.assertEqual(result[1][0], 'Борисов')
        self.assertEqual(result[2][0], 'Ветров')

    def test_task_b2(self):
        result = solve_task_b2(self.one_to_many, self.groups)
        expected = [('Группа А', 2), ('Группа Б', 1)]
        self.assertEqual(result, expected)

    def test_task_b3(self):
        result = solve_task_b3(self.many_to_many, self.students)

        self.assertNotIn('Алексеев', result)

        self.assertIn('Борисов', result)

        self.assertIn('Ветров', result)

        self.assertCountEqual(result['Ветров'], ['Группа А', 'Группа Б'])
        self.assertEqual(result['Борисов'], ['Группа Б'])


if __name__ == '__main__':
    unittest.main()
