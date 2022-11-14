import collections
def function(self):
    counter = collections.Counter()

    for value in list(self):
        counter[value] = counter[value] + 1
    return counter

assert(function([1])) == {1:1}
assert(function([0, 0, 0, 0])) == {0:4}
assert(function([1,2,3,1,3,5] )) == {2:1, 1:2, 3:2, 5:1}
assert(function([1, -1, 1.1, 1.1, 10, 100, 100, 100])) == {1:1, -1:1, 1.1:2, 10:1, 100:3}