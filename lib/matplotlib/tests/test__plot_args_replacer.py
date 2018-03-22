import pytest
from matplotlib.axes._axes import _plot_args_replacer
import numpy as np

# Sanity checking _replace_plot_args()

def test__plot_args_replacer_onearg():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])

    # should be [y] regardless of type of data    
    assert _plot_args_replacer(('y'), {'ones' : [1, 1], 'twos' : [2, 2]}) == ['y']
    assert _plot_args_replacer(('ones',), {'ones' : [1, 1], 'twos' : [2, 2]}) == ['y']
    
    assert _plot_args_replacer(('y',), pts) == ['y']
    assert _plot_args_replacer(('m',), pts) == ['y']


def test__plot_args_replacer_twoarg_dict():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])

    # [x, y] and [y, c?] with regular data
    assert _plot_args_replacer(('threes', 'fours'), {'ones' : [1, 1], 'twos' : [2, 2]}) == ['y', 'c']
    assert _plot_args_replacer(('ones', 'twos'), {'ones' : [1, 1], 'twos' : [2, 2]}) == ['x', 'y']
    
    
def test__plot_args_replacer_twoarg_stucturedict():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])
    
    # [x, y] and [y, c?] with structured data
    assert _plot_args_replacer(('threes', 'fours'), pts) == ['y', 'c']
    assert _plot_args_replacer(('ones', 'twos'), pts) == ['x', 'y']


def test__plot_args_replacer_manyarg():
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])
    
    # should all raise error
    with pytest.raises(ValueError):
        _plot_args_replacer(('fives', 'sixes', 'sevens', 'eights'), {'ones' : [1, 1], 'twos' : [2, 2]})
    with pytest.raises(ValueError):
        _plot_args_replacer(('ones', 'twos', 'threes', 'fours'), {'ones' : [1, 1], 'twos' : [2, 2]})
        
    with pytest.raises(ValueError):
        _plot_args_replacer(('fives', 'sixes', 'sevens', 'eights'), pts)
    with pytest.raises(ValueError):
        _plot_args_replacer(('ones', 'twos', 'threes', 'fours'), pts)

