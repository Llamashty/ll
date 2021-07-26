# Рекурсия - это вызов функции самой себя

# Рассмотрим на примере факториала
# факториал N - произведение всех целых чисел от 1 до N

# Например факториал 9:
# 9!= 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
# 9!= 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 9!= 9 * (8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
# 9!= 9 * factorial(8)

# факториал 2
# 2! = 2* factorial(1)
# 1! == 1

# В общем случае
# N * factorial(N-1)

def factorial(n):
    if n == 1:
        return 1 # возвращаем 1, без вычислений, условие выхода из рекурсии
    factorial_n_minus_1 = factorial(n = n-1)
    return n * factorial_n_minus_1


print(factorial(9))

# рекурсия часто используется для обхода деревьев
html_dom = { # это словарь словарей
    'html':{
        'head': {
            'title' : 'Kolobok',
        },
        'body' : {
            'h2' : 'Hello!',
            'div': 'Хочешь, я расскажу тебе сказку?',
            'p': 'Жили-были старик со старухой...',
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items(): # для каждого ключа и поддерева делай много раз
        if isinstance(sub_tree, dict):
            result = find_element(tree=sub_tree, element_name=element_name)
            if result:
                break
    else:
        result = None
    return result

res = find_element(tree=html_dom, element_name='title')
print(res)