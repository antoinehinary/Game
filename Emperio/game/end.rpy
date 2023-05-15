label dead:
    show screen credit_UI
    "You lose"
            
label ending:
    show screen credit_UI
    scene path
    $ power =50
    $ score = power+money+happiness+population

    if population <= 25 :
        $ population_rank = "Ghost Town"
    elif population <= 50 :
        $ population_rank = "Baby Boomtown" 
    elif population <= 75 :
        $ population_rank = "Growing Like Weeds"
    elif population <= 100 : 
        $  population_rank = "The Packed-est Place on Earth"

    if money <= 25 :
        $ money_rank = "Penniless Place"
    elif money <= 50 :
        $ money_rank = "Counting Pennies" 
    elif money <= 75 :
        $ money_rank = "Scrooge McDuck's Dream"
    elif money <= 100 : 
        $ money_rank = "Filthy Rich"

    if power <= 25 :
        $ power_rank ="The Powerless Pipsqueak"
    elif power <= 50 :
        $ power_rank ="Barely in Charge"
    elif power <= 75 :
        $ power_rank ="The Emperor of Everything"
    elif power <= 100 : 
        $ power_rank ="Supreme Ruler"

    if happiness <= 25 :
        $ happiness_rank = "The village with the highest suicide rate"
    elif happiness <= 50 :
        $ happiness_rank = "Fake It 'Til You Make It"    
    elif happiness <= 75 :
        $ happiness_rank = "Smiling from Ear to Ear"
    elif happiness <= 100 :  
        $ happiness_rank = "Paradise Village" 

    hide text
    hide screen simple_stats_screen
    show screen end_stats_screen

    "Congratulations on completing the game! Here are the results of your village's progress."

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
