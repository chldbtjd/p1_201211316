class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is ", self.name
    def talk(self):
        print self.name,"mung mung"

class ShihTzuDog(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print self.name,"Si Si " 
class Maltess(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print self.name,"mal mal"
def lab14():
    myShihTZuDog = ShihTzuDog("ShihTZu")
    myShihTZuDog.talk()
    mymaltess = Maltess("Maltess")
    mymaltess.talk()
    mydog =Dog("poppy")
    mydog.talk()
def main():
    lab14()
if __name__=="__main__": 
     main()  