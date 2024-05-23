import time
from datetime import datetime


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Function start in {time.strftime("%H:%M:%S", time.localtime())}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function end in {time.strftime("%H:%M:%S", time.localtime())}\n")
        print(f"""Function {func.__name__} work {
              end_time - start_time} seconds to run.""")
    return wrapper


@timing_decorator
def my_function():
    print('Hello world')
    time.sleep(1)


my_function()
