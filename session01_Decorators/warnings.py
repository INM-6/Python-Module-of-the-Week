"""
Warnings is a python module, which provides options to alert the user to some
condition in the programm without raising an exception or terminating the program.
For documentation see: https://docs.python.org/2/library/warnings.html
"""

import time
import warnings

# 1 Warnings ###################################################################

# raise a warning if outdated code is used
def outdated_function():
    """ This is an outdated function, which should not be used anymore"""
    warnings.warn("deprecated")
    return None

# execute function and check if a warning is displayed
#outdated_function()



# 2 Warning Categories #########################################################

# warnings can be of different categories
warning_categories= [Warning,
                     UserWarning,
                     DeprecationWarning,
                     SyntaxWarning,
                     RuntimeWarning,
                     FutureWarning,
                     PendingDeprecationWarning,
                     ImportWarning,
                     UnicodeWarning]

# not all warnings are automatically displayed as warnings are filtered by
# warning category before display.
def outdated_function():
    """ This is an outdated function, which should not be used anymore"""
    warnings.warn("deprecated", DeprecationWarning)
    return None

# execute function and check if a warning is displayed
#outdated_function()

# Warnings are filtered according to warning type befor they are displayed.
# DeprecationWarnings are not automatically displayed. You can change the
# filter setting like this:

warnings.simplefilter('always', DeprecationWarning)

def outdated_function():
    """ This is an outdated function, which should not be used anymore"""
    warnings.warn("deprecated", DeprecationWarning)
    return None

# execute function again and check if a warning is displayed now
#outdated_function()

accepted_filter_modes = ["error", "ignore" , "always" , "default", "module",
                         "once"]




# 3 Warning Stacklevel #########################################################

# Depending on the location, where you raise the warning you don't want to
# have the original line where the warning is raised as source of the
# warning, but an upstream reference (eg. the containing function)

for stack_level in [1,2,3]:
    print 'Using stacklevel %i'%stack_level

    def outdated_function():
        """ This is an outdated function, which should not be used anymore"""
        warnings.warn("deprecated", DeprecationWarning, stacklevel=stack_level)
        return None

    # execute function again and check the source location of the warning
    #outdated_function()

    # The order of warning and print statements does not need to be preserved
    # in the output. Waiting a bit helps in this demo to assign print and
    # warning messages
    time.sleep(1)
