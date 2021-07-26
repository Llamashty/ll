# простое определение функции def - определить

# def <имя_функции>(...):
#      <блок кода>

def some_func():
    print('Привет! Я функция')


for _ in range(10):  # 10 раз повторяем функцию
    some_func()

some_func()

my_list = [3, 14, 15, 92, 6]
for element in my_list:
    some_func()


# более сложное опредление фунции - параметры
def func_with_programs(poram):  # их может быть несколько
    print('Функцию вызвали с параметром', poram)


my_list = [3, 14, 15, 92, 6]
for element in my_list:
    print('Начало цикла')
    func_with_programs(element)
    print('Конец цикла')


def func_with_programs(poram):
    print('Функцию вызвали с параметром', poram)


my_list = [3, 14, 15, 92, 6]
for element in my_list:
    print('Начало цикла')
    func_with_programs(param=element)
    print('Конец цикла')


# возврат значения из функции

def power(number, pow):  # возведение number в степень pow
    print('Функцию вызвали с параметрами', number, pow)
    power_value = number ** pow
    return power_value


my_list = [3, 14, 15, 92, 6]
for element in my_list:
    result = power(element, 10)  # для каждого элмента степень 10
    print(result)
# можно написать так
for element in my_list:
    result = power(number=element, pow=element)
    print(result)


# если нет return то возвращается None

def some_func():
    print('я ничего не верну')


#  можно дописать return None, но итак в результате будет None
result = some_func()
print(result)


# можно возвращать несколько значений
def create_default_user():  # создаем пользователя по умолчанию
    name = 'Василий'
    age = 27
    return name, age  # return name, age, 35 будет ошибка распаковки, т.к. данных больше


# step over клавиша в отладчике  = не входить в функции;
# step into - входить внутрь функции

user_name, user_age = create_default_user()
# можно написать result = create_default_user()
print(user_name, user_age)  # результат распаковки Василий, 27


# print(result) # результат (Василий, 27)


# документирование
def my_function():
    """Не делаем ничего, но документируем.

    Нет, правда, эта функция ничего не делает.
    """
    pass


print(my_function.__doc__)

help(...)  # можно вписать сюда функцию,встроенную или нет


# и мы получим справочную информацию по ней в формате документа

def ff():
    """обьяснение как работает моя функция"""


ff()  # если мы ее вызовем,ничего не будет
# а вот если запросим помощь
help(ff)  # программа выдаст:


# Help on function ff in module __main__:
# ff()
#    обьяснение как работает моя функция

# динамическая типизация
def multiplay(number_1, number_2):
    print('Функцию вызвали с параметрами', number_1, number_2)
    value = number_1 * number_2
    return value


print(multiplay(number_1=42, number_2=27))  # функция сработает как надо
print(multiplay(number_1='привет', number_2=34))  # функция сработает, в данном случае, но если,


# например, будет возведение в степень, то будет ошибка
# но так сработает хотя бы ошибка:

def multiplay(number_1, number_2):
    print('Функцию вызвали с параметрами', number_1, number_2)
    if isinstance(number_1, int):
        value = number_1 * number_2
        return value
    return 'Ошибка'


# параметры передаются как сслыка

def elephant_to_free(some_list):
    # elephant_found - булевая переменная которая может быть thue or folse
    elephant_found = 'elephant' in some_list  # оператор вхождения в список
    if elephant_found:
        some_list.remove('elephant') # удалить этот элемент из списка
        print('Слон на свободе!')
    return elephant_found


zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']
# если zoo = ('lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant') это неизменяемый обьект - тьюпл,
# то функция работать не будет! или же elephant_to_free(some_list=tuple(zoo)) что тоже не будет работать
# присваиваем zoo = some_list как внешняя и внутреняя функция
# в данном случае у нас 2 слона и функция будет работать 2 раза,
# а на третий уже ничего не произойдет
elephant_to_free(some_list=zoo) # elephant_found = True
print(zoo)

elephant_to_free(some_list=zoo) # elephant_found = True
print(zoo)

elephant_to_free(some_list=zoo) # elephant_found = False
print(zoo)