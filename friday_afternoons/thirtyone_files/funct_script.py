from tests.test_thirtyone_prob import coin_list
from thirtyone.thirtyone_prob import Combinations as combo

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
max_val = 200

# combo.one_combo()
c_obj = combo()
print(c_obj.allcombos(coin_list, max_val))