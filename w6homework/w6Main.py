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
def lab6_2():
    year()
def main():
    lab6()
    lab6_2()
if __name__=="__main__": 
     main() 