class EmptyArgsError(Exception):
    pass


class NoResultError(Exception):
    pass


# Функция
def drink_in_hot_day(*stroki, temp=5):
    if not stroki:
        raise EmptyArgsError('No arguments')
    for line in stroki:
        if not isinstance(line, str):
            raise TypeError ('Not all strings')
    stroki = list(filter(lambda x: len(x) > temp, stroki))
    stroki = sorted(stroki, key=lambda x: [len(x), x])
    if not stroki:
        raise NoResultError('Empty list')
    return stroki


data = ('narzan', 'borjomi', 'apricot', 'soda', 'baikal')
print(*drink_in_hot_day(*data))
data = ('tarragon', 'mojito', 'lime', 'orange', 'duchess')
print(drink_in_hot_day(*data, temp=8))