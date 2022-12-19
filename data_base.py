from pathlib import Path

def read_base(): # метод чтения файла
  file = Path('tel_directory.txt')
  with open(file, 'r', encoding='UTF-8') as data:
    return data.readlines()

def write_base(name,family,number): # Метод записы в файл
  file = Path('tel_directory.txt')
  with open(file, 'a', encoding='UTF-8') as data:
    data.write(f'{name} {family} {number}\n')
  
    
def clear_base(name,family,number):      #  Метод очистки файла
  file = Path('tel_directory.txt')
  with open(file, 'w', encoding='UTF-8') as data:
    data.write(f'{name} {family} {number}\n')
    
def read_csv_base(): # метод чтения файла
  file = Path('tel_book.csv')
  with open(file, 'r', encoding='UTF-8') as data:
    return data.readlines()
    