default money = 0
default power = 0
default happiness = 0
default population = 0
#default hubmenu = True


# The game starts here.
label start:
    $ money = 10
    $ money_max = 100
    $ power = 10
    $ power_max = 100
    $ happiness = 10
    $ happiness_max = 100
    $ population = 10
    $ population_max = 100
    $ world = 0
    $ list_scenario = ["scenario1" ,"scenario2","scenario3","scenario4","scenario5","scenario6","scenario7","scenariop1","scenariop2","scenarion1","scenarion2"]
    $ renpy.random.shuffle(list_scenario)
    $ loop = 0

label game:
    scene path
    jump presentation

label choice_done:
    $ hubmenu = True
    if list_scenario and loop <10 :
        $ loop +=1
        show screen simple_stats_screen

        #verification of ressources
        $ lose=0
        if money ==0:
            $ lose +=1
        if happiness ==0:
            $ lose +=1
        if power ==0:
            $ lose +=1
        if lose >=2:
            jump dead
        if happiness <0 or power <0 or population<=0 :
            jump dead
        if money<0 :
            "Be careful, you are in debt"
        
        #Background choice
        $ moy = (money+power+happiness+population)/4
        if (world == 0 ):
            if money <=2:
                scene ruins1
            elif population <= 10 :
                if happiness <=10 :
                    scene ville1
                elif happiness >= 10:
                    scene ville2
            elif moy >=80 :
                scene ville8
            elif moy >=70 :
                scene ville7
            elif moy >=60 :
                scene ville6
            elif moy >=50 :
                scene ville5
            elif moy >=40 :
                scene ville4
            else:
                scene ville3

        elif (world == 1) :
            if money <=2:
                scene medievaltown1
            elif population <= 10 :
                if happiness <=10 :
                    scene medievaltown3
                elif happiness >= 10:
                    scene medievaltown4
            elif moy >=80 :
                scene medievaltown10
            elif moy >=70 :
                scene medievaltown9
            elif moy >=60 :
                scene Mmedievaltown8
            elif moy >=50 :
                scene medievaltown7
            elif moy >=40 :
                scene medievaltown6
            else:
                scene medievaltown5

        python :
            renpy.jump(list_scenario.pop(0))
    else :
        jump ending

label dead:
    "You lose"
            
label ending:
    "The end."

    return
