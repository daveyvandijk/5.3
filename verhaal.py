from re import A
import time 
import random 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
list1 = ['ja', 'nee']
list2 = ['ja', 'JA', 'Ja', 'jA']


#start
def intro():
    print ("je bent een vluchteling en je komt uit een land waar oorlog word gevoert. je wild vluchten naar nederland maar met wie ga je naar nederland reizen?")
    time.sleep(3)
    print ("A.  je gaat Familie ")
    time.sleep(1)
    print ("B.  je gaat aleen ")
    time.sleep(1)
    choice = input ("make your choice...")
    if choice in answer_A:
        option_vervoer1()
    elif choice in answer_B:
        option_vervoer2()
    else:
        print ("invalid choice!")
        intro()
    time.sleep(2)

#01
def option_vervoer1():
    print ("je gaat met je familie uit een anderland naar nederland komen maar hoe ga jij er heen komen?")
    time.sleep(3)
    print ("A.  je gaat met een boot ")
    time.sleep(1)
    print ("B.  je gaat met een auto ")
    time.sleep(1)
    print ("C.  je gaat met een vliegtuig ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_boot1()
    elif choice in answer_B:
        option_auto1()
    elif choice in answer_C:
        print ("uit een oorlogs gebied weg vliegen is niet zo handig. ")
    else:
        print ("invalid choice!")
        option_vervoer1()
    time.sleep(2)

#03
def option_boot1():
    print ("je gaat met de boot naar nederland maar er zitten veel mensen op het kleinen bootje wat doe je? ")
    time.sleep(3)
    print ("A.  je propt je zelf er bij")
    time.sleep(1)
    print ("B.  je laat je famielie voor gaan en jij neemt de volgende boot ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_ac1()
    elif choice in answer_B:
        option_ac1()
    else:
        print ("invalid choice!")
        option_boot1()
    time.sleep(2)

#04  
def option_auto1():
    print ("je gaat met je familie met de auto naar nederland maar de auto is vol met koffers?  ")
    time.sleep(3)
    print ("A.  je laat een paar koffers achter ")
    time.sleep(1)
    print ("B.  je gaat met iemand anders mee ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in 'A':
        option_ac1()
    elif choice in'B':
        option_ac1()
    else:
        print ("invalid choice!")
        option_auto1()
    time.sleep(2)

#02  
def option_vervoer2():
    print ("je bent alleen en je wilt uit een anderland in nederland komen wonen hoe ga jij er heen komen?")
    time.sleep(3)
    print ("A.  je gaat met een boot ")
    time.sleep(1)
    print ("B.  je gaat met een auto ")
    time.sleep(1)
    print ("C.  je gaat met een vliegtuig ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_boot2()
    elif choice in answer_B:
        option_auto2()
    elif choice in answer_C:
        print ("uit een oorlogs veld weg vliegen is denk zo handig. ")
    else:
        print ("invalid choice!")
        option_vervoer2()
    time.sleep(2)

#05  
def option_boot2():
    print ("je gaat met de boot naar nederland maar er zitten veel mensen op een kleinen bootje wat doe je? ")
    time.sleep(3)
    print ("A.  je propt je zelf op de boot ")
    time.sleep(1)
    print ("B.  wachten op de volgende boot")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_ac2()
    elif choice in answer_B:
        option_ac2()
    else:
        print ("invalid choice!")
        option_boot2()
    time.sleep(2)

#06  !
def option_auto2():
    print ("je bent alleen gegaan met de auto naar nederland maar ga je liften of ga je zelf met de auto?")
    time.sleep(3)
    print ("A.  liften")
    time.sleep(1)
    print ("B.  zelf rijden")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_ac2()
    elif choice in answer_B:
        option_ac2()
    else:
        print ("invalid choice!")
        option_auto1()
    time.sleep(2)

#09
def option_ac1():
    print ("je komt in nederland met je familie je moet je dan inschrijven bij het aanmeld centerum in Ter Apel?")
    time.sleep(3)
    print ("A.  je schrijft je in bij het AC")
    time.sleep(1)
    print ("B.  je schrijft je niet in bij het AC")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_school1()
    elif choice in answer_B:
        option_slaap()
    else:
        print ("invalid choice!")
        option_ac1()
    time.sleep(2)

#10
def option_ac2():
    print ("je komt aleen in nederland je moet je dan inschrijven bij de aanmeld centerum in Ter Apel?")
    time.sleep(3)
    print ("A.  je schrijft je in bij het AC")
    time.sleep(1)
    print ("B.  je schrijft je niet in bij het AC")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_school2()
    elif choice in answer_B:
        option_slaap()
    else:
        print ("invalid choice!")
        option_ac2()
    time.sleep(2)

#11
def option_school1():
    print ("je hebt je zelf ingeschreven bij het AC, je hebt een huis en je kan nu ook naar school?")
    time.sleep(3)
    print ("A.  ga naar school")
    time.sleep(1)
    print ("B.  ga niet naar school ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_school_werk1()
    elif choice in answer_B:
        option_geenwerk()
    else:
        print ("invalid choice!")
        option_school1()
    time.sleep(2)

#12
def option_slaap():
    print ("je hebt je niet ingeschreven bij het AC dus moet je een slaap plek zoeken?")
    time.sleep(3)
    print ("A.  je slaapt kan een paar nachten overnachten in een instantie")
    time.sleep(1)
    print ("B.  je slaapt buiten ergens onder een brug.")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_stelen()
    elif choice in answer_B:
        option_stelen1()
    else:
        print ("invalid choice!")
        option_slaap()
    time.sleep(2)

#13
def option_school2():
    print ("je hebt je zelf ingeschreven bij het AC, je hebt een huis en je kan nu ook naar school?")
    time.sleep(3)
    print ("A.  je gaat wel naar school")
    time.sleep(1)
    print ("B.  je gaat niet naar school")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_werk1()
    elif choice in answer_B:
        option_werk2()
    else:
        print ("invalid choice!")
        option_school2()
    time.sleep(2)

#14  
def option_school_werk1():
    print ("je gaat wel naar school maar ga je ook werken? ")
    time.sleep(3)
    print ("A.  geen werk ")
    time.sleep(1)
    print ("B.  wel gaan werken ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print("het einde famillie   je hebt wel school gedaan maar je ouders hebben een winkeltje en je moet toch geld gaan verdienen dus ga je gaat werken.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        option_hogeschool()
    else:
        print ("invalid choice!")
        option_school_werk1()
    time.sleep(2)

#15  
def option_geenwerk():
    print ("je gaat niet naar school maar ga je wel werken? ")
    time.sleep(3)
    print ("A.  ja")
    time.sleep(1)
    print ("B.  nee")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print("het einde famillie   je hebt geen school gedaan maar je ouders hebben een winkeltje en je gaat daar werken. ")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        print("het niks doen einde   je bent lui en doet geen school en geen werk dus je er komt geen geld binnen.")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_geenwerk()
    time.sleep(2) 

#21
def option_hogeschool():
    print ("je bent geslaagt voor je school en je bent druk bezig met werk ga je nog veder met school?")
    time.sleep(3)
    print ("A.  ga veder met een hoge school ")
    time.sleep(1)
    print ("B.  een leuke baan zoeken ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print ("het happy einde   je hebt een normaal verdient goed en levent met een gezelige famillie.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        print("het normalen einde   je een normalen baan en verdient goed je leeft in een normaal huis.")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_hogeschool()
    time.sleep(2)

#16
def option_stelen():
    print ("je hebt in een instantie geslapen en je ziet dat iemand zijn portemennee laat vallen steel je het of niet?")
    time.sleep(3)
    print ("A.  je steelt het niet en geeft het terug")
    time.sleep(1)
    print ("B.  je steelt het ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_laatstekans()
    elif choice in answer_B:
        print("het slechten einde   je hebt geld gestolen en je hebt je ook niet aangemeld bij het ac dus moet je en een boete betalen en terug naar je eigen land.")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_stelen()
    time.sleep(2)

#17
def option_stelen1():
    print ("je hebt buiten geslapen en je ziet dat iemand zijn portemennee laat vallen steel je het of niet?")
    time.sleep(3)
    print ("A.  je steelt het niet en geeft het terug")
    time.sleep(1)
    print ("B.  je steelt het")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_laatstekans()
    elif choice in answer_B:
        print("het slechten einde   je hebt geld gestolen en je hebt je ook niet aangemeld bij het ac dus moet je en een boete betalen en terug naar je eigen land. ")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_stelen1()
    time.sleep(2)

#20  
def option_laatstekans():
    print ("je hebt geen dingen gestolen, maar je wild je toch inschrijven of ga je terug naar je eigenland? ")
    time.sleep(3)
    print ("A.  probeeren aanmelden bij het AC")
    time.sleep(1)
    print ("B.  terug gaan eigen land")
    time.sleep(1)
    choice = input ("Make your choice...")
    if choice in answer_A:
        list = random.choice(list1)
        print (list)
        if list1 == 'ja':
            option_ac1()
        else:
            print ("het verdrietige einde   je bent afgewezen en moet je nu terug naar je eigen land of bij een ander land proberen aantemelden. ")
            time.sleep(5)
            option_opniew()
    elif choice in answer_B:
        print("het verdrietige einde   je gaat terug naar je eigenland en daar weer wonen of je gaat je proberen aanmelden in een ander land. ")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_laatstekans()
    time.sleep(2)

#18  
def option_werk1():
    print ("je hebt geen school gedaan maar ga je wel werken? ")
    time.sleep(3)
    print ("A.ja")
    time.sleep(1)
    print ("B.nee")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print ("het normalen einde   je een normalen baan en verdient goed je leeft in een normaal huis maar wel alleen.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        print("het niks doen einde   je bent lui en doet geen school en geen werk dus je er komt geen geld binnen.")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_werk1()
    time.sleep(2)

#19
def option_werk2():
    print ("je bent begonnen met je school ga je daar bij ook werken?")
    time.sleep(3)
    print ("A.  ja")
    time.sleep(1)
    print ("B.  nee")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        option_hoge_school1()
    elif choice in answer_B:
        option_hoge_school2()
    else:
        print ("invalid choice!")
        option_werk2()
    time.sleep(2)

#25
def option_hoge_school1():
    print ("je bent geslaagt voor je school ga je nu verder met een hogere school of ga je voor een standaart baan? ")
    time.sleep(3)
    print ("A.  voor een standaart baan ")
    time.sleep(1)
    print ("B.  hogere school")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print("het normalen einde   je een normalen baan en verdient goed je leeft in een normaal huis maar wel alleen.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        option_begin_fam1()
    else:
        print ("invalid choice!")
        option_hoge_school1()
    time.sleep(2)

#26
def option_hoge_school2():
    print ("je bent geslaagt voor je school ga je nu verder met een hogere school of ga je voor een standaart baan? ")
    time.sleep(3)
    print ("A.  voor een standaart baan ")
    time.sleep(1)
    print ("B.  hogere school")
    time.sleep(1)
    choice = input ("Make your choice...")
    if choice in answer_A:
        print("het normalen einde   je een normalen baan en verdient goed je leeft in een normaal huis maar wel alleen.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        option_begin_fam1()
    else:
        print ("invalid choice!")
        option_hoge_school2()
    time.sleep(2)

#27
def option_begin_fam1():
    print ("je bent met je hoge school bezig en wil je een familie beginnen?")
    time.sleep(3)
    print ("A.  ja")
    time.sleep(1)
    print ("B.  nee")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print ("het happy einde   je hebt een normaal verdient goed en levent met een gezelige famillie.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        option_schoolafmaken()
    else:
        print ("invalid choice!")
        option_begin_fam1()
    time.sleep(2)

#28
def option_schoolafmaken():
    print ("de school die je doet is moeilijk en haalt niet de besten cijfers maak je de school af?")
    time.sleep(3)
    print ("A. school niet afmaken ")
    time.sleep(1)
    print ("B.  school wel afmaken ")
    time.sleep(1)
    choice = input ("Make your choice... ")
    if choice in answer_A:
        print("het normalen einde   je een normalen baan en verdient goed je leeft in een normaal huis maar wel alleen.")
        time.sleep(5)
        option_opniew()
    elif choice in answer_B:
        print("het rijke einde   je hebt veel gedaan je hebt hard gewerkt je hebt nu je eigen bedrijf en groot huis en verdient nu veel geld.")
        time.sleep(5)
        option_opniew()
    else:
        print ("invalid choice!")
        option_schoolafmaken()
    time.sleep(2)

#29
def option_opniew():
        print("wil je opnieuw beginnen?")
        choice = input ("Make your choice... ") 
        if choice in list2:
            print("hij bigint weer opnieuw")
            time.sleep(1)
            intro()
        else:
            print("ik hoop dat je het leuk vond!")

intro()