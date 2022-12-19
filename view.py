from prettytable import PrettyTable
import data_base


def get_print(data): # Метод вывода
  return print(data,end='')

def get_input():
  input_txt = input('-> ')
  return input_txt

def print_fcs(): # Метод вывода сообшения 
  print('Введите Имя, Фамилию и номер')
  
def write_name(): # Метод ввода имени
  name = input('Имя: ')
  name.capitalize()
  return name

def write_family(): # Метод ввода фамилии
  family = input('Фамилия: ')
  family.capitalize()
  return family

def phon_namder(): # Метод ввода номера
  number = int(input('Номер: '))    
  return number

def write_fsc():  # Метод ввода имени фамилии и номера
  name = write_name()
  family = write_family()
  number = phon_namder()
  return name,family,number

def menu():
  print('ТЕЛЕФОНАЯ  КНИГА')
  print('''
1. Добавить
2. Поиск
3. Удалить
4. Выход
''')
  oper = int(input('Введите число: '))
  return oper

def print_table():  # Выаод таблицы 
  mytable = PrettyTable()
  print('            Блокнот        ')
  mytable.field_names = ["Имя", "Фамилия", "Телефон"]
  temp = data_base.read_base()
  for i in temp:
    j = i.split()
    mytable.add_rows([j])
  print(mytable)