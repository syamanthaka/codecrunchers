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

    def indexmethod(self, coin_list, max_val):
        T = [0] * (max_val + 1)
        T[0] = 1

        for i in range(len(coin_list)):
            j = coin_list[i]
            while j <= max_val:
                T[j] += T[j - coin_list[i]]
                j = j + 1
        return T[max_val]
