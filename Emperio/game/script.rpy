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
    $ money = 50
    $ money_max = 100
    $ power = 50
    $ power_max = 100
    $ happiness = 50
    $ happiness_max = 100
    $ population = 50
    $ population_max = 100
    $ world = 0
    $ turns_max = 15

    $ scenario_chill = ["scenario1","scenario7"]
    $ renpy.random.shuffle(scenario_chill)
    $ scenario_war =  ["scenario4","scenario3"]
    $ renpy.random.shuffle(scenario_war)
    $ scenario_money =  ["scenario2","scenario5"]
    $ renpy.random.shuffle(scenario_money)
    $ scenario_invest_little =  ["scenario8","scenario14"]
    $ renpy.random.shuffle(scenario_invest_little)
    $ scenario_big_invest =  ["scenario10","scenario18","scenario19","scenario20"]
    $ renpy.random.shuffle(scenario_big_invest)
    $ scenario_hard_invest =["scenario16","scenario12"]
    $ renpy.random.shuffle(scenario_hard_invest)
    $ scenario_random_invest = ["scenario17","scenario9","scenario10"]
    $ renpy.random.shuffle(scenario_random_invest)
    $ scenario_neg = ["scenario21","scenario22"]
    $ renpy.random.shuffle(scenario_neg)
    $ scenario_posi = ["scenario6","scenario15"]
    $ renpy.random.shuffle(scenario_posi)
    $ scenario_mid_game = ["scenario13","scenario11"]
    $ renpy.random.shuffle(scenario_mid_game)
    $ list_totale = []

    #generation de la list effective 
    $ list_totale.append(scenario_chill[0])
    $ list_totale.append(scenario_invest_little[0])
    $ list_totale.append(scenario_posi[0])
    $ list_totale.append(scenario_big_invest[0])
    $ list_totale.append(scenario_mid_game[0])
    $ list_totale.append(scenario_neg[0])
    $ list_totale.append(scenario_random_invest[0])
    $ list_totale.append(scenario_war[0])
    $ list_totale.append(scenario_money[0])
    $ list_totale.append(scenario_chill[1])
    $ list_totale.append(scenario_neg[1])
    $ list_totale.append(scenario_big_invest[2])
    $ list_totale.append(scenario_war[1])
    $ list_totale.append(scenario_hard_invest[0])
    $ list_totale.append(scenario_random_invest[1])
    
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