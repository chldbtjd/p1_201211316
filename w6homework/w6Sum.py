begin=0
end=1000
def sum():
    sum =0
    for i in range(begin,end):    
        if (i%3==0 or i%5==0) :
            sum=sum+i
    print sum
    return sum    
def lab6():
    sum()
def main():
    lab6()
if __name__=="__main__": 
     main() 
    