from contextlib import contextmanager
import sys


# Where does a context manager make sense?

# Setup/Preperation:
f = open('./text.txt', 'w')

# Do the stuff you want to do:
f.write('text')

# Clean up so everything is nice and tidy:
f.close()


# Context Manager as Class
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True


@contextmanager
def ContextFile(filename, method):
    try:
        file_obj = open(filename, method)
        yield file_obj
    except Exception:
        print("Exception has been handled")
    finally:
        file_obj.close()
        return True


# Context Manager as Generator
@contextmanager
def open_file(name, method):
    f = open(name, method)
    yield f
    f.close()


@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stout = oldstdout


with ContextFile('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

print('This goes to the console')
with open('./ContextManager.py', 'a') as f:
    with redirect_stdout(f):
        print('# This goes down there:')


# Really nice stuff:
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


@ignored(ZeroDivisionError)
def do_something_dangerous():
    1 / 0

do_something_dangerous()
# This goes down there:
