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

    text "[loop] /[turns_max]" size 20 xalign 0.95 yalign 0.06

screen end_stats_screen:
    
    bar:
        xysize(480,132)
        value money 
        range money_max
        xalign 0.25
        yalign 0.12
        left_bar Frame("money_idle.png", 5,0)
        right_bar Frame("money_empty.png",2,0)
        left_gutter 49
        right_gutter 8
        thumb None
        thumb_shadow None
    text "Money : [money] /[money_max]" size 25 xalign 0.345 yalign 0.2

    bar:
        xysize(500,132)
        value power
        range power_max
        xalign 0.253
        yalign 0.26
        left_bar Frame("power_idle.png",10,0)
        right_bar Frame("power_empty.png",5,0)
        left_gutter 49
        right_gutter 20
        thumb None
        thumb_shadow None
    text "Power : [power] /[power_max]" size 25 xalign 0.345 yalign 0.33
   
    bar:
        xysize(480,132)
        value happiness
        range happiness_max
        left_bar Frame("happiness_idle.png", 5,0)
        right_bar Frame("happiness_empty.png", 5,0)
        xalign 0.25
        yalign 0.4
        left_gutter 50
        right_gutter 12
        thumb None
        thumb_shadow None
    text "Happiness : [happiness] /[happiness_max]" size 25 xalign 0.35 yalign 0.45

    bar:
        xysize(480,132)
        value population
        range population_max
        left_bar Frame("population_idle.png",2,0)
        right_bar Frame("population_empty.png",5,0)
        xalign 0.253
        yalign 0.54
        left_gutter 47
        right_gutter 11
        thumb None
        thumb_shadow None
    text "Population : [population] /[population_max]" size 25 xalign 0.35 yalign 0.58

    frame:
        xsize 460
        ysize 60
        xalign 0.5
        yalign 0.7

        text "Total score : [score] / 400" :
            size 40

    vbox:
        align (0.9, 0.22)
        spacing 85  
        frame:
            text money_rank :
                color "#e8ba01"
                size 40 #xalign 0.8 yalign 0.14
        frame :
            text power_rank  :
                color "#c226ea"
                size 40 #xalign 0.8 yalign 0.27
        frame :
            text happiness_rank :
                color "#da2222"
                size 40 #xalign 0.8 yalign 0.4
        frame :
            text population_rank :
                color "#02e5e5"
                size 40 #xalign 0.8 yalign 0.52


#################################################### Screen with indices
screen gameUI:
    imagebutton:
        xalign 0.08
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "UI/loupe.png"
        action ShowMenu("StatsUI")
        
## Stats UI
screen StatsUI:    
    if world == 0 :
        add "auroraborealis.png"
    elif world == 1:
        add "medievaltown2.png"
    frame:
        background Solid("#00000090")     # or use any semi-transparent image you like
        align (0.5, 0.4)
        
        side "c r":
            area (0, 0, 1000, 150)

            viewport id "vp":
                draggable True

                vbox:
                    text tips
            vbar value YScrollValue("vp")

    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()

################################################## theory

image perso animated:

    "attack_extra0.png"
    pause 1.0
    "attack_extra1.png"
    pause 0.15
    "attack_extra2.png"
    pause 0.15
    "attack_extra3.png"
    pause 0.15
    "attack_extra4.png"
    pause 0.15
    "attack_extra5.png"
    pause 0.15
    "attack_extra6.png"
    repeat

screen theory:

    imagebutton:
        xalign 0.15
        yalign 0.95
        xoffset -30
        yoffset 30
        idle "transp.png"
        action ShowMenu("TheoryUI")
        
## Stats UI
screen TheoryUI:
    if world == 0 :
        add "auroraborealis.png"
    elif world == 1:
        add "medievaltown2.png"
    frame:
        background Solid("#00000090")     # or use any semi-transparent image you like
        align (0.5, 0.4)
        
        side "c r":
            area (0, 0, 1000, 320)

            viewport id "vp":
                draggable True

                vbox:
                    text theory_text
            vbar value YScrollValue("vp")
     
    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()


###################################################### Credits

## Screen with Stats Button
screen credit_UI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/credit_%s.png"
        action ShowMenu("Statcredit")

## Stats UI
screen Statcredit:

    if world == 0 :
        add "auroraborealis.png"
    elif world == 1:
        add "medievaltown2.png"
    frame:
        background Solid("#00000090")     # or use any semi-transparent image you like
        align (0.5, 0.4)
        
        side "c r":
            area (0, 0, 1000, 850)

            viewport id "vp":
                draggable True

                vbox:
                    text "{b}Credits{/b} : \n\n{b}Backgrounds{/b} : \nhttps://maxmeents.itch.io/228-free-medieval-town-backgrounds \n& \nhttps://lornn.itch.io/fantasy-ice-and-snow-backgrounds \n\n{b}Tips/credit button{/b} : \nhttps://zeillearnings.itch.io/stats-ui \n\n{b}Characters{/b} : \nhttps://pochipochihouse.itch.io/ \n\n{b}Stat bar{/b} : \nhttps://gamedeveloperstudio.itch.io/meters-and-levels \n\n{b}Game made by{/b} : Tristan Broccard, Anthony Dawoud, Antoine Hinary & Camille Challier" size 35 
            vbar value YScrollValue("vp")



    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()

screen s :
    frame:
        background Solid("#00000050")     # or use any semi-transparent image you like
        align (0.5, 0.4)
        
        side "c r":
            area (0, 0, 1000, 160)

            viewport id "vp":
                draggable True

                vbox:
                    text situation
            vbar value YScrollValue("vp")
