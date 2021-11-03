def windows_error(hi):
    print('System: Cannot find the file specified:',hi)
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
    print('System: There are no more lines to read.')
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
def environment_error(hi):
    print('Error: EnvironmentError')
    print('\nSystem: No information provided.')
    print('\nSystem Replay:',hi)
def i_o_error(hi):
    print('Error: IOError')
    print('\nSystem: No information provided.')
    print('\nSystem Replay:',hi)
def windows_error(hi):
    print('Error: WindowsError')
    print('\nSystem: No information provided. Only available in windows.')
    print('\nSystem Replay:',hi)
def blocking_io_error(hi):
    print('Error: BlockingIOError')
    print('\nSystem: Non-Blocking operation detected.')
    print('\nSystem Replay:',hi)
def child_process_error(hi):
    print('Error: ChildProcessError')
    print('\nSystem: Child Process has failed.')
    print('\nSystem Replay:',hi)
def connection_error(hi):
    print('Error: ConnectionError')
    print('\nSystem: Connection issue has occured. May sure what you are trying to connect to is accessible')
    print('\nSystem Replay:',hi)
def broken_pipe_error(hi):
    print('Error: BrokenPipeError')
    print('\nSystem: Attempted to write to pipe but the other end is closed.')
    print('\nSystem Replay:',hi)
def connection_aborted_error(hi):
    print('Error: ConnectionAbortedError')
    print('\nSystem: Connection attempt was aborted.')
    print('\nSystem Replay:',hi)
def connection_refused_error(hi):
    print('Error: ConnectionRefusedError')
    print('\nSystem: Connection attempt was denied.')
    print('\nSystem Replay:',hi)
def connection_reset_error(hi):
    print('Error: ConnectionResetError')
    print('\nSystem: Connection attempt was reset.')
    print('\nSystem Replay:',hi)
def warning(hi):
    print('Notice: Warning')
    print('\nSystem: A warning was called. No more information given.')
    print('\nSystem Replay:',hi)
def user_warning(hi):
    print('Notice: UserWarning')
    print('\nSystem: A warning was called for code created by a user.')
    print('\nSystem Replay:',hi)
def deprecation_warning(hi):
    print('Notice: DeprecationWarning')
    print('\nSystem: A warning was called for a feature that is depreciated.')
    print('\nSystem Replay:',hi)
def pending_deprecation_warning(hi):
    print('Notice: PendingDeprecationWarning')
    print('\nSystem: A warning was called for a feature that is going to be depreciated.')
    print('\nSystem Replay:',hi)
def syntax_warning(hi):
    print('Notice: SyntaxWarning')
    print('\nSystem: A warning was called for a suspicious syntax.')
    print('\nSystem Replay:',hi)
def runtime_warning(hi):
    print('Notice: RuntimeWarning')
    print('\nSystem: A warning was called for runtime behavior')
    print('\nSystem Replay:',hi)
def future_warning(hi):
    print('Notice: FutureWarning')
    print('\nSystem: A warning was called for deprecated features.')
    print('\nSystem Replay:',hi)
def import_warning(hi):
    print('Notice: ImportWarning')
    print('\nSystem: A warning was called about a probale mistake in module imports.')
    print('\nSystem Replay:',hi)
def unicode_warning(hi):
    print('Notice: UnicdoeWarning')
    print('\nSystem: A warning was called for a possible unicode issue.')
    print('\nSystem Replay:',hi)
def encoding_warning(hi):
    print('Notice: EncodingWarning')
    print('\nSystem: A warning was called for a possible encoding issue.')
    print('\nSystem Replay:',hi)
def bytes_warning(hi):
    print('Notice: BytesWarning')
    print('\nSystem: A warning was called for a problem related to bytes and bytearray.')
    print('\nSystem Replay:',hi)
def resource_warning(hi):
    print('Notice: ResourceWarning')
    print('\nSystem: A warning was called for a problem related to a resource issue.')
    print('\nSystem Replay:',hi)
#show_error on line 336 of main.py




#Add in future
def not_implemented_error(hi):
    print('Error: NotImplementedError')
def generator_exit(hi):
    print('Error: GeneratorExit')
def lookup_error(hi):
    print("Error: LookupError")
def buffer_error(hi):
    print('Error: BufferError')
def arithmetic_error(hi):
    print('Error: ArithmeticError')
def base_exception(hi):
    print('Error: BaseException')
def exception(hi):
    print('Error: Exception')
def file_exists_error(hi):
    print('Error: FileExistsError')
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


#Cannot be used
def floating_point_error():
    print('Error: FloatingPointError')
    print('Not currently used.')
