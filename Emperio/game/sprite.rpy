screen stat_box1():
    frame:
        align (0.3,0.05)
        vbox:
            text "Initial power: 20" size 20
            text "Initial money: 20"size 20

screen stat_box2():
    frame:
        align (0.65,0.05)
        vbox:
            text "Initial power: 10" size 20
            text "Initial money: 30" size 20

#mage
image perso animated:

    "mage/attack_extra0.png"
    pause 1.0
    "mage/attack_extra1.png"
    pause 0.15
    "mage/attack_extra2.png"
    pause 0.15
    "mage/attack_extra3.png"
    pause 0.15
    "mage/attack_extra4.png"
    pause 0.15
    "mage/attack_extra5.png"
    pause 0.15
    "mage/attack_extra6.png"
    repeat

image sprite_attack :
    "knight/attack_extra1.png"
    pause 1.0
    "knight/attack_extra2.png"
    pause 0.15
    "knight/attack_extra3.png"
    pause 0.15
    "knight/attack_extra4.png"
    pause 0.15
    "knight/attack_extra5.png"
    pause 0.15
    "knight/attack_extra6.png"
    pause 0.15
    "knight/attack_extra7.png"
    pause 0.15
    "knight/attack_extra8.png"
    repeat
image sprite_death :
    "knight/death1.png"
    pause 1.0
    "knight/death2.png"
    pause 0.2
    "knight/death3.png"
    pause 0.2
    "knight/death4.png"
    pause 0.2
    "knight/death5.png"
    pause 0.2
    "knight/death6.png"
    pause 0.2
    "knight/death7.png"
    pause 0.2
    "knight/death8.png"
    pause 0.2
    "knight/death9.png"
    pause 0.2
    "knight/death10.png"
image sprite_hurt :
    "knight/hurt1.png"
    pause 1.0
    "knight/hurt2.png"
    pause 0.2
    "knight/hurt3.png"
    pause 0.2
    "knight/hurt4.png"
    pause 0.2
    "knight/hurt1.png"
    pause 0.5

image sprite_happy :
    "knight/idle1.png"
    pause 1.0
    "knight/idle2.png"
    pause 0.2
    "knight/idle3.png"
    pause 0.2
    "knight/idle4.png"
    pause 0.2
    "knight/idle1.png"
    pause 0.5
    repeat


image sprite_attack2 :
    "rogue/attack_extra1.png"
    pause 1.0
    "rogue/attack_extra2.png"
    pause 0.15
    "rogue/attack_extra3.png"
    pause 0.15
    "rogue/attack_extra4.png"
    pause 0.15
    "rogue/attack_extra5.png"
    pause 0.15
    "rogue/attack_extra6.png"
    pause 0.15
    "rogue/attack_extra7.png"
    pause 0.15
    "rogue/attack_extra8.png"
    pause 0.15
    "rogue/attack_extra9.png"
    pause 0.15
    "rogue/attack_extra10.png"
    pause 0.15
    "rogue/attack_extra11.png"
    repeat

image sprite_death2 :
    "rogue/death1.png"
    pause 1.0
    "rogue/death2.png"
    pause 0.15
    "rogue/death3.png"
    pause 0.15
    "rogue/death4.png"
    pause 0.15
    "rogue/death5.png"
    pause 0.15
    "rogue/death6.png"
    pause 0.15
    "rogue/death7.png"
    pause 0.15
    "rogue/death8.png"
    pause 0.15
    "rogue/death9.png"
    pause 0.15
    "rogue/death10.png"
    pause 0.15

image sprite_hurt2 :
    "rogue/hurt1.png"
    pause 1.0
    "rogue/hurt2.png"
    pause 0.2
    "rogue/hurt3.png"
    pause 0.2
    "rogue/hurt4.png"
    pause 0.2
    "rogue/hurt1.png"
    pause 0.5
    repeat

image sprite_happy2 :
    "rogue/idle1.png"
    pause 1.0
    "rogue/idle2.png"
    pause 0.15
    "rogue/idle3.png"
    pause 0.15
    "rogue/idle4.png"
    pause 0.15
    "rogue/idle5.png"
    pause 0.15
    "rogue/idle6.png"
    pause 0.15
    "rogue/idle7.png"
    pause 0.15
    "rogue/idle8.png"
    pause 0.15
    "rogue/idle9.png"
    pause 0.15
    "rogue/idle10.png"
    pause 0.15
    "rogue/idle12.png"
    pause 0.15
    "rogue/idle13.png"
    pause 0.15
    "rogue/idle14.png"
    pause 0.15
    "rogue/idle15.png"
    pause 0.15
    "rogue/idle16.png"
    pause 0.15
    "rogue/idle17.png"
    pause 0.15
    "rogue/idle18.png"
    pause 0.15
    repeat

label character_choice:

    "Choose your character before we begin - each character has unique strengths and weaknesses that will impact gameplay !"
    $ hubmenu = False
    show sprite_attack :#with leftside :
        xzoom 5  yzoom 5
        xalign 0.3 yalign 0.6

    show sprite_attack2 :#with leftside :
        xzoom 5  yzoom 5
        xalign 0.8 yalign 0.6
    with Dissolve(.5)

    show screen stat_box1
    show screen stat_box2
    
    menu:
        "Character 1":
            $ avatar = 1
            $ power = 20
            $ money = 20

        "Character 2":
            $ avatar = 2
            $ power = 10
            $ money = 30

    hide sprite_attack #with leftside
    hide sprite_attack2 #with leftside
    hide screen stat_box1
    hide screen stat_box2

    $ world = 0
    scene auroraborealis
    with irisout
    "A little advice before you start, be careful not to let your resources drop to zero..."
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ theory_text = "Hey ! I'm here to help you make the best decisions ! Good luck :)"
    show screen theory
    "If you're unsure of a decision, you can always listen to your wise Maester by clicking on it !"
    $ hubmenu = True
    hide screen theory
    hide perso animated
    jump choice_done

