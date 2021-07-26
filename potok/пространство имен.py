# Пространство имен (nomespace) - место где живут переменные

# Глобальное пространство имен

a, b = 1, 2
print('global', a+b)

def simple():
    print('simple: ', a + b)


simple()

# Локальное пространство - имена локальных в функции переменных

a, b = 1, 2
print('global', a+b)

def simple():
    # Локальное пространство имен появляется в момент вызова функции
    c, d = 3, 4
    print('simple: ', c + d)

def simple_2():
    # Локальное пространство имен
    x, y = 3, 4
    print('simple: ', x + y)
    # но если запросить переменные определенные другой функцией,
    # то будет ошибка print('simple: ', c + d)

#  Операторы управления потоком не дают локального пространства имен
if 2 > 1:  # если определить некую а = 0 и условие будет а>1,
    # то условие не сработает, е не будет определена
    # и второй print не сработает т.к. е не определен
    e, f = 5, 6
    print('if', e + f)
# но если поставить условие, при котором
# е будет всегда определен, то все будет работать:
# else:
#    e, f = 7, 8
print('global:', e + f)

# лучше определять значения до условий, чтобы программа сработала,
# если в течение условия они изменятся, тогда и значения поменяются

# для циклов
for elem in [1, 2, 3]: # если список пустой,
    # то elem не определен, цикл не работал
    # это можно обойти else
    print('for', elem)
    e, f = 5, 6
    # после break, икл пройдет 1 раз и он и будет последним
print('global:', elem) # после выхода из цикла указывает на последний
print('global:', e + f)
e, f = 0, 0


# перекрытие глобальных переменных
a, b = 1, 2
print('global', a+b) # будет равно 3

def simple():
    # Локальное пространство имен
    a, b = 3, 4 # переменная а затронет глобальную
    print('simple: ', a + b) # будет равно 7

simple()
print('global', a+b) # примененная функция, не заменит
# глобального значения и будет 3


# если переменной нет в локаьном namespace, то значение берется из глобального namespace
a, b = 1, 2
print('global', a+b) # будет равно 3

def simple():
    # Локальное пространство имен
    b = 4 # переменная b затронет глобальную
    print('simple: ', a + b) # будет равно 5

simple()
print('global', a+b) # примененная функция, не заменит
# глобального значения и будет 3


# если в функции есть присвоение - это будет локальная переменная

def simple():
    # Локальное пространство имен
    print('simple: ', a + b)
    a = 9 # будет оибка, тк. переменная определяется после применения
    print('simple: ', a + b)

# параметры - это локальные переменные
def simple_3(a, b):
    print('simple: ', a + b)

a, b = 2, 2
print('global', a + b)
simple_3(a=3, b=4)


# Способы вызова функции:
def vector_module(x, y, z):
    return(x**2 + y**2 + z**2) ** .5


# позиционные параметры
res = vector_module(2, 3, 4)
print(res)

# именованные параметры
res = vector_module(x=2, y=3, z=4)
print(res)

# если параметры именованны, порядок неважен
res = vector_module(z=4, y=3, x=2)
print(res)

# можно совмещеть
res = vector_module(2, 3, z=4)
print(res)


# можно потребовать чтобы параметры указывались явно
# это будут параметры, которые идут после *,
# соотвественно * перед всеми параметрами будет запрашивать указание всех

def vector_module(x, y, *, z):
    return(x**2 + y**2 + z**2) ** .5

# не пройдет
res = vector_module(2, 3, 4)

# все нормально
res = vector_module(2, 3, z=4)
res = vector_module(z=4, y=3, x=2)

# неправильные вызовы функций
res = vector_module() # нет параметров
res = vector_module(2, 3) # мало параметров
res = vector_module(2, 3, 3, 4) # много параметров
res = vector_module(x=2, y=3, y=4) # повтор параметров
res = vector_module(2, 3, x=4) # повтор параметра
res = vector_module(2, y=3, 4) # позиционный идет после именованного
res = vector_module(x=2, y=3, z=4, dist=4) # неизвестное имя

# распаковка параметров
some_list = [2, 3, 4]
res = vector_module(*some_list)
# x, y, z = args
# vector_module(2, 3, 4)
print(res)

# распаковка именованных параметров
some_dict = {'x' : 2, 'y' : 3, 'z': 4}
res = vector_module(**some_dict)
# vector_module(x=2, y=3, z=4)
print(res)

# можно совмещать
some_list = [2, 3]
some_dict = dict(z=4)
res = vector_module(*some_list, **some_dict)
#vector_module(2, 3, z=4)
some_list = [3, 4]
res = vector_module(2, *some_list)
print(res)


# параметры по умолчанию
def process(subject, action='мыла', object='раму'):
    print('Кто- ', subject)
    print('Делал(а) - ', action)
    print('Над чем - ', object)
    print('Получается: ', subject, action, object)

process(subject='Мама')
process(subject='Папа' action='сломал')
process(subject='Лось', action='видел', object='Ленина')

# значения по умолчанию вычисляются в точке определения функции, при компиляции
# обычная ошибка - изменяемый обьект в качестве параметра по умолчанию
def add_element_to_list(element, list_to_add=[]): # в этот момент создался пустой список,
    # не стоит так делать!
    """добавляем элемент к списку"""
    list_to_add.append(element)
    return list_to_add

my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

#new_list = add_element_to_list(element=1) мы не указываем список,
# в который нужно добавить элемент, значит по умолчанию самый первый
#print(new_list) получим [1]
#add_element_to_list(element=7, list_to_add=new_list)
#print(new_list) получим [1, 7]

#other_new_list = add_element_to_list(element=2) мы не указываем список,
# в который нужно добавить элемент, значит по умолчанию самый первый
#print(other_new_list) добавит к уже существующему [1, 7, 2]
#print(new_list) и этот выглядит теперь так же [1, 7, 2]
# print(new_list is other_new_list) будет True


# Но можно написать функцию так:
def add_element_to_list(element, list_to_add=None):
    """добавляем элемент к списку"""
    if list_to_add is None:
        list_to_add = []
    list_to_add.append(element)
    return list_to_add

my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list) # [1]

new_list = add_element_to_list(element=1) # будет создан новый список
print(new_list) # получим [1]
add_element_to_list(element=7, list_to_add=new_list)
print(new_list) # получим [1, 7]

other_new_list = add_element_to_list(element=2) # будет снова создан новый список
print(other_new_list) # получим [2]
print(new_list) # [1, 7] остается таким
print(new_list is other_new_list) # будет False


# Произвольное число параметров
print(1, 2, 3, 4, 5, 56, 6,)


# Произвольное число позиционных параметров
def print_them_all_v1(*args):
    print('print_them_all_v1')
    print('тип agrs: ', type(args))
    print(args)
    for i, arg in enumerate(args): # возвращает пары индекс-элемент
        print('позиционный параметр ', i, arg)

print_them_all_v1(2,'привет', 5.6)


# распаковка
my_favorite_pets = ['lion', 'elephant', 'monkey', 'cat', 'horse']
print_them_all_v1(my_favorite_pets) # позиционным параметром будет весь сисок и равен 0
print_them_all_v1(*my_favorite_pets) # все элементы списка распакуются по онмерам

# Произвольное число именованных параметров
def print_them_all_v2(**kwargs):
    print('print_them_all_v2')
    print('тип kwargs: ', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items(): # возвращает пары ключ-значение для свловарей
        print('именованный параметр ', key, value)

print_them_all_v2(name='Вася', address='Moscow')

# распаковка
my_friend = {'name': 'Вася', 'address': 'Moscow' , 'age': 25}
print_them_all_v2(**my_friend)

# неправильные вызовы
print_them_all_v1(name='Вася', address='Moscow')
print_them_all_v2('Вася','Moscow', 25)

# Комбинация
def print_them_all_v3(*args, **kwargs):
    print('print_them_all_v3')
    print('тип agrs: ', type(args))
    print(args)
    for i, arg in enumerate(args): # возвращает пары индекс-элемент
        print('позиционный параметр ', i, arg)
    print('тип kwargs: ', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items(): # возвращает пары ключ-значение для свловарей
        print('именованный параметр ', key, value)

print_them_all_v3('Вася', 'Moscow', 25) # заполнится первый тип,
# но еще создастся пустой словарь
print_them_all_v3(name='Вася', address='Moscow') # заполнится словарь,
# первый тип будет пустой

print_them_all_v3(1000, 'рублей', name='Вася', address='Moscow') # заполнятся все типы

# распаковка
my_friend = {'name': 'Вася', 'address': 'Moscow'}
print_them_all_v3(1000, 'рублей', **my_friend)

# При создании функции можно указывать как обычные параметры,
# так и произвольные параметры
def print_them_all_v4(a, b=5, *args, **kwargs):
    print('print_them_all_v4')
    print('a and b: ', a, b)
    print('тип agrs: ', type(args))
    print(args)
    for i, arg in enumerate(args): # возвращает пары индекс-элемент
        print('позиционный параметр ', i, arg)
    print('тип kwargs: ', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items(): # возвращает пары ключ-значение для свловарей
        print('именованный параметр ', key, '=', value)

print_them_all_v4(5, 6, 7, 8, cat='may!')
# a=5, b=6, args=7,8, kwargs=cat='may!'
print_them_all_v4(5, b=8, cat='may!')
#a=5, b=8, kwargs=cat='may!'
print_them_all_v4(5, cat='may!', address='Moscow')
# a=5, b=5, kwargs= cat='may!', address='Moscow'