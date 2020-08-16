class Gen:
    def __init__(self):
        pass

    def toBeDone(self):
        pass

    def do_it(self):
        self.toBeDone()


class Spec1(Gen):
    def spec_one_way(self):
        print('Way 1')

    def toBeDone(self):
        self.spec_one_way()


class Spec2(Gen):
    def spec_two_way(self):
        print('Way 2')

    def toBeDone(self):
        self.spec_two_way()


s1 = Spec1()
s2 = Spec2()

s1.do_it()
s2.do_it()