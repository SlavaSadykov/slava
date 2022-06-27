class MinStat:
    def __init__(self):
        self.stat = []
        self.lst = []

    def add_number(self, number):
        self.stat.append(number)

    def result(self):
        if self.stat == self.lst:
            return None
        else:
            return min(self.stat)


class MaxStat:
    def __init__(self):
        self.stat = []
        self.lst = []

    def add_number(self, number):
        self.stat.append(number)

    def result(self):
        if self.stat == self.lst:
            return None
        else:
            return max(self.stat)


class AverageStat:
    def __init__(self):
        self.stat = []
        self.lst = []

    def add_number(self, number):
        self.stat.append(number)

    def result(self):
        if self.stat == self.lst:
            return None
        else:
            dlina = len(self.stat)
            summa = sum(self.stat)
            return summa / dlina

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
