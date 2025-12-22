# lab_python_fp/process_data.py
import json
import sys
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random


try:
    path = sys.argv[1]
except IndexError:
    print("Error: Путь к файлу не передан. Используется дефолтный 'data_light.json'")
    path = 'data_light.json'

try:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: Файл {path} не найден.")
    data = []

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=lambda x: x.lower())

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return list('{}, зарплата {} руб.'.format(job, salary) for job, salary in zip(arg, salaries))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
