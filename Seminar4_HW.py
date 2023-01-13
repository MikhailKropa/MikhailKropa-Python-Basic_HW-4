# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import Random, randint

# number = int(input("Введите натуральную степень k: "))
# st = ""
# start = number
# f = open('dz4.txt', 'w')

# while start >= 0:
#     num = randint(0, 100)
#     if start > 1:
#         st += f'{num}x^{start}'
#     elif start == 1:
#         st += f'{num}x'
#     elif start == 0:
#         st += f'{num} = 0'
#     if start > 0:
#         st += ' + '
#     start -= 1

# f.write(str(st))
# f.close()

# print(st)



# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.



with open('file1.txt', "r") as file_one:
    lst1=file_one.readline()
    lst1=lst1.split('=')[0]
    print(lst1)
with open('file2.txt', "r") as file_second:
    lst2=file_second.readline()
    lst2=lst2.split('=')[0]
    print(lst2)

a, b, c    = lst1.split('+')
a = int(a[:a.index('*x')])
b=int(b[:b.index('*x')])
c=int(c)

i, j, k = lst2.split('+')
i = int(i[:i.index('*x')])
j=int(j[:j.index('*x')])
k=int(k)

with open('file3.txt', 'w') as file_tree:
    file_tree.write(f'{(a+i)}*x^2+{b+j}*x+{c+k}') # Не знаю, нужно ли степени складывать у многочлена. 





