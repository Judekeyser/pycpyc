import ctypes
from .get_lib import get_lib


class StringSize:
    def __init__(self):
        c_lib = get_lib("pycpyc_string_size")
        self._cmethod = c_lib.pycpyc_string_size
        self._cmethod.restype = ctypes.c_int
        self._cmethod.argtypes = (ctypes.c_char_p,)
    
    def __call__(self, some_string: str) -> int:
        return self._cmethod(some_string.encode('utf-8'))


string_size = StringSize()
