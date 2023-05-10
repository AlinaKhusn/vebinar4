# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    num_lst = []
    count = 0
    while num > 0:
        x = num % 10
        count += 1
        num_lst.append(x)

        num = num // 10
    num_lst.reverse()

    s = []
    for i in range(10 ** (count - 1), 10 ** count):
        if i % 3 == 0:
            s.append(i)
    f = []
    for elem in range(len(s)):
        w = []
        while s[elem] > 0:
            x = s[elem] % 10
            w.append(x)
            s[elem] = s[elem] // 10
        w.reverse()
        f.append(w)
    number = []
    for u in range(len(f)):
        count2 = 0
        for y in range(count):
            if num_lst[y] == f[u][y]:
                count2 += 1
            if count2 >= count - 1:
                number.append(f[u])
    new_num = ''.join(map(str, number[-1]))
    new_num = int(new_num)
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')