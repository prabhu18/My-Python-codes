import random

class RandomizedCollection(object):

    def __init__(self):
        self.list={}
        self.count=0

    def insert(self, val):

        try:
            self.list[val]=self.list[val]+1
            self.count=self.count+1
            return False

        except:

            self.list[val] = 1
            self.count = self.count + 1
            return True

    def remove(self, val):

        try:
            self.list[val] = self.list[val] -1
            self.count=self.count-1
            return True

        except:

            return False


    def getRandom(self):
        z=random.randrange(self.count)
        random_array=[]
        for i in self.list.iterkeys():
            if self.list[i]>0:
                flag=self.list[i]
                while(flag>0):
                    random_array.append(i)
                    flag=flag-1

        return random_array[z]




obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.insert(2)
param_3 = obj.insert(3)
param_4 = obj.insert(3)
param_5 = obj.remove(3)
param_6 = obj.remove(4)
param_7 = obj.getRandom()
print param_7