echo Building Example PKG

gcc -O3 -std=c17 -pedantic -Wall -Wextra -Werror -DPYCPYC_STRING_SIZE_IMPL -c c/src/pycpyc_string_size.c -o c/target/pycpyc_string_size.o
gcc -shared c/target/pycpyc_string_size.o -o c/target/pycpyc_string_size.so
export PYCPYC_LIB_LOCATION=/Users/justin.dekeyser/Documents/perso/justin/pycpyc/c/target
python build_support/check.py
