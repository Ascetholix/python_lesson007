import view
import data_base

def search_phon_book():  # Метод поиска
  view.print_fcs()
  sought = view.get_input()
  temp = data_base.read_base()
  for i in temp:
    i.lower()
    if sought in i:
      view.get_print(i)
  print()
      
def del_phon_book(): # Метод удаления контакта
  view.print_fcs()
  sought = view.get_input()
  temp = data_base.read_base()
  for i in temp:
    i.lower()
    if sought in i:
      temp.remove(i)
  for j in temp:
    fsn = j.split()
    print(fsn)
    data_base.clear_base(fsn[0],fsn[1],fsn[2])