my_dict = {'Vova':1992, 'Nastya':1987, 'Lera':2008, 'Vasilisa':2022}
print(my_dict)
print(my_dict.get('Vasilisa'))
print(my_dict.get('Alex'))
my_dict.update({'Alex':1961, 'Lara':1965})
del_ = my_dict.pop('Vova')
print(del_)
print(my_dict)

my_set = {1, 2, 3, 1, 2, 2, 1, 'камень', 'ножницы', 'камень', 'бумага'}
print(my_set)
my_set.discard('ножницы')
my_set.add('water')
print(my_set)