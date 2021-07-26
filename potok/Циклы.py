# This is a sample Python script.
print('Hello!')
my_family_height = [
    ['mom', 168],
    ['dad', 186],
    ['iam', 200],
]
total_hight = my_family_height[0][1]
total_hight += my_family_height[1][1]
total_hight += my_family_height[2][1]
print('total height my family', total_hight)
print('Good night!')

# Цикл while - до тех пор пока
print('Hello!')
i = 1
while i < 10:
    i = i * 2
    print(i)
print('Good night')

# Число Фибаначи: записали 2 числа, каждое следующее равно смме 2-х предыдущих.
# 1,1,2,3,5,8,13,21...
f1, f2 = 1, 1
print(f1)
while f2 < 1000:
    print(f2)
    next_f2 = f1 + f2 # Можно: f1, f2 = f2, f1 + F2
    next_f1 = f2
    f1, f2 = next_f1, next_f2

# оператор else
    i = 1
    while i < 10: # до тех пор пока выполняется усливие
        i *= 2
        print(i)
else: # усливие стало ложным - выполняется else
    print('i >= 10')
print('Good night')

# оператор break - прекратить
my_pets = ['cat', 'dog', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('Proverka', pet)
    if pet == 'cat':
        print('Yea, cat!')
        break  # цикл завершится после нахождения кота
    i += 1
print('Good night')

# break + else
my_pets = ['dog', 'hamster', 'hamster', 'hamster', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('Proverka', pet)
    if pet == 'cat':
        print('Yea, cat!')
        break  # действует на весь оператор; цикл будет работать
        # пока условие не станет ложным
    i += 1
else:  # не сработает, если будет break; как только цикл закончится будет применен else
    print('Oh...nothing')
print('Good night')

# continue
my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
i = -1  # -1 потому что первым шагом мы увеличим на 1 и переменная будет равна о ,
# соотвественно первому в списке
while i < len(my_pets):
    i += 1
    if i == 2:  # мы не хотим чтобы данная переменная нам показывалась  (скунс же ну!)
        # и говорим программе переходить к следующей
        continue  # остаток кода не проверяется, сразу идет на проверку нового условия
    pet = my_pets[i]
    print('Proverka', pet)
    if pet == 'cat':
        print('Yea, cat!')
        break
print('Good night')

# else, break and continue - все вместе
f1, f2, count = 0, 1, 0
while f2 < 10000:
    count += 1
    if count > 27: # количество повторений кода (итераций)
        print('Итерации больше чем 27. Прерываюсь. ')
        break
    f1, f2 = f2, f1 + F2 # вычисление Фибаначи
    if f2 < 1000: # если число Фибананчи больше 1000 не выводим его print
        continue
    print(f2)  # не сработает если Фианачи меньше 1000
else: # сработает если не будет break
    print('Было', count, 'итераций')

# Цикл for
# Цикл for ("для каждого элемента")
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
print('Выход из цикла')

zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
letters_count = 0
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
    letters_count += len(animal)
    pass # ничего не делать
print('Всего букв', letters_count)

# принудительная остановка цикла - break
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
    if animal == 'elephant':
        print('Нашли слона :)')
        break
    print('Это не слон...')
print('Выход из цикла')

# опция else для цикла
zoo_pets = ['lion', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
    if animal == 'elephant':
        print('Нашли слона :)')
        break
    print('Это не слон...')
else: # не выполняется если сработал break
    print('Тут слона нет...')
print('Выход из цикла')

# пропуск остатка цикла - continue
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    if animal == 'skunk':
        continue
    print('У нас в руках ', animal)
print('Выход из цикла')

# все вместе
zoo_pets = [
    'lion', 'elephant', 'monkey',
    'skunk', 'horse'
]
for animal in zoo_pets:
    if animal == 'skunk':
        print('Фуууу....')
        continue
    print('Сейчас переменная animal указывает на ', animal)
    if animal == 'elephant':
        print('Нашли слона :)')
        break
    print('Это не слон...')
else:
    print('Тут слона нет...')
print('Выход из цикла')

# Изменять содержимое последовательности, по которой проходит цикл, не безопасно
zoo_pets = [
    'lion', 'elephant', 'monkey',
    'skunk', 'horse'
]
for animal in zoo_pets:
    print(animal)
    del zoo_pets[0]
print(zoo_pets)

# автоматическая распаковка содержимого списка/тьюпла
a, b = 1, 2
(a, b) = (1, 2)

for element in [(1, 2), (3, 4)]:
    a, b = element[0], element[1]
    print(a + b)
# можно записать так
for (a, b) in [(1, 2), (3, 4)]:
    print(a + b)

peir_list = [(1, 2), (3, 4), (5, 6)]
# peir_list = [(1, 2), (3, 4), (5, 6, 7)] произойдет ошибака переменных, много значений для распаковки,
# так же будет если не хватит значений peir_list = [(1, 2), (3, 4), (5, )]
for a, b in peir_list:
    print(a + b)

triple_list = [(1, 2, 3), (4, 5, 6)]
for a, b, c in triple_list:
    print(a, b, c)

# полезные функции
# for(i = 0); i < 10; i++) {
#   animal = zoo_pets[i];
#   print(i, animal);
# }

for i, animal in enumerate(zoo_pets): # выдает пары значений: номер элемента и сам элемент
    print(i, animal)

for i, animal in zoo_pets[::2]: # переборка через 1 элемент
    print(animal)

# генерация целочисленных последовательностей
for i in range(100, 600, 50): # начни со значения 100 до 600(не входит) с шагом 50( если не указывать, то шаг 1);
    # можно опустить все значения range(10) тогда получим все значения с 1 до 9
    print(i)

# не делать так!
zoo_pets = ['lion', 'monkey', 'skunk', 'horse', ]
for i in range(len(zoo_pets)): # выдает последовательность длинн
    animal = zoo_pets[i] # получаем значение с помощью индексации
    print(i, animal)

# вложенные циклы
zoo_pets = [
    'lion', 'elephant', 'monkey',
    'skunk', 'horse'
]
for animal in zoo_pets:
    for char in animal: # внутренний цикл идет по буквам каждого элемента
        print(char)
    print(animal) # вконце цикла печатает сам элемент
    # {l
    # i
    # o
    # n
    # lion
    # это один цикл, который будет произведен с каждым элементом списка

# цикл по словарям
zoo_pets_mass = {
    'lion': 300,
    'elephant': 5000,
    'skunk': 5,
    'horse': 400,
} # словарь неупорядочен, нет гарантии что результаты будут так же по порядку
total_mass = 0 # переменная накопитель
for animal in zoo_pets_mass: # animal = ключ
    mass = zoo_pets_mass[animal]
    print(animal, mass)
    total_mass += mass # проходит цикл, вес животных накапливается в этой переменной,
    # пока цикл не будет завершен;
    # далее печатаем общий вес
print('Общая масса животных ', total_mass)

total_mass = 0
for animal, mass in zoo_pets_mass.items(): # будет выдавать пары ключ - значение
    print(animal, mass)
  total_mass += mass
print('Общая масса животных ', total_mass)

total_mass = 0
for mass in zoo_pets_mass.values():  # будет выдавать только значение, без ключей
    print(mass)
    total_mass += mass
print('Общая масса животных ', total_mass)
