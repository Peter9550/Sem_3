
def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            val = item.get(key)
            if val is not None:
                yield val
    else:
        for item in items:
            result_dict = {key: item.get(key) for key in args if item.get(key) is not None}
            if len(result_dict) > 0:
                yield result_dict


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стелаж', 'price': None, 'color': 'white'}
    ]

    print("--- 1 аргумент ---")
    for title in field(goods, 'title'):
        print(title)

    print("\n--- 2 аргумента ---")
    for item in field(goods, 'title', 'price'):
        print(item)
