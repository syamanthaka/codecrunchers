class Combinations:
    def one_combo(coin_list, max_val):
        n_possibilites = 0
        for each in coin_list:
            if max_val % each == 0:
                n_possibilites = n_possibilites + 1
        return n_possibilites

    def allcombos(self, coin_list, max_val):
        if len(coin_list) == 0:
            return 0
        if max_val == 0 and len(coin_list) != 0:
            return 1
        if max_val < 0 and len(coin_list) != 0:
            return 0
        return self.allcombos(coin_list[1:], max_val) + self.allcombos(coin_list, max_val-coin_list[0])