#!/usr/bin/env python3

import sys, time
import pytest

def test_we_can_import_module():
    timelimit = pytest.importorskip('timelimit')

def test_context_manager_exists():
    timelimit = pytest.importorskip('timelimit')
    timelimit.timelimit

def test_context_manager_can_be_used():
    timelimit = pytest.importorskip('timelimit')
    with timelimit.timelimit(1):
        pass

def test_sleep_1():
    timelimit = pytest.importorskip('timelimit')

    with timelimit.timelimit(2):
        time.sleep(1)

def test_sleep_2():
    timelimit = pytest.importorskip('timelimit')

    with pytest.raises(RuntimeError):
        with timelimit.timelimit(1):
            time.sleep(2)

@pytest.mark.xfail
def test_sleep_nested():
    # We expect this test to fail, because there's only one alarm timer,
    # so we cannot nest them…
    timelimit = pytest.importorskip('timelimit')

    with pytest.raises(RuntimeError):
        with timelimit.timelimit(1):
            with timelimit.timelimit(5):
                time.sleep(2)

if __name__ == '__main__':
    pytest.main([__file__] + sys.argv[1:])
