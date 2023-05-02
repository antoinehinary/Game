default money = 0
default power = 0
default happiness = 0
default population = 0

define p = Character('Hanta', color="#20B2AA")

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
    $ list_scenario_1 = ["scenario1" ,"scenario2","scenario3","scenario4","scenario5","scenario6","scenario7"]
    $ list_scenario_2 = ["scenario8","scenario9","scenario10","scenario11","scenario12","scenario12","scenario13","scenario15","scenario16","scenario17","scenario5","scenario18","scenario19","scenario20","scenario21","scenario22"]
    $ renpy.random.shuffle(list_scenario_1)
    $ renpy.random.shuffle(list_scenario_2)
    $ list_totale = []

#generation de la list effective 
$ i = 0 
$ j = 0
while i < 5 :
    $ list_totale.append(list_scenario_1[i])
    $ i += 1
while j < 15 :
    $ list_totale.append(list_scenario_2[j])
    $ j += 1
$ loop = 0
$ counter = 0
    

label game:
    scene auroraborealis
    jump presentation

    scene ville1
    show screen simple_stats_screen
    jump scenario1

label choice_done:
    if list_totale and loop <10 :
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

        python :
            renpy.jump(list_totale.pop(0))
    else :
        jump ending

label dead:
    "You lose"
            
label ending:
    "The end."

    return
