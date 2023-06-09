# Напишите две функции. Первая принимает одно целое положительное число N и находит сумму всех цифр в числе. 
#Вторая принимает число N и считает количество цифр в числе. 
#В ответ выводится разность суммы чисел и количества.
# Пример работы программы
# Введите число: 500 
# Сумма чисел: 5
# Количество цифр в числе: 3
# Разность суммы и количества цифр: 2
def get_number_sum(number_input):
    result = 0
    number_string = str(number_input)
    for index in number_string:
        result += int(index)
    return result

def get_count_number(number_input):
    count = 1
    while number_input > 9:
        number_input //= 10
        count += 1
    return count

def make_difference(number_input):
    result = get_number_sum(number_input) - get_count_number(number_input)
    return result

number = int(input('Введите целое положительное число: '))
print('Сумма чисел: ', get_number_sum(number))
print('Количество цифр в числе: ', get_count_number(number))
print('Разность суммы и количества цифр: ', make_difference(number))