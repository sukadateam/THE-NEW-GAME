import os, sys
os.chdir('\\Users\\Brobi\\Desktop')
os.rename("Save.gsf","Save.py")
from Save import error_message
os.rename("Save.py","Save.gsf")
try:
  os.remove('Save.pyc')
except:
  pass
def windows_error(topic):
  print("The system cannot find the file specified:",topic)
  print('Note: If you are not a developer please ignore this.')
def value_error():
  print('System: ValueError. An incorrect input has been given.')
def unknown_error():
  print('System: An unregistered error has occured.')
def keyboard_interrupt():
  print('Error: keyboardInterrupt')
  print('System: The interrupt key was pressed.')
  print('Interrupt keys: control-c or delete')
def name_error():
  print('Error: name_error')
  print('System: Local or Global name is not found.')
  print('The program tried to find it but returned an error.')
def memory_error():
  print('Error: MemoryError')
  print('System: Memory is full.')
  print('Try closing other applications that are not needed.')
def assertion_error():
  print('Error: AssertionError')
  print('System: A debugging assert statement failed')
def attribute_error():
  print('Error: AttributeError')
  print('System: Could not assign to a variable.')
  print('May be a different mode. Ex: int, str, float, bool.')
def eof_error():
  print('Error: EOFError')
  print('System: There are no more lines to read.')
def import_error():
  print('Error: ImportError')
  print('System: Cannot load module from file.')
  print('Item may not exist.')
def show_error():
    if error_message==True:
      ex, ex_value, ex_traceback = sys.exc_info()
      ex=str(ex)
      ex=ex[8:len(ex)-2]
      print('Error:',ex)
      if ex=="ValueError": value_error()
      elif ex=="WindowsError": windows_error()
      elif ex=="KeyboardInterrupt": keyboard_interrupt()
      elif ex=="NameError": name_error()
      elif ex=="MemoryError": memory_error()
      elif ex=="AssertionError": assertion_error()
      elif ex=="AttributeError": attribute_error()
      elif ex=="EOFError": eof_error()
      elif ex=="ImportError": import_error()
      else: unknown_error()
