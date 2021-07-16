import pytest
import time
from thirtyone.thirtyone_prob import Combinations as combo

@pytest.fixture
def coin_list_simple():
    return [1,2,5]

@pytest.fixture
def max_val_simple():
    return 10

@pytest.fixture
def coin_list():
    return [1, 2, 5, 10, 20, 50, 100, 200]

@pytest.fixture
def max_val():
    return 200

class TestCombinations:
    def test_onecombo(self, coin_list_simple, max_val_simple):
        assert combo.one_combo(coin_list_simple, max_val_simple) == 3

    def test_allcombos(self, coin_list_simple, max_val_simple):
        c_obj = combo()
        assert c_obj.allcombos(coin_list_simple, max_val_simple) == 10

    # def test_allcombos(self, coin_list, max_val):
    #     c_obj = combo()
    #     t1 = time.time()
    #     result = c_obj.allcombos(coin_list, max_val)
    #     t2 = time.time()

    #     assert result == 73682
    #     assert t2-t1 <= 20

    def test_indexmethod(self, coin_list, max_val):
        c_obj = combo()
        t1 = time.time()
        result = c_obj.indexmethod(coin_list, max_val)
        t2 = time.time()

        assert result == 73682
        assert t2-t1 <= 1