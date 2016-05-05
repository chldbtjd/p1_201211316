
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
    
def lab10():
    mins()
    ing()
def main():
    lab10()
if __name__=="__main__": 
     main() 
