#!/usr/bin/env python3
# encoding: utf8
#
# This is a comment.
#
# Only developers read this text. Use it to make the internal mechanisms more
# clear for further development and maintenance!
#

'''
    This is a string literal as first statement in the file. This is the
    so-called module doc-string.

    Describe what the user (or external developers) can do with this module.
    Maybe explain the idea behind the offered API or generally the interface to
    the world outside of this file.
'''

3              # integer
4.5            # float
"another text" # string


class Foo:
    '''
    This is a superduper class that looks nice to the outside. The class offers
    bars and a baz.
    '''

    def bar(self, asdf):
        ''' bar(asdf) -> sdfg

        Opens the given asdf bar and returns the resulting sdfg
        '''
        print("Opening the %s-Bar..." % asdf)
        return 42

    def baz(self):
        ''' baz() -> None

        Does the foo.baz().
        '''
        pass

def myFunction(test):
    ' this is a function '
    return

if __name__ == "__main__":
    foo = Foo()
    result = foo.bar("INM-Coffee")
    print("-> %s" % result)


