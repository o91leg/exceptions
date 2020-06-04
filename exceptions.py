def calc (oper, x, y):

  operations = ('+', '-', '*' ,'/')
  res = 0

  try:
    assert oper in operations
  except AssertionError:
    print('Ошибка, неверный занк')

  try:
    x = int(x)
    y = int(y)
    if oper == '+':
      res = x + y
    elif oper == '-':
      res = x - y
    elif oper == '*':
      res = x * y
    elif oper == '/':
      res = x / y
    print('Ответ:', res)
  except ZeroDivisionError:
    print('Ошибка на ноль делить нельзя')
  except ValueError:
    print('Ошибка типа')

try:
  a, b, c = input('Введите выражение формата "+ 2 2 => " ').split()
except Exception as e:
  print('Аргументов больше 3х', e)


calc(a, b, c)