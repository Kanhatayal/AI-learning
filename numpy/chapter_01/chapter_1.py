import numpy as np

# Converts a Python list into a NumPy array.
# Internally, NumPy performs the iteration in optimized C code. 
# This is called vectorization, and it's one of the main reasons NumPy is fast
marks = np.array([85, 90, 78])
print(marks)
print(type(marks))

new_marks = marks*1.1 
print(new_marks)
print(type(new_marks))

# file path we are working on 
print(np.__file__) 

# python version
print(np.__version__)