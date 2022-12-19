import view
import data_base
import func
import csv_creater

def dialog():
  meaning = view.menu()
  return meaning

def add_contact():
  fsn = view.write_fsc()# Возрашает кортеж
  csv_creater.name_csv(fsn[0])
  csv_creater.family_csv(fsn[1])
  csv_creater.number_csv(fsn[2])
  data_base.write_base(fsn[0],fsn[1],fsn[2]) 
  
def search_contact():
  func.search_phon_book()

def del_contact():
  func.del_phon_book()
  
def print_t():
  view.print_table()
  
def read_csv():
  read = data_base.read_csv_base()
  print(read)