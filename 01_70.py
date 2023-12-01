from collections import OrderedDict
def beg_ins(d, k, v):
    d.update({k: v})
    d.move_to_end(k, last= False)
    return d
d= OrderedDict([('a', 1),
                ('b', 2),
                ('c', 3)])
print(beg_ins(d, 'd', 4))