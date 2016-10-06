#!/usr/bin/env python3

import time, re, io, sys
import contextlib

def test_we_can_import_module():
    import printtime_cm

def test_context_manager_exists():
    import printtime_cm
    printtime_cm.printtime_cm

def test_context_manager_can_be_used():
    import printtime_cm
    with printtime_cm.printtime_cm():
        pass

def test_sleep_1():
    import printtime_cm

    tmp = io.StringIO()
    with contextlib.redirect_stdout(tmp):
        with printtime_cm.printtime_cm():
            time.sleep(1)

    out = tmp.getvalue()
    re.match(r'calculations took 1\..*s', out, re.IGNORECASE)

def test_sleep_nested():
    import printtime_cm

    tmp = io.StringIO()
    tmp2 = io.StringIO()
    with contextlib.redirect_stdout(tmp):
        with printtime_cm.printtime_cm():
            with contextlib.redirect_stdout(tmp2):
                with printtime_cm.printtime_cm():
                    time.sleep(1)
            time.sleep(1)

    out = tmp.getvalue()
    out2 = tmp.getvalue()
    re.match(r'calculations took 2\..*s', out, re.IGNORECASE)
    re.match(r'calculations took 1\..*s', out2, re.IGNORECASE)

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
