class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)
        return self.maximumDifference
    
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)