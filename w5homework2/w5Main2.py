def computeBMI(height,weight):
    

    bmi=weight/(height*height)
   
    if bmi>=18.5 and bmi<25:
        print "normal weight"
    elif bmi>=25.0 and bmi<30:
        print "overweight"
    else:
        print "error"

def lab5():
    a=raw_input("height:")
    b=raw_input("weight:")
    h=float(a)
    w=float(b)
    computeBMI(h,w)
def main():
    lab5()
 
if __name__=="__main__": 
     main() 