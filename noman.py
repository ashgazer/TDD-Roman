class roman:

    def __init__(self):
        self.RN = {"I": 1
            , "V": 5
            , "X": 10
                   , "C": 100

            , "IV": 4

            , 'L': 50
                   }

        self.rn2 = {v: k for k, v in self.RN.items()}

    def cal(self, num):
        return self.RN.get(num, KeyError)

    def num_2_rom(self, r):
        r_string = ""
        od = dict(sorted(self.rn2.items(), key=lambda kv: (kv[0], kv[1]), reverse=True))

        for k, v in od.items():
            while r >= k:
                r_string += v
                r -= k

        return r_string
#
#     def printdict(self):
#         print(self.rn2)
#
#         testt = dict(sorted(self.rn2.items(), key=lambda kv: (kv[0], kv[1]), reverse=True))
#         print(testt)
#
#     #
#     #
#     #
#     #
#
#
# r = roman()
# r.printdict()
