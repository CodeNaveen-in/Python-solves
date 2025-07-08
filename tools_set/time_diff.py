import time

# Print current time for reference
print(time.time())

# Define the decorator
def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{function.__name__} run speed: {run_time}s")
    return wrapper

# Apply decorator to fast_function
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

# Apply decorator to slow_function
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# Run the functions
fast_function()
slow_function()