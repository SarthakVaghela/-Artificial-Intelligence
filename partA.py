import random

_goal_state = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]


class puzz:

    def __init__(self):
        self.h = 0
        self.d = 0
        self.p = None
        self.ad_m = []
        for i in range(3):
            self.ad_m.append(_goal_state[i][:])

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        else:
            return self.ad_m == other.ad_m

    def __str__(self):
        rr = ''
        for rw in range(3):
            rr += ' '.join(map(str, self.ad_m[rw]))
            rr += '\r\n'
        return rr

    def g_l_m(self):
        rw, clm = self.find(0)
        fr = []

        if rw > 0:
            fr.append((rw - 1, clm))
        if clm > 0:
            fr.append((rw, clm - 1))
        if rw < 2:
            fr.append((rw + 1, clm))
        if clm < 2:
            fr.append((rw, clm + 1))

        return fr

    def suff(self, s_c):
        for i in range(s_c):
            rw, clm = self.find(0)
            fr = self.g_l_m()
            tr = random.choice(fr)
            self.swap((rw, clm), tr)
            rw, clm = tr

    def find(self, value):
        if value < 0 or value > 8:
            raise Exception("ERROR")

        for rw in range(3):
            for clm in range(3):
                if self.ad_m[rw][clm] == value:
                    return rw, clm

    def peek(self, rw, clm):
        return self.ad_m[rw][clm]

    def poke(self, rw, clm, value):
        self.ad_m[rw][clm] = value

    def swap(self, pos_a, pos_b):
        temp = self.peek(*pos_a)
        self.poke(pos_a[0], pos_a[1], self.peek(*pos_b))
        self.poke(pos_b[0], pos_b[1], temp)

def index(item, seq):
    if item in seq:
        return seq.index(item)
    else:
        return -1


def main():
    p = puzz()
    p.suff(10)
    print(p)


if __name__ == "__main__":
    main()