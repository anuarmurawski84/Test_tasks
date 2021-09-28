lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

# Найдем индексы для разбиения исходного списка 
def indexes_to_split(lst, days):

    target = sum(lst) // days
    indexes = []
    cost = 0
    start = 0
    print(target)

    for i, w in enumerate(lst):
        delta = target - cost
        cost += w
        if cost >= target:
            if i == 0 or cost - target <= delta:
                indexes.append((start, i+1))
                start = i+1
            elif cost - target > delta:
                indexes.append((start, i))
                start = i
            cost -= target
            if len(indexes) == days-1:
                indexes.append((start, len(lst)))
                break   
                
    return tuple(indexes)

# Найдем подсписки и выведем максимальный объем
def print_parts(lst, days):
    indexes = indexes_to_split(lst, days)
    print(f'Индексы исходного списка для разбиения: {indexes}')
    results = []
    for t in indexes:
        start, end = t
        sublist = lst[start:end]
        results.append(sum(sublist))
        print(f' - {sublist} сумма: {sum(sublist)}')
    print()
    print(f'Минимальный объём для выполнения условия:{max(results)}')

    
print_parts(lst, days)
