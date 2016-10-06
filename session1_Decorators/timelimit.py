"""
Exercise — context manager to limit computation time

The OS call alarm can be used to interrupt a process:

import signal
import time

def _handler(signum, frame):
    print('_handler called for signal', signum)

oldhandler = signal.signal(signal.SIGALRM, _handler)
signal.alarm(3)
time.sleep(100)

Write a context manager which limits the execution time
to the given number of seconds:

>>> with timelimit(5):
...     looong_computation()
RuntimeError         Traceback (most recent call last)
...
RuntimeError: over the deadline

Notes: signal.signal returns the *previous* handler that
was installed. It should be restored after our contextmanager
is done.

Some docs on the web:
http://stackoverflow.com/questions/8616630/time-out-decorator-on-a-multprocessing-function

https://docs.python.org/3/library/exceptions.html#RuntimeError
https://docs.python.org/3/library/signal.html#signal.alarm
https://docs.python.org/3/library/signal.html#signal.signal

http://linux.die.net/man/2/alarm
"""
