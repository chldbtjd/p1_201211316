import os
import time
import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
def FileAdd():
    try:
        fin1 = open('python.txt','a')
        fin2 = open('outputNumber.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
        myfin = open('python.txt','r')
        for line in myfin:
            print line
    except IOError as e:
        print e
def drawSquareWithCoords(aFile):
    xs=aFile[0]
    xe=aFile[1]
    ys=aFile[2]
    ye=aFile[3]
    t1.penup()
    t1.setpos(xs)
    t1.pendown()
    t1.goto(aFile[0][0],aFile[1][1])
    t1.goto(xe)
    t1.goto(aFile[1][0],aFile[0][1])
    t1.goto(xs)
    t1.write("first Square")
    t1.penup()
    t1.setpos(ys)
    t1.pendown()
    t1.goto(aFile[2][0],aFile[3][1])
    t1.goto(ye)
    t1.goto(aFile[3][0],aFile[2][1])
    t1.goto(ys)
    t1.write("second Square")

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
def lab13_2():
    myfin=open('rect.txt','w')
    myfin.write("0,0,100,100\n")
    myfin.write("150,150,200,200")
    myfin= open('rect.txt','r')
    li = list()
    for line in myfin:
        line1=line.split(',')
        li.append((int(line1[0]),int(line1[1])))
        li.append((int(line1[2]),int(line1[3].strip())))
    myfin.close()
    UpperOut()    
    DataOut()
    drawSquareWithCoords(li)
    FileAdd()
def main():
    lab13_2()
if __name__=="__main__": 
     main()