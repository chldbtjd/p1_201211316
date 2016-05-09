import matplotlib
import matplotlib.pyplot as plt
import math   

def mins():
    Locations=list()
    x=37.575803
    y=126.973282
    z=0
    Locations=[("anguk",37.576563, 126.985446),("ganhamon",37.571595, 126.976429),("dokrib",37.574483, 126.957901),("dongdae",37.570920, 127.009192)]
    dis=list()
    for i in Locations:
        dis.append(math.sqrt((x-i[1])**2+(y-i[2])**2))
    
    
    for i in range (len(dis)):
        if(min(dis)==dis[i]):
            z=i
    print "ziyuk::",Locations[z][0] 
    print "min::",min(dis)
    return min(dis)

    

def ing():
    ingoo = list()
    ingoo=[["jongro",74425 ,76326],["jungu",61164, 61636], ["yongsan",109688, 115744], ["sungdong",144796, 146776], ["gangzin",174996, 181676], ["dongdaemon",177841,177434], 
           ["jongrang",204630, 205980], 
           ["sungbok",223373, 232245], ["ganbuk",161055, 166130], ["dobong",171576, 176735], ["noone",279169, 293772], ["eunphung",239450, 251066], ["seodaemon",148690, 156510], 
           ["mapo",182977, 196992], ["yangchon",237792, 242641]
    , ["gangseo",283869, 296762], ["guro",209344, 210282], ["gunchan",118965, 114441], ["yongdunfo",186503, 186856], ["dongjak",195734, 203014], ["gankak",254381, 249472], 
           ["seocho",212401, 229111], ["gananam",271654, 295354]
    , ["songpa",319197, 335045], ["gangdong",229829, 231671]]
    ma=0
    fa=0
    gu = dict()
    
    for i in ingoo:
        gu.update({i[0]:i[1]+i[2]})
        ma+=i[1]
        fa+=i[2]
    mavg=ma/len(ingoo)
    favg=fa/len(ingoo)
        
    print "male:",ma
    print "female:",fa
    print "gu:",gu
    print "male avg:",mavg
    print "female avg:",favg
    plt.bar(range(len(gu)),gu.values(),align='center')
    plt.xticks(range(len(gu)),list(gu.keys()))
    plt.show()
    return ma,fa,gu,mavg,favg 
    

def milk():
    da=[
        ["Coffee","Water","Milk","Icecream"],
        ["Espresso","No","No","No"],
        ["Long Black","Yes","No","No"],
        ["Flat White","No","Yes","No"],
        ["Cappuccino","No","Yes","No"],
        ["Affogato","No","No","Yes"]
    ]
    
    Da=da[1:]

    milk=0
    for i in range(len(Da)-1):
        if (Da[i][2]=="Yes"):
            milk+=1
            print "Milk in",Da[i][0]
            
    
    print float(milk)/len(Da)*100, "%"
    
def score():
    dd=[
        ["computer", "math"],
        [100, 70], [80, 60], [90, 50]
    ]
    score=dd[1:]
    
  
    cs=0
    ms=0
    for i in range(0, len(score)):
        cs=cs+score[i][0]
        ms=ms+score[i][1]
    cavg=float(cs)/len(score)
    mavg=float(ms)/len(score)
    
    print "com :", cs
    print "com avg", cavg
    print "math", ms
    print "math avg", mavg
def lyr():
    lyrics=["When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom" 
            "let it be And in my hour of darkness She is standing right in front of me Speaking words of wisdom," 
            "let it be Let it be, let it be, let it be, let it be Whisper words of wisdom, let it beAnd when the broken hearted people" 
            "Living in the world agree There will be an answer, let it be For though they may be parted there is still a chance that" 
            "they will see There will be an answer, let it be Let it be, let it be, let it be ,let it be There will be an answer" 
            "let it be Let it be, let it be, let it be, let it be Whisper words of wisdom, let it be Let it be, let it be, let it be," 
            "let it be Whisper words of wisdom, let it beAnd when the night is cloudy There is still a light that shines on me Shine until" 
            "tomorrow, let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom, let it be Let it be, let it be,"
            "let it be, let it be Whisper words of wisdom let it"]

    d=dict()
    for i in lyrics[0].split():
        if i not in d:
                d[i]=1
        else:
                d[i]=d[i]+1
    print d
    for i in d:
            if(d[i]>=20):
                print "word", i,"num", d[i]
def lab10():
    mins()
    ing()
    milk()
    score()
    lyr()
def main():
    lab10()
if __name__=="__main__": 
     main() 