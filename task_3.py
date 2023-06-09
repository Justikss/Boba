# Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1.

# Пример работы программы 1
# Введите число: 6
# Наименьший делитель, отличный от единицы: 2
# Пример работы программы 2
# Введите число: 17
# Наименьший делитель, отличный от единицы: 17
def smallest_divisor(number_input):
    for index in range(2, number_input + 1):
        if number_input % index == 0:
            return index
    return number_input  

number = int(input('Введите число: '))
print("Наименьший делитель, отличный от единицы:", smallest_divisor(number))
