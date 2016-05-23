import os
def searchPY():
    try:
        mydir=os.getcwd() 
        filename='Python.txt' 
        myfilename=os.path.join(mydir, filename) 
        myfile = open(myfilename,'r')
        contents=myfile.readlines()
        for i in contents:
            if i.find("Python")>=0:
                print i
        myfile.close()
    except IOError as e:
        print e
    

def lineUpper():
    try:
        myfile=open("output.txt","w")
        line1='first line\n'
        myfile.write(line1)
        line2='\tsecond line\n'
        myfile.write(line2)
        line3='third'
        myfile.write(line3)
        myfile=open("output.txt","r")
        contents = myfile.readlines()
        re = list()
        word="line"
        for i in contents:
            if i.find("line")>=0:
                re.append(i.replace(word,word.upper()))
            else:
                re.append(i)
        myfile=open("output.txt","w")
        for i in range (0,len(re)):
            myfile.write(re[i])
        myfile.close()
    except IOError as e:
        print e
def lab12():
    searchPY()
    lineUpper()
def main():
    lab12()
if __name__=="__main__": 
     main()