# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки


names = ['Оля', 'Петя', 'Вася', 'Маша']
for item in names:
    print(item)

print()

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for item in names:
    print(f"{item}: {len(item)}")
print()

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша', 'Анаксимандр']
for item in names:
    if is_male.get(item, None) is True:
        print(item, '-', 'пол мужской')
    elif is_male.get(item, None) is False:
        print(item, '-', 'пол женский')
    else:
        print(f"{item} - такого имени нет в списке")

print()


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы.')

i = 1
for gr in groups:
    count_pupils_in_group = len(gr)
    print(f"Группа {i}: {count_pupils_in_group} ученика")
    i += 1

print()


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

i = 1
for gr in groups:
    gr_members = ", ".join(gr)
    print(f'Группа{i}: {gr_members}')
    i += 1


