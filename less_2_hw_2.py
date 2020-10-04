# Задание 2
"""
Даны три множества a, b, c. Необходимо выполнить все изученные виды бинарных операций
над всеми комбинациями множеств
"""

a = set('13579')
b = set('24569')
c = {()}

# Пересечение
aib = a.intersection(b)  # пересечение a, b
aic = a.intersection(c)  # пересечение a, c
bic = b.intersection(c)  # пересечение b, c
aibic = aib.intersection(c)  # пересечение a, b, c

# Объединение
aub = a.union(b)  # объединение a и b
auc = a.union(c)  # объединение a и c
buc = b.union(c)  # объединение b и c
aubuc = aub.union(c)  # объединение a, b и c

aubic = aub.intersection(c)
aibuc = aib.union(c)

# Разность
adb = a.difference(b)  # разность a\b
adc = a.difference(c)  # разность a\c
bda = b.difference(a)  # разность b\a
bdc = b.difference(c)  # разность b\с
cda = c.difference(a)  # разность c\a
cdb = c.difference(b)  # разность c\b

adbdc = adb.difference(c)
adcdb = adc.difference(b)
bdadc = bda.difference(c)
bdcda = bdc.difference(a)
cdadb = cda.difference(b)
cdbda = cdb.difference(a)

# Симметричкская разность
asdb = a.symmetric_difference(b)  # симметрическая разность a и b
asdc = a.symmetric_difference(c)  # симметрическая разность a и c
bsdc = a.symmetric_difference(c)  # симметрическая разность b и c
asdbsdc = asdb.symmetric_difference(c)

# функция вычисления декартова произведения
def decart(s1, s2):
    return[(a,b) for a in s1 for b in s2]

decart(a, b)
decart(b, a)
decart(a, c)
decart(c, a)
decart(b, c)
decart(c, b)
