import os
import time
def UpperOut():

    editor='CYS'
    timeEdited=time.strftime('%Y-%m-%d %H:%M:%S')
    fin =open("output.txt",'r')
    fout=open("outputUpper.txt",'w')
    for line in fin:
        if(line.find("line")>=0):
            line=line.replace("line","line".upper())
            fout.write("[{0} edited {1}]".format(editor,timeEdited)+" "+line)
            print "[{0} edited {1}]".format(editor,timeEdited),line
        else:
            fout.write(line)
            print line
    fin.close()
    fout.close()

def DataOut():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        toPrint="{0}\t".format(i)
        if(i%2==0):
            print toPrint
            fout.write(toPrint+"\n")
        else:
            print toPrint,
            fout.write(toPrint)

    fout.close()
def lab13():
    UpperOut()    
    DataOut()
def main():
    lab13()
if __name__=="__main__": 
     main()