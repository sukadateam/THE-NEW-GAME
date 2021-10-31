#Added 
def windows_error(hi):
    print("System: Cannot find the file specified:",hi)
    print('\nNote: If you are not a developer please ignore this.')
def value_error(hi):
    print('Error: ValueError.')
    print('\nSystem: An incorrect input has been given.')
    print('\nSystem Replay:',hi)
def unknown_error(hi):
    print('System: An unregistered error has occured.')
    print('System Replay:',hi)
def keyboard_interrupt():
    print('Error: keyboardInterrupt')
    print('\nSystem: The interrupt key was pressed.')
    print('\nNote: Interrupt keys: control-c or delete')
def name_error(hi):
    print('Error: NameError')
    print('\nSystem: Local or Global name is not found.')
    print('\nNote: The program tried to find it but returned an error.')
    print('\nSystem Replay:',hi)
def memory_error():
    print('Error: MemoryError')
    print('\nSystem: Memory is full.')
    print('\nNote: Try closing other applications that are not needed.')
def assertion_error(hi):
    print('Error: AssertionError')
    print('\nSystem: A debugging assert statement failed')
    print('\nSystem Replay:',hi)
def attribute_error(hi):
    print('Error: AttributeError')
    print('\nSystem: Could not assign to a variable.')
    print('\nNote: May be a different mode. Ex: int, str, float, bool.')
    print('\nSystem Replay',hi)
def eof_error():
    print('Error: EOFError')
    print('\nSystem: There are no more lines to read.')
def import_error(hi):
    print('Error: ImportError')
    print('\nSystem: Cannot load module from file.')
    print('\nNote: Item may not exist.')
    print('\nSystem Replay:',hi)
def module_not_found(hi):
    print('Error: ModuleNotFoundError')
    print('\nSystem: Cannot locate module.')
    print('\nNote: Make sure item being called exists.')
    print('\nSystem replay:',hi)
def index_error(hi):
    print('Error: IndexError')
    print('\nSystem: Sequence subscript out of range.')
    print('\nNote: Possibly tried to call a part of var that doesn\'t exist.')
    print('\nSystem Replay:',hi)
def key_error(hi):
    print('Error: KeyError')
    print('\nSystem: Mapping(dictionary) key is not found in the existing set.')
    print('\nNote: Perhaps changing the input key.')
    print('\nSystem Replay:',hi)
def over_flow_error(hi):
    print('Error: OverflowError')
    print('\nSystem: Math operation is to large to be calculated/represented.')
    print('\nNote: Try using the round() function to solve this if possible.')
    print('\nSystem Replay:',hi)
def indentation_error(hi):
    print('Error: IndentationError')
    print('\nSystem: An unexpected indent has appeared.')
    print('\nSystem Replay:',hi)
def tab_error(hi):
    print('Error: TabError')
    print('\nSystem: Found an inconsistent use of tabs and spaces.')
    print('\nSystem Replay:',hi)
def system_error(hi):
    print('Error: SystemError')
    print('\nSystem: Internal error found. Not so serius error.')
    print('\nSystem Replay:',hi)
def type_error(hi):
    print('Error: TypeError')
    print('\nSystem: Operation or function cannot be applied to item specified.')
    print('\nSystem Replay:',hi)
def unbound_local_error(hi):
    print('Error: UnboundLocalError')
    print('\nSystem: Local variable in function/method has no assigned value.')
    print('\nSystem Replay:',hi)
def zero_division_error(hi):
    print('Error: ZeroDivisionError')
    print('\nSystem: Cannot divide by zero.')
    print('\nSystem Replay:',hi)
#show_error on line 86 of main.py



#Add in future
def file_exists_error(hi):
    print("Error: FileExistsError")
def file_not_found_error(hi):
    print('Error: FileNotFoundError')
def interrupted_error(hi):
    print('Error: InterruptedError')
def is_a_directory_error(hi):
    print('Error: IsADirectoryError')
def not_a_directory_error(hi):
    print('Error: NotADirectoryError')
def permission_error(hi):
    print('Error: PermissionError')
def process_look_up_error(hi):
    print('Error: ProcessLookupError')
def timeout_error(hi):
    print('Error: TimeoutError')
def unicode_translate_error(hi):
    print('Error: UnicodeTranslateError')
def unicode_decode_error(hi):
    print('Error: UnicodeDecodeError')
def unicode_encode_error(hi):
    print('Error: UnicodeEncodeError')
def unicode_error(hi):
    print('Error: UnicodeError')
def unbound_local_error(hi):
    print('Error: UnboundLocalError')
def system_error(hi):
    print('Error: SystemError')
def system_exit(hi):
    print('Error: SystemExit')
def stop_async_iteration(hi):
    print('Error: StopAsyncIteration')
def stop_iteration(hi):
    print('Error: StopIteration')
def runtime_error(hi):
    print('Error: RuntimeError')
def reference_error(hi):
    print('Error: ReferenceError')
def recursion_error(hi):
    print('Error: RecursionError')
