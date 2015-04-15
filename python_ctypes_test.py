import ctypes
import ctypes.util

dll = ctypes.CDLL('libpython_ctypes_test.so')

class _test_struct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]
    
    def __init__(self):
        ctypes.Structure.__init__(self)
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        
    def wrap(self, something):
        self.a,self.b,self.c,self.d = something
        
    def unwrap(self):
        part1 = self.a,self.b
        part2 = self.c,self.d
        return part1, part2
    
dll.get_test_struct.restype = ctypes.POINTER(_test_struct)
dll.get_test_struct.argtypes = [ctypes.c_int]

def py_get_test_struct(valid):
    ctypesPtr = dll.get_test_struct(valid).contents
    return ctypesPtr.unwrap()

def py_get_test_struct_safe(valid):
    ctypesPtr = dll.get_test_struct(valid)
    if ctypesPtr: 
        return ctypesPtr.contents.unwrap()
    else:
        return None

dll.get_two_floats.restype = None
dll.get_two_floats.argtypes = [ctypes.c_int, 
        ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]

def py_get_two_floats(valid):
    float1 = ctypes.c_float(0.54545)
    float1_pointer = ctypes.pointer(float1)
    float2 = ctypes.c_float(0.76767)
    float2_pointer = ctypes.pointer(float2)
    
    dll.get_two_floats(valid, float1_pointer, float2_pointer)
    
    return float1.value, float2.value

print py_get_two_floats(True)
print py_get_two_floats(False)
print py_get_test_struct_safe(True)
print py_get_test_struct_safe(False)
print py_get_test_struct(True)
print py_get_test_struct(False)
