# lab_python_fp/unique.py
from lab_python_fp.gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)  # Превращаем входные данные в итератор
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.items)  # Может выбросить StopIteration, что корректно завершит итерацию

            # Логика определения уникальности
            check_item = item
            if self.ignore_case and isinstance(item, str):
                check_item = item.lower()

            if check_item not in self.seen:
                self.seen.add(check_item)
                return item


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(10, 1, 3)
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print(list(Unique(data1)))
    print(list(Unique(data2)))
    print(list(Unique(data3, ignore_case=True)))
    print(list(Unique(data3, ignore_case=False)))
