  
import pytest
from my_source1 import add_func


def test_add_one():
    assert add_func(2, 5) == 7


@pytest.mark.xfail
def test_add_fail():
    assert add_func(5, 5) == 9
    
    
def test_add_fail2():
    assert add_func(5, 11) == 9
