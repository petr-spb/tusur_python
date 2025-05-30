#Типы данных

'''

    Тип данных	Пример значения	Определение в Python
    Целые числа	−30, −20, −10, 0, 1, 2, 3	int
    Вещественные числа	−10.6, −1.6, 0.0, 2.8	float
    Комплексные числа	−15j, 5+4j	complex
    Булевы значения	True, False	bool
    NoneType	None	None
    Строка	'abracadabra'	str
    Список	[1, 2, 3], ['a', 'b', 'c']	list
    Кортеж	('red', green, 'blue')	tuple
    Изменяемое множество	{'red', 'blue', 'white'}, {1, 3, 5, 7}	set
    Неизменяемое множество	{'red', green, 'blue'}, {2, 3, 4, 5}	frozenset
    Диапазон	0, 1, 2, 3, 4, 5	range
    Словарь	{'color': 'red', height: 30, wight: 50}	dict
    Байты	b'\x00\x00\x00'	bytes
    Байтовая строка	(b'\x00\x00')	bytearray
    Просмотр памяти	0x1577168f3a00	memoryview

'''

# Как узнать тип данных

a = 5
print(type(a))
# <class 'int'>
b = 10.3
b = 3. # Равнозначные значения
b = 3.0 # Равнозначные значения
и = .4 # Равнозначные значения
print(type(b))
# <class 'float'>
comp = 10j
print(type(comp))
# <class 'complex'>
d = True
print(type(d))
# <class 'bool'>
none = None
print(type(none))
# <class 'NoneType'>
e = 'Text'
print(type(e))
# <class 'str'>
ee = "Text1"
print(type(ee))
# <class 'str'>
spisok = [1,2,'f']
print(type(spisok))
# <class 'list'> Список
kort = (1,'b', True)
print(type(kort))
# <class 'tuple'> Кортеж
izm_mnozh = {'abc', 2, True}
print(type(izm_mnozh))
# <class 'set'> Изменяемое множество

neizm_mnozh = {'red', True, 2}
# Неизменяемое множество frozenset

# Диапазон range

slovar = {'color': 'red', 'weight': 5, 'True': False}
print(type(slovar))
# <class 'dict'> Словарь

bayt = b'\x00'
print(type(bayt))
# <class 'bytes'> bytes

byte_str = (b'\x00\x00')
print(type(byte_str))
# <class 'bytes'> Байтовая строка


# Приведение типов
a_str = '10'
print(type(a_str))
# <class 'str'>

a_str2int = int(a_str)
print(type(a_str2int))
# <class 'int'>

a_float = 10.3
print(type(a_float))
# <class 'float'>
a_float2int = int(a_float)
print(a_float2int)
# 10
print(type(a_float2int))
# <class 'int'>

# Функция int() конвертирует значение аргумента в целое число.
# Функция float() преобразует аргумент в вещественное число.