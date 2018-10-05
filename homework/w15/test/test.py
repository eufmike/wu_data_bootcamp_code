# %%
import logging

# %%
# original concept about decorator
# add a function on foo()
def use_logging(func):

    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()   
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  
foo()       

# %%
# use @ replace the last line
def use_logging(func):
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()

# %%
# advanced decorator that pass arguments, which can be used 
# for conditional statement
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="info")
def foo(name='foo'):
    print("i am %s" % name)

foo()
# %%
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.info('So should this')