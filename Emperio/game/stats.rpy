screen simple_stats_screen:
    
    bar:
        xysize(200,55)
        value money 
        range money_max
        xalign 0.03
        yalign 0.02
        left_bar Frame("money_idle.png", 5,0)
        right_bar Frame("money_empty.png",2,0)
        left_gutter 49
        right_gutter 8
        thumb None
        thumb_shadow None
    text "Money : [money]/[money_max]" size 10 xalign 0.08 yalign 0.054

    bar:
        xysize(210,55)
        value power
        range power_max
        xalign 0.03
        yalign 0.08
        left_bar Frame("power_idle.png",5,0)
        right_bar Frame("power_empty.png",5,0)
        left_gutter 49
        right_gutter 20
        thumb None
        thumb_shadow None
    text "Power : [power]/[power_max]" size 10 xalign 0.08 yalign 0.112
   
    bar:
        xysize(200,55)
        value happiness
        range happiness_max
        left_bar Frame("happiness_idle.png", 5,0)
        right_bar Frame("happiness_empty.png", 5,0)
        xalign 0.03
        yalign 0.14
        left_gutter 50
        right_gutter 12
        thumb None
        thumb_shadow None
    text "Happiness : [happiness]/[happiness_max]" size 10 xalign 0.077 yalign 0.171

    bar:
        xysize(200,55)
        value population
        range population_max
        left_bar Frame("population_idle.png",2,0)
        right_bar Frame("population_empty.png",5,0)
        xalign 0.031
        yalign 0.2
        left_gutter 47
        right_gutter 11
        thumb None
        thumb_shadow None
    text "Population : [population]/[population_max]" size 10 xalign 0.077 yalign 0.228

