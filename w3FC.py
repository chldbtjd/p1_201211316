def F():
    b=raw_input("F:")
    f=float(b)
    c=(f-32.0)/1.8  
    print c
def C():
    b=raw_input("C:")
    c=float(b)
    f=(c*1.8)+32.0
    print f
    

a= raw_input("F/C?")
if(a=="F"):
   F()
elif(a=="C"):
   C()
else :
    print "Error"


