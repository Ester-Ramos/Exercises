import pytest
from binary_search import binary_search
from recursive_binary import recursive_binary

@pytest.fixture(params=[binary_search, recursive_binary])
def itemNo(request):
    return request.param

def test_search(itemNo):
    assert itemNo([1,2,3,4,5], 4)
    assert not itemNo([1,2,3,4,5], 0)
    assert itemNo([1,2,6,9,43], 2)
    assert itemNo([1,2,6,6,9,43], 6)
    assert not itemNo([1,2,3,4,5], 6)
    assert itemNo([-2,-1,3,4,5], 5)
    assert itemNo([-56,-43,-20,-6,-2], -43)
    assert not itemNo([-56,-43,-20,-6,-2], -42)
    assert not itemNo([1,2,3,4,5], 1.5)
