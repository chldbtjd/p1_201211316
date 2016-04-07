begin=0
end=1000
def sum(begin,end):
    sum =0
    for i in range(begin,end):    
        if (i%3==0 or i%5==0) :
            sum=sum+i
    print sum
    return sum    
def lab6():
    sum(begin,end)



def year():
    a=raw_input("year:")
    y=int(a)
    if(y%4==0) and (y%100 !=0 or y%400==0):
        print "yoonneyon"
    else:
        print "false"

def UpDownGame():
    while True:
        a = raw_input("number:")
        z = int(a)
        num = 100
        if(num<z):
            print "down"
        elif(num>z):
            print "up"
        else:
            print "correct"
            break;
def lab6_3():
    UpDownGame()

   
def lab6_2():
    year()
def main():
    lab6()
    lab6_2()
    lab6_3()
if __name__=="__main__": 
     main() 