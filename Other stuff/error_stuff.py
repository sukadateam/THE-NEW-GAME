import os
os.chdir('\\Users\\Brobi\\Desktop')
os.rename("Save.gsf","Save.py")
from Save import error_message
os.rename("Save.py","Save.gsf")
try:
  os.remove('Save.pyc')
except:
  pass
def windows_error(topic):
    if error_message==True:
        print("The system cannot find the file specified:",topic)
        print('Note: If you are not a developer please ignore this.')
def value_error():
    if error_message==True:
        print('System: ValueError. An incorrect input has been given.')
def unknown_error():
    if error_message==True:
        print('System: An unregistered error has occured.')
