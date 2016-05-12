import operator
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()



def keyup():
	t1.forward(50)
def keydown():
	t1.backward(50)
def keyright():
	t1.right(90)
def keyleft():
	t1.left(90)
def addkeys():
	wn.onkey(keyup,"Up")
	wn.onkey(keydown,"Down")
	wn.onkey(keyright,"Right")
	wn.onkey(keyleft,"Left")
	
def addMouse():
	wn.onclick(mousegoto)
	

def mousegoto(x,y):
	if(x==50 and y<=50 and y>=0):
		t1.setpos(x,y)
		t1.write("good")
		print "good"
		
	else:
		t1.setpos(x,y)
def exitq():
	wn.bye()
def addexit():
	wn.onkey(exitq,"q")

            
def lab11():	
	t2.penup()
	t2.setposition(50,50)
	t2.pendown()
	t2.setposition(50,00)
	addMouse()
	addkeys()
	addexit()
	wn.listen()
	turtle.mainloop()




def isSpeech():
    word=["AMONG the vicissitudes incident to life no event could have filled me with greater anxieties than that of which the notification was transmitted by your order, and received on the 14th day of the present month. On the one hand, I was summoned by my country, whose voice I can never hear but with veneration and love, from a retreat which I had chosen with the fondest predilection, and, in my flattering hopes, with an immutable decision, as the asylum of my declining years - a retreat which was rendered every day more necessary as well as more dear to me by the addition of habit to inclination, and of frequent interruptions in my health to the gradual waste committed on it by time. On the other hand, the magnitude and difficulty of the trust to which the voice of my country called me, being sufficient to awaken in the wisest and most experienced of her citizens a distrustful scrutiny into his qualifications, could not but overwhelm with despondence one who (inheriting inferior endowments from nature and" 
    "unpracticed in the duties of civil administration) ought to be peculiarly conscious of his own deficiencies. In this conflict of emotions all I dare aver is that it has been my faithful study to collect my duty from a just appreciation of every circumstance by which it might be affected. All I dare hope is that if, in executing this task, I have been too much swayed by a grateful remembrance of former instances, or by an affectionate sensibility to this transcendent proof of the confidence of my fellow-citizens, and have thence too little consulted my incapacity as well as disinclination for the weighty and untried cares before me, my error will be palliated by the motives which mislead me, and its consequences be judged by my country with some share of the partiality in which they originated."
    "Such being the impressions under which I have, in obedience to the public summons, repaired to the present station, it would be peculiarly improper to omit in this first official act my fervent supplications to that Almighty Being who rules over the universe, who presides in the councils of nations, and whose providential aids can supply every human defect, that His benediction may consecrate to the liberties and happiness of the people of the United States a Government instituted by themselves for these essential purposes, and may enable every instrument employed in its administration to execute with success the functions allotted to his charge. In tendering this homage to the Great Author of every public and private good, I assure myself that it expresses your sentiments not less than my own, nor those of my fellow-citizens at large less than either. No people can be bound to acknowledge and adore the Invisible Hand which conducts the affairs of men more than those of the United States." 
    "Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency; and in the important revolution just accomplished in the system of their united government the tranquil deliberations and voluntary consent of so many distinct communities from which the event has resulted can not be compared with the means by which most governments have been established without some return of pious gratitude, along with an humble anticipation of the future blessings which the past seem to presage. These reflections, arising out of the present crisis, have forced themselves too strongly on my mind to be suppressed. You will join with me, I trust, in thinking that there are none under the influence of which the proceedings of a new and free government can more auspiciously commence."
    "By the article establishing the executive department it is made the duty of the President to recommend to your consideration such measures as he shall judge necessary and expedient. The circumstances under which I now meet you will acquit me from entering into that subject further than to refer to the great constitutional charter under which you are assembled, and which, in defining your powers, designates the objects to which your attention is to be given. It will be more consistent with those circumstances, and far more congenial with the feelings which actuate me, to substitute, in place of a recommendation of particular measures, the tribute that is due to the talents, the rectitude, and the patriotism which adorn the characters selected to devise and adopt them. In these honorable qualifications I behold the surest pledges that as on one side no local prejudices or attachments, no separate views nor party animosities, will misdirect the comprehensive and equal eye which ought to watch" 
    "over this great assemblage of communities and interests, so, on another, that the foundation of our national policy will be laid in the pure and immutable principles of private morality, and the preeminence of free government be exemplified by all the attributes which can win the affections of its citizens and command the respect of the world. I dwell on this prospect with every satisfaction which an ardent love for my country can inspire, since there is no truth more thoroughly established than that there exists in the economy and course of nature an indissoluble union between virtue and happiness; between duty and advantage; between the genuine maxims of an honest and magnanimous policy and the solid rewards of public prosperity and felicity; since we ought to be no less persuaded that the propitious smiles of Heaven can never be expected on a nation that disregards the eternal rules of order and right which Heaven itself has ordained; and since the preservation of the sacred fire of liberty" 
    "and the destiny of the republican model of government are justly considered, perhaps, as deeply, as finally, staked on the experiment entrusted to the hands of the American people." 
    "Besides the ordinary objects submitted to your care, it will remain with your judgment to decide how far an exercise of the occasional power delegated by the fifth article of the Constitution is rendered expedient at the present juncture by the nature of objections which have been urged against the system, or by the degree of inquietude which has given birth to them. Instead of undertaking particular recommendations on this subject, in which I could be guided by no lights derived from official opportunities, I shall again give way to my entire confidence in your discernment and pursuit of the public good; for I assure myself that whilst you carefully avoid every alteration which might endanger the benefits of an united and effective government, or which ought to await the future lessons of experience, a reverence for the characteristic rights of freemen and a regard for the public harmony will sufficiently influence your deliberations on the question how far the former can be impregnably fortified or" 
    "the latter be safely and advantageously promoted." 
    "To the foregoing observations I have one to add, which will be most properly addressed to the House of Representatives. It concerns myself, and will therefore be as brief as possible. When I was first honored with a call into the service of my country, then on the eve of an arduous struggle for its liberties, the light in which I contemplated my duty required that I should renounce every pecuniary compensation. From this resolution I have in no instance departed; and being still under the impressions which produced it, I must decline as inapplicable to myself any share in the personal emoluments which may be indispensably included in a permanent provision for the executive department, and must accordingly pray that the pecuniary estimates for the station in which I am placed may during my continuance in it be limited to such actual expenditures as the public good may be thought to require." 
    "Having thus imparted to you my sentiments as they have been awakened by the occasion which brings us together, I shall take my present leave; but not without resorting once more to the benign Parent of the Human Race in humble supplication that, since He has been pleased to favor the American people with opportunities for deliberating in perfect tranquillity, and dispositions for deciding with unparalleled unanimity on a form of government for the security of their union and the advancement of their happiness, so His divine blessing may be equally conspicuous in the enlarged views, the temperate consultations, and the wise measures on which the success of this Government must depend." 

    ]
    word2=[
    "WHEN it was first perceived, in early times, that no middle course for America remained between unlimited submission to a foreign legislature and a total independence of its claims, men of reflection were less apprehensive of danger from the formidable power of fleets and armies they must determine to resist than from those contests and dissensions which would certainly arise concerning the forms of government to be instituted over the whole and over the parts of this extensive country. Relying, however, on the purity of their intentions, the justice of their cause, and the integrity and intelligence of the people, under an overruling Providence which had so signally protected this country from the first, the representatives of this nation, then consisting of little more than half its present number, not only broke to pieces the chains which were forging and the rod of iron that was lifted up, but frankly cut asunder the ties which had bound them, and launched into an ocean of uncertainty." 
    "The zeal and ardor of the people during the Revolutionary war, supplying the place of government, commanded a degree of order sufficient at least for the temporary preservation of society. The Confederation which was early felt to be necessary was prepared from the models of the Batavian and Helvetic confederacies, the only examples which remain with any detail and precision in history, and certainly the only ones which the people at large had ever considered. But reflecting on the striking difference in so many particulars between this country and those where a courier may go from the seat of government to the frontier in a single day, it was then certainly foreseen by some who assisted in Congress at the formation of it that it could not be durable." 
    "Negligence of its regulations, inattention to its recommendations, if not disobedience to its authority, not only in individuals but in States, soon appeared with their melancholy consequences - universal languor, jealousies and rivalries of States, decline of navigation and commerce, discouragement of necessary manufactures, universal fall in the value of lands and their produce, contempt of public and private faith, loss of consideration and credit with foreign nations, and at length in discontents, animosities, combinations, partial conventions, and insurrection, threatening some great national calamity." 
    "In this dangerous crisis the people of America were not abandoned by their usual good sense, presence of mind, resolution, or integrity. Measures were pursued to concert a plan to form a more perfect union, establish justice, insure domestic tranquillity, provide for the common defense, promote the general welfare, and secure the blessings of liberty. The public disquisitions, discussions, and deliberations issued in the present happy Constitution of Government." 
    "Employed in the service of my country abroad during the whole course of these transactions, I first saw the Constitution of the United States in a foreign country. Irritated by no literary altercation, animated by no public debate, heated by no party animosity, I read it with great satisfaction, as the result of good heads prompted by good hearts, as an experiment better adapted to the genius, character, situation, and relations of this nation and country than any which had ever been proposed or suggested. In its general principles and great outlines it was conformable to such a system of government as I had ever most esteemed, and in some States, my own native State in particular, had contributed to establish. Claiming a right of suffrage, in common with my fellow-citizens, in the adoption or rejection of a constitution which was to rule me and my posterity, as well as them and theirs, I did not hesitate to express my approbation of it on all occasions, in public and in private. It was not then, nor has be"
    "en since, any objection to it in my mind that the Executive and Senate were not more permanent. Nor have I ever entertained a thought of promoting any alteration in it but such as the people themselves, in the course of their experience, should see and feel to be necessary or expedient, and by their representatives in Congress and the State legislatures, according to the Constitution itself, adopt and ordain." 
    "Returning to the bosom of my country after a painful separation from it for ten years, I had the honor to be elected to a station under the new order of things, and I have repeatedly laid myself under the most serious obligations to support the Constitution. The operation of it has equaled the most sanguine expectations of its friends, and from an habitual attention to it, satisfaction in its administration, and delight in its effects upon the peace, order, prosperity, and happiness of the nation I have acquired an habitual attachment to it and veneration for it." 
    "What other form of government, indeed, can so well deserve our esteem and love?" 
    "There may be little solidity in an ancient idea that congregations of men into cities and nations are the most pleasing objects in the sight of superior intelligences, but this is very certain, that to a benevolent human mind there can be no spectacle presented by any nation more pleasing, more noble, majestic, or august, than an assembly like that which has so often been seen in this and the other Chamber of Congress, of a Government in which the Executive authority, as well as that of all the branches of the Legislature, are exercised by citizens selected at regular periods by their neighbors to make and execute laws for the general good. Can anything essential, anything more than mere ornament and decoration, be added to this by robes and diamonds? Can authority be more amiable and respectable when it descends from accidents or institutions established in remote antiquity than when it springs fresh from the hearts and judgments of an honest and enlightened people? For it is the people only" 
    "that are represented. It is their power and majesty that is reflected, and only for their good, in every legitimate government, under whatever form it may appear. The existence of such a government as ours for any length of time is a full proof of a general dissemination of knowledge and virtue throughout the whole body of the people. And what object or consideration more pleasing than this can be presented to the human mind? If national pride is ever justifiable or excusable it is when it springs, not from power or riches, grandeur or glory, but from conviction of national innocence, information, and benevolence." 
    "In the midst of these pleasing ideas we should be unfaithful to ourselves if we should ever lose sight of the danger to our liberties if anything partial or extraneous should infect the purity of our free, fair, virtuous, and independent elections. If an election is to be determined by a majority of a single vote, and that can be procured by a party through artifice or corruption, the Government may be the choice of a party for its own ends, not of the nation for the national good. If that solitary suffrage can be obtained by foreign nations by flattery or menaces, by fraud or violence, by terror, intrigue, or venality, the Government may not be the choice of the American people, but of foreign nations. It may be foreign nations who govern us, and not we, the people, who govern ourselves; and candid men will acknowledge that in such cases choice would have little advantage to boast of over lot or chance." 
    "Such is the amiable and interesting system of government (and such are some of the abuses to which it may be exposed) which the people of America have exhibited to the admiration and anxiety of the wise and virtuous of all nations for eight years under the administration of a citizen who, by a long course of great actions, regulated by prudence, justice, temperance, and fortitude, conducting a people inspired with the same virtues and animated with the same ardent patriotism and love of liberty to independence and peace, to increasing wealth and unexampled prosperity, has merited the gratitude of his fellow-citizens, commanded the highest praises of foreign nations, and secured immortal glory with posterity." 
    "In that retirement which is his voluntary choice may he long live to enjoy the delicious recollection of his services, the gratitude of mankind, the happy fruits of them to himself and the world, which are daily increasing, and that splendid prospect of the future fortunes of this country which is opening from year to year. His name may be still a rampart, and the knowledge that he lives a bulwark, against all open or secret enemies of his country's peace. This example has been recommended to the imitation of his successors by both Houses of Congress and by the voice of the legislatures and the people throughout the nation." 
    "On this subject it might become me better to be silent or to speak with diffidence; but as something may be expected, the occasion, I hope, will be admitted as an apology if I venture to say that if a preference, upon principle, of a free republican government, formed upon long and serious reflection, after a diligent and impartial inquiry after truth; if an attachment to the Constitution of the United States, and a conscientious determination to support it until it shall be altered by the judgments and wishes of the people, expressed in the mode prescribed in it; if a respectful attention to the constitutions of the individual States and a constant caution and delicacy toward the State governments; if an equal and impartial regard to the rights, interest, honor, and happiness of all the States in the Union, without preference or regard to a northern or southern, an eastern or western, position, their various political opinions on unessential points or their personal attachments; if a love of "
    "virtuous men of all parties and denominations; if a love of science and letters and a wish to patronize every rational effort to encourage schools, colleges, universities, academies, and every institution for propagating knowledge, virtue, and religion among all classes of the people, not only for their benign influence on the happiness of life in all its stages and classes, and of society in all its forms, but as the only means of preserving our Constitution from its natural enemies, the spirit of sophistry, the spirit of party, the spirit of intrigue, the profligacy of corruption, and the pestilence of foreign influence, which is the angel of destruction to elective governments; if a love of equal laws, of justice, and humanity in the interior administration; if an inclination to improve agriculture, commerce, and manufacturers for necessity, convenience, and defense; if a spirit of equity and humanity toward the aboriginal nations of America, and a disposition to meliorate their condition by inclining" 
    "the m to" 
    "be more friendly to us, and our citizens to be more friendly to them; if an inflexible determination to maintain peace and inviolable faith with all nations, and that system of neutrality and impartiality among the belligerent powers of Europe which has been adopted by this Government and so solemnly sanctioned by both Houses of Congress and applauded by the legislatures of the States and the public opinion, until it shall be otherwise ordained by Congress; if a personal esteem for the French nation, formed in a residence of seven years chiefly among them, and a sincere desire to preserve the friendship which has been so much for the honor and interest of both nations; if, while the conscious honor and integrity of the people of America and the internal sentiment of their own power and energies must be preserved, an earnest endeavor to investigate every just cause and remove every colorable pretense of complaint; if an intention to pursue by amicable negotiation a reparation for the injuries that have been" 
    "committed on the commerce of our fellow-citizens by whatever nation, and if success can not be obtained, to lay the facts before the Legislature, that they may consider what further measures the honor and interest of the Government and its constituents demand; if a resolution to do justice as far as may depend upon me, at all times and to all nations, and maintain peace, friendship, and benevolence with all the world; if an unshaken confidence in the honor, spirit, and resources of the American people, on which I have so often hazarded my all and never been deceived; if elevated ideas of the high destinies of this country and of my own duties toward it, founded on a knowledge of the moral principles and intellectual improvements of the people deeply engraven on my mind in early life, and not obscured but exalted by experience and age; and, with humble reverence, I feel it to be my duty to add, if a veneration for the religion of a people who profess and call themselves Christians, and a" 
    "fixed resolution to consider a" 
    "decent respect for Christianity among the best recommendations for the public service, can enable me in any degree to comply with your wishes, it shall be my strenuous endeavor that this sagacious injunction of the two Houses shall not be without effect." 
    "With this great example before me, with the sense and spirit, the faith and honor, the duty and interest, of the same American people pledged to support the Constitution of the United States, I entertain no doubt of its continuance in all its energy, and my mind is prepared without hesitation to lay myself under the most solemn obligations to support it to the utmost of my power." 
    "And may that Being who is supreme over all, the Patron of Order, the Fountain of Justice, and the Protector in all ages of the world of virtuous liberty, continue His blessing upon this nation and its Government and give it all possible success and duration consistent with the ends of His providence." 

    ]
    d=dict()
    for i in word[0].split():
            if i not in d:
                    d[i]=1
            else:
                    d[i]=d[i]+1
    d2=dict()

    for i in word2[0].split():
            if i not in d2:
                    d2[i]=1
            else:
                    d2[i]=d2[i]+1

    sorted_d=sorted(d.items(), key=operator.itemgetter(1))
    sorted_d2=sorted(d2.items(), key=operator.itemgetter(1))
    print "speech---"
    print ""
    for i in range (len(d)-1,len(d)-11,-1):
        print sorted_d[i]
    print ""
    print "speech2---"
    print ""
    for i in range (len(d2)-1,len(d2)-11,-1):
        print sorted_d2[i]
def seoul():
    x=list()
    x2=list()
    x=[["very good","good","bad","so bad"], 
    [13.1,37.1,1.5,3.52],  
    [10.6,34.6,  1.9, 3.39],  
    [27.1 ,40.0 ,1.5, 3.88],  
    [16.2 , 37.8 ,  0.8 , 3.62],  
    [11.4,  29.8   ,4.9 , 3.28],  
    [12.2,  26.5  , 4.4 , 3.27],  
    [13.5,  29.7,  2.4,  3.41],  
    [13.7,  37.6 ,  1.2  ,3.59]]

    x2=x[1:]
    vg=0
    g=0
    b=0
    sb=0
    for i in range(len(x2)-1):
        vg+=x2[i][0]
        g+=x2[i][1]
        b+=x2[i][2]
        sb=x2[i][3]
    goodavg=(vg+g)/len(x2)
    badavg=(b+sb)/len(x2)
    
    
    print "--good avg--"
    print goodavg
    print "--bad avg--"
    print badavg
    return goodavg,badavg
def lab11_1():
	seoul()
	isSpeech()
def main():
    lab11()
    lab11_1()
if __name__=="__main__": 
     main() 