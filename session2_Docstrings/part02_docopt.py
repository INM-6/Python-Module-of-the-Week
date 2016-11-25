#!/usr/bin/env python3
# encoding: utf8
#
# check out the interactive example on
# http://docopt.org/

'''
Usage: part02_docopt [-h|--help] do [--force] <something>
       part02_docopt [-h|--help] stop [--force] <something>

Options:
    --force         use the --force, Luke!
    -v, --verbose   be more chatty about what is going on
    -h, --help      print this text
'''


import docopt

from part03_doctest import *

if __name__ == '__main__':
    args = docopt.docopt(__doc__)

    print(args)

