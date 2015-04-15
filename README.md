Test code for the stackoverflow article:
https://stackoverflow.com/questions/29642249/what-happens-with-null-values-are-returned-from-foreign-functions-using-ctypes

To build the shared object:
cc -fPIC -shared -o libpython_ctypes_test.so python_ctypes_test.c

To run:
python python_ctypes_test.py
