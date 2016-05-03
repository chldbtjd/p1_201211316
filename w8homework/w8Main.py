
import matplotlib
import matplotlib.pyplot as plt
    
def word():
    word = '7 hongji'

    z=dict()
    z['alpha']=0
    z['number']=0
    for i in word:
        if i.isalpha():
                z['alpha']=z['alpha']+1
        elif i.isdigit():
                z['number']=z['number']+1
    print z
    plt.bar(range(len(z)),z.values(),align='center')
    plt.xticks(range(len(z)),list(z.keys()))
    plt.show()
def dcit():
    word = 'sangmyung university'
    
    d=dict()


    for i in word:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    print d

    d.keys()
    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()
def Home():
    Myhome=set(['TV', 'phone', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
    Fhome=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])
    
    print " MyHome U FriendHome "
    print Myhome.union(Fhome)
    

    print "MyHome - FriendHome"
    print Myhome-Fhome
    
    print "FriendHome - MyHome"
    print Fhome-Myhome
 

    print "FriendHome intersection MyHome"
    print Myhome.intersection(Fhome)
    

    num=dict()
   
    for c in Myhome.union(Fhome):
        if c not in Myhome&Fhome:
            num[c]=1
        else:
            num[c]=2
            
    print "Count"
    print num
def lab8():
        dcit()
        word()
        Home()
def main():
    lab8()
if __name__=="__main__": 
     main() 
