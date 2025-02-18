    #How memory is managed in Python?
import sys

# Function to show memory usage of an object
def show_memory(obj):
    print(f"Memory usage of {obj}: {sys.getsizeof(obj)} bytes")

a = [1, 2, 3, 4]  
b = a           
show_memory(a)  

del a           
show_memory(b)  
