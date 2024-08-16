import ctypes
import os
import platform

PYCPYC_LIB_LOCATION = os.environ["PYCPYC_LIB_LOCATION"]
PYCPYC_LIBS = dict()


def _extension():
    sys_name = platform.system()
    if sys_name == "Windows":
        return ".dll"
    elif sys_name == "Darwin" or sys_name == "Linux":
        return ".so"
    else:
        raise NotImplemented


def get_lib(library_name):
    if library_name not in PYCPYC_LIBS:
        location = os.environ["PYCPYC_LIB_LOCATION"]
        lib_location = os.path.join(location, library_name + _extension())
        library = ctypes.CDLL(lib_location)
        if library is not None:
            PYCPYC_LIBS[library_name] = library
    return PYCPYC_LIBS[library_name]
