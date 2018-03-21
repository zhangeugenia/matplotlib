import numpy as np
import pytest

import warnings

import matplotlib.pyplot as plt
from matplotlib.cbook import (
    IgnoredKeywordWarning, MatplotlibDeprecationWarning)

# Sanity checking _replace_plot_args()

def test__plot_args_replacer_onearg():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])

    # should be [y] regardless of type of data    
    assert _plot_args_replacer(('y'), [1,2,3]) == ['y']
    assert _plot_args_replacer(('ones'), [1,2,3]) == ['y']
    
    assert _plot_args_replacer(('y'), pts) == ['y']
    assert _plot_args_replacer(('m'), pts) == ['y']


def test__plot_args_replacer_twoarg():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])

    # [x, y] and [y, c?] with regular data
    assert _plot_args_replacer(('x', 'y'), [1,2,3]) == ['x', 'y']
    assert _plot_args_replacer(('ones', 'twos'), [1,2,3]) == ['y', 'c']
    
    # [x, y] and [y, c?] with structured data
    assert _plot_args_replacer(('x', 'y'), pts) == ['y', 'c']
    assert _plot_args_replacer(('ones', 'twos'), pts) == ['x', 'y']

def test__plot_args_replacer_manyarg():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])
    
    # should all raise error
    with pytest.raises(ValueError):
        _plot_args_replacer(('x', 'y', 'z', 'a'), [1,2,3])
    with pytest.raises(ValueError):
        _plot_args_replacer(('ones', 'twos', 'threes', 'fours'), [1,2,3])
        
    with pytest.raises(ValueError):
        _plot_args_replacer(('x', 'y', 'z', 'a'), pts)
    with pytest.raises(ValueError):
        _plot_args_replacer(('ones', 'twos', 'threes', 'fours'), pts)
