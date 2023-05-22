label dead:
    image death animated = Movie(play="animation_death.webm", loop=False)
    show death animated at truecenter
    
    if avatar ==1:
        show sprite_death with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_death2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    "You lose"
    "The Game ended you have:"
    "Money: [money]{p}Power: [power]{p}Happiness: [happiness]{p}Population: [population]"
    if (money <= 0 or happiness <= 0 or power <= 0 or population <= 0):
        if money <= 0:
            "You were not carefull with your money. \nTips : You have only 15 turns to play, maybe it is better to not invest much at the end of the game... "
        if power <= 0:
            "You were not carefull with your power. \nTips : Look carefully at your village's power before fighting ! "
        if happiness <= 0:
            "You were not carefull with your happiness. \nYou can try the {a=https://findahelpline.com/ch}Helpline{\a}"
            "\n Tips : Invest in what is useful so you don't run out of money during key moments!"
        if population <= 0:
            "You were not carefull with your population. \nTips : Invest in your village to attract people and expend your population !"   
    if avatar ==1 :
        hide sprite_death with leftside
    if avatar == 2 :
        hide sprite_death2 with leftside
    jump end
            
label ending:
    show screen credit_UI
    scene path
    $ power =50
    $ score = power+money+happiness+population

    if population <= 25 :
        $ population_rank = "Ghost Town"
    elif population <= 50 :
        $ population_rank = "The borders are a little too closed..."
    elif population <= 75 :
        $ population_rank = "Baby Boomtown"
    elif population <= 100 : 
        $  population_rank = "Growing Like Weeds"

    if money <= 25 :
        $ money_rank = "Penniless Place"
    elif money <= 50 :
        $ money_rank = "Counting Pennies" 
    elif money <= 75 :
        $ money_rank = "Pixou's Dream"
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

    if world == 0 : 
        if power <50 :
            "Tips : Look carefully at your village's power before fighting ! "
        
        if money <50 :
            "Tips : You have only 15 turns to play, maybe it is better to not invest much at the end of the game... "
        
        if happiness <50 :
            "Tips : Invest in what is useful so you don't run out of money during key moments!"
        
        if population <50 :
            "Tips : Invest in your village to attract people and expend your population !"
    if world == 1 :
        if score >= 350 :
            "You obtain the title of {color=#f00}Emperor/Empress{/color} !"
        elif score >= 300 :
            "You obtain the title of {color=#f00}Duke/Duchess{/color} !"
        elif score >= 200 :
            "You obtain the title of {color=#f00}Count/Countess{/color} !"
        elif score >= 0 :
            "You obtain the title of {color=#f00}Baron/Baroness{/color} !"
    if world == 0 :
        jump level_2
    elif world == 1 :
        jump end


label end :
    "Thank you for playing, hope to see you soon ;) \nThe end."
    return