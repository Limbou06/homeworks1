def function(self, b):
    a=[]
    if len(self)==len(b):
        for i in range(len(self)):
            a.append(self[i]*b[i])
        a.sort()
    else:
        for i in (self+b):
            if (self + b).count(i)>1:
                a.append(i)
        a.sort()
    return a



assert(function([1, 2, 3, 3, 3], [-1, 2, 3])) == [2, 2, 3, 3, 3, 3]
assert(function([1, 2, 3],[-1, 2, 0])) == [-1,0,4]
assert(function([0,0,1, 0, 11, 8, 9], [-1,-2,-3,-4,-5,-7])) ==[0,0,0]
