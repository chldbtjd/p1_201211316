def dcit():
    word = 'sangmyung university'
    
    d=dict()


    for i in word:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    print d

 
def lab8():
        dcit()
def main():
    lab8()
if __name__=="__main__": 
     main() 