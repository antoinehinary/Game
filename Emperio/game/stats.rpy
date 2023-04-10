screen simple_stats_screen:
    
    bar:
        xysize(240,66)
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
    text "Money : [money] /[money_max]" size 13 xalign 0.09 yalign 0.06

    bar:
        xysize(250,66)
        value power
        range power_max
        xalign 0.03
        yalign 0.09
        left_bar Frame("power_idle.png",5,0)
        right_bar Frame("power_empty.png",5,0)
        left_gutter 49
        right_gutter 20
        thumb None
        thumb_shadow None
    text "Power : [power] /[power_max]" size 13 xalign 0.09 yalign 0.128
   
    bar:
        xysize(240,66)
        value happiness
        range happiness_max
        left_bar Frame("happiness_idle.png", 5,0)
        right_bar Frame("happiness_empty.png", 5,0)
        xalign 0.03
        yalign 0.16
        left_gutter 50
        right_gutter 12
        thumb None
        thumb_shadow None
    text "Happiness : [happiness] /[happiness_max]" size 13 xalign 0.088 yalign 0.195

    bar:
        xysize(240,66)
        value population
        range population_max
        left_bar Frame("population_idle.png",2,0)
        right_bar Frame("population_empty.png",5,0)
        xalign 0.031
        yalign 0.23
        left_gutter 47
        right_gutter 11
        thumb None
        thumb_shadow None
    text "Population : [population] /[population_max]" size 13 xalign 0.088 yalign 0.26

