##### Test code for [this](https://stackoverflow.com/questions/29642249/what-happens-with-null-values-are-returned-from-foreign-functions-using-ctypes) stackoverflow article. #####

##### To build the shared object: #####
<code>cc -fPIC -shared -o libpython_ctypes_test.so python_ctypes_test.c</code>

##### To run: #####
<code>python python_ctypes_test.py</code>
