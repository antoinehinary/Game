default money = 0
default power = 0
default happiness = 0
default population = 0

screen simple_stats_screen:
    frame:
        xalign 0.0 yalign 0.01
        vbox:
            text "{image=coin.png}: [money]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value money
                    range money_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5         
                
    frame:
        xalign 0.0 yalign 0.09
        vbox:
            text "{image=power.png}: [power]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value power
                    range power_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5

    frame:
        xalign 0.1 yalign 0.01
        vbox:
            text "{image=hapiness.png}: [happiness]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value happiness
                    range happiness_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5

    frame:
        xalign 0.1 yalign 0.09
        vbox:
            text "{image=population.png}: [population]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value population
                    range population_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
# The game starts here.
label start:
    $ money = 30
    $ money_max = 50
    $ power =30
    $ power_max =50
    $ happiness =30
    $ happiness_max =50
    $ population =50
    $ population_max =50

label game:
    
    show screen simple_stats_screen
    scene village
    show text "Script Events 1" at truecenter

menu:

    "Choix 1":
        jump choice1_yes
    "Choix 2":
        jump choice1_no

label choice1_yes:
    $ menu_flag = True
    "Script choix 1"
    $ power =2
    jump choice1_done

label choice1_no:
    $ menu_flag = False
    "Script choix 1"
    $ power =2
    jump choice1_done

label choice1_done:
    
    show screen simple_stats_screen
    scene village
    show text "Script Events 2" at truecenter

menu:

    "Choix 1":
        jump choice2_yes
    "Choix 2":
        jump choice2_no

label choice2_yes:
    $ menu_flag = True
    "Script choix 1"
    $ power =2
    jump choice2_done

label choice2_no:
    $ menu_flag = False
    "Script choix 1"
    $ power =2
    jump choice2_done

label choice2_done:
        
    hide screen simple_stats_screen
    
label ending:
    "The end."

    return
