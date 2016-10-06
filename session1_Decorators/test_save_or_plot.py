#!/usr/bin/env python3

import sys, tempfile, os, subprocess
import numpy as np

def test_we_can_import_module():
    import save_or_plot

def test_context_manager_exists():
    import save_or_plot
    save_or_plot.save_or_plot

def test_context_manager_can_be_used():
    import save_or_plot
    with save_or_plot.save_or_plot('dummy'):
        pass

def test_context_manager_saves():
    import save_or_plot
    save_or_plot.SAVEFIGS = True

    with tempfile.TemporaryDirectory() as dirname:
        fname = dirname + '/out'
        with save_or_plot.save_or_plot(fname) as f:
            axes = f.add_subplot(111)
            axes.plot(np.random.random(100))
        assert os.path.exists(fname + '.svg')

def test_context_manager_shows():
    import save_or_plot
    save_or_plot.SAVEFIGS = False

    with tempfile.TemporaryDirectory() as dirname:
        fname = dirname + '/out'
        with save_or_plot.save_or_plot(fname) as f:
            axes = f.add_subplot(111)
            axes.plot(np.random.random(100))
        assert not os.path.exists(fname + '.svg')

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
