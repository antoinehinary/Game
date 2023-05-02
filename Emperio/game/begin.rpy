init:
    image Character_1 = "Character_1.png"
    image Character_2 = "Character_2.png"
    image Character_3 = "Character_3.png"
    image Character_4 = "Character_4.png"
    image ville_3 = "ville3.png"
    image Medieval_Town_4 = "medievaltown4.png"

transform midleft:
    xalign 0.35 yalign 1.0

transform midright:
    xalign 0.6 yalign 1.0

transform tieright:
    xalign 0.15 yalign 1.0

transform tierleft:
    xalign 0.8 yalign 1.0

default avatar = 1
image character = DynamicImage("Character_[avatar].png" )
image character_fight = DynamicImage("Character_[avatar]_fight.png" )
image character_sad = DynamicImage("Character_[avatar]_sad.png" )


screen stat_box1():
    frame:
        align (0.1,0.05)
        vbox:
            text "Initial power: 30" size 20
            text "Initial money: 30"size 20

screen stat_box2():
    frame:
        align (0.41,0.05)
        vbox:
            text "Initial power: 20" size 20
            text "Initial money: 40" size 20

screen stat_box3():
    frame:
        align (0.65,0.05)
        vbox:
            text "Initial power: 30" size 20
            text "Initial money: 30" size 20

screen stat_box4():
    frame:
        align (0.91,0.05)
        vbox:
            text "Initial power: 40" size 20
            text "Initial money: 20" size 20




label presentation:
    scene path
    "Welcome to Imperio, a strategy game where you play the role of the chief of a small village and your goal is to increase the resources and prosperity of your community by making smart choices during events." 
    "As the chief, you will need to balance the needs of your people with the demands of your expanding village, making sure that your population is happy and thriving."
    jump character_choice

label character_choice:

    "Choose your character before we begin - each character has unique strengths and weaknesses that will impact gameplay !"
    $ hubmenu = False
    show Character_1 at left :
        xzoom 0.3 yzoom 0.3
    show Character_2 at midleft :
        xzoom 0.3 yzoom 0.3
    show Character_3 at midright :
        xzoom 0.3 yzoom 0.3
    show Character_4 at right :
        xzoom 0.3 yzoom 0.3
    with Dissolve(.5)

    show screen stat_box1
    show screen stat_box2
    show screen stat_box3
    show screen stat_box4
    
    menu:
        "Character 1":
            $ avatar = 1
            $ power = 30
            $ money = 30

        "Character 2":
            $ avatar = 2
            $ power = 20
            $ money = 40

        "Character 3":
            $ avatar = 3
            $ power = 30
            $ money = 30

        "Character 4":
            $ avatar = 4
            $ power = 40
            $ money = 20

    hide Character_1
    hide Character_2
    hide Character_3
    hide Character_4
    hide screen stat_box1
    hide screen stat_box2
    hide screen stat_box3
    hide screen stat_box4

    show character at tierleft :
        xzoom 0.3 yzoom 0.3

    $ nb = avatar*10
    image character2 = DynamicImage("Character_[nb].png" )
    show character2 at tieright :
        xzoom 0.3 yzoom 0.3
    with Dissolve(.5)

    menu:
        "Style 1":
            hide character2
            hide character
            jump world_choice

        "Style 2":
            hide character
            hide character2
            $ avatar *=10
            jump world_choice

label world_choice:
    scene path
    "Please choose the world you would like to play in. This will impact the type of event you will have to face"
    show ville3 :
        xalign 0.1 yalign 0.5
        xzoom 0.4 yzoom 0.4
    show Medieval_Town_4  :
        xalign 0.9 yalign 0.5
        xzoom 0.4 yzoom 0.4
    menu:
        "North village":
            hide ville3
            hide Medieval_Town_4
            scene auroraborealis
            with irisout
 

        "Medieval village":
            hide ville3
            hide Medieval_Town_4
            scene medievaltown2
            with irisout 
            $ world =1

    "A little advice before you start, be careful not to let your resources drop to zero..."
    $ hubmenu = True
    jump scenario1
