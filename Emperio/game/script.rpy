init -1 python:
    RestrictRanges_ = {}
    def RestrictRangeCallback():
        for v in RestrictRanges_:
            if hasattr(store, v):
                val = getattr(store, v)
                val_min, val_max = RestrictRanges_[v]
                if val_min is not None and val < val_min:
                    setattr(store, v, val_min)
                if val_max is not None and val > val_max:
                    setattr(store, v, val_max)
    config.python_callbacks.append(RestrictRangeCallback)
    def RestrictRange(varname, min, max):
        if min is None and max is None:
            if varname in RestrictRanges_:
                del RestrictRanges_[varname]
        else:
            RestrictRanges_[varname] = (min, max)

# The game starts here.
label start:
    $ RestrictRange("money", -10, 100)
    $ RestrictRange("power", -1, 100)
    $ RestrictRange("happiness", -1, 100)
    $ RestrictRange("population", 0, 100)
    $ money = 10
    $ money_max = 100
    $ power = 10
    $ power_max = 100
    $ happiness = 10
    $ happiness_max = 100
    $ population = 10
    $ population_max = 100
    $ world = 0
    $ turns_max = 15
    $ list_scenario_1 = ["scenario4","scenario5","scenario6","scenario7","scenario9","scenario12"]
    $ list_scenario_2 = ["scenario2","scenario3","scenario8","scenario10","scenario11","scenario13","scenario15","scenario16","scenario17","scenario5","scenario18","scenario19","scenario20","scenario21","scenario22"]
    $ renpy.random.shuffle(list_scenario_1)
    $ renpy.random.shuffle(list_scenario_2)
    $ list_totale = []
    $ tips = "bjhvj"
    show screen gameUI

#generation de la list effective 
$ i = 0 
$ j = 0
while i < 3 :
    $ list_totale.append(list_scenario_1[i])
    $ i += 1
while j < 12 :
    $ list_totale.append(list_scenario_2[j])
    $ j += 1
$ loop = 0
$ counter = 0

label game:
    scene path
    jump presentation


label choice_done:
    $ hubmenu = True
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
        $ population = 0
        $ power = 0
        jump dead
    if money<0 :
        "Be careful, you are in debt"
        if money <-20 :
            jump dead
    
    if money >= 100:
        $ money = 100
    if happiness >= 100:
        $ money = 100
    if power >= 100:
        $ money = 100
    if population >= 100:
        $ money = 100
    
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
            scene medievaltown8
        elif moy >=50 :
            scene medievaltown7
        elif moy >=40 :
            scene medievaltown6
        else:
            scene medievaltown5

    if list_totale and loop <15 :
        $ loop +=1
        python :
            renpy.jump(list_totale.pop(0))
    else :
        jump ending

label dead:
    "You lose"
            
label ending:
    $ power =50
    $ score = power+money+happiness+population
    hide text
    hide screen simple_stats_screen
    show screen end_stats_screen

    "Show ranking/results (to do)"

    if power <50 :
        "Tips : Look carefully at your village's power before fighting ! "
    
    if money <50 :
        "Tips : You have only 15 turns to play, maybe it is better to not invest much at the end of the game... "
    
    if happiness <50 :
        "Tips : Invest in what is useful so you don't run out of money during key moments!"
    
    if population <50 :
        "Tips : Invest in your village to attract people and expend your population !"

    "The end."

    return
