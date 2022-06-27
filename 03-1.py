class LeftParagraph:
    def __init__(self, num=int()):
        self.num = num
        self.x = []

    def add_word(self, stroka=str()):
        if len(self.x) == 0 or len(stroka + self.x[-1]) >= self.num:
            self.x.append(stroka)
        else:
            self.x[-1] = self.x[-1] + ' ' + stroka

    def end(self):
        for elem in self.x:
            print(elem)


class RightParagraph:
    def __init__(self, num=int()):
        self.num = num
        self.x = []

    def add_word(self, stroka=str()):
        if len(self.x) == 0 or len(stroka + (self.x[-1]).lstrip()) >= self.num:
            self.x.append(stroka.rjust(self.num, " "))
        else:
            self.x[-1] = (self.x[-1].lstrip() + ' ' + str(stroka)).rjust(' ', self.num)

    def end(self):
        for elem in self.x:
            print(elem)


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()
