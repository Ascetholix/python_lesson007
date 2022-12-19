# Для коректной работы нужен интерпритатор python 3.7

import controller as c
import sys, subprocess

def clear(): 
  subprocess.run('cls', shell=True)

while True:
  c.print_t()
  dialog = c.dialog()
  if dialog == 4:
    break
  elif dialog == 1:
    c.add_contact()
  elif dialog == 2:
    clear()
    c.search_contact()
  elif dialog == 3:
    clear()
    c.del_contact()