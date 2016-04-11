x1=list()

def sumList(x1): 
    sum =0
    for i  in range (1,1000):
        if(i%4==0 and i%5!=0):
            x1.append(i)

    for i in range (0,len(x1)):
        sum=sum+x1[i]
    print sum
    return sum

def lab6():
    sumList(x1)
def main():
    lab6()
    
if __name__=="__main__": 
     main() 