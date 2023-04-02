label presentation:
    show personnage:
        xalign 0.0
        yalign 1.0
    p "Hi ! My name is Hanta, I am the chief of an Inuit village. You are here to help me grow and improve my village. I am counting on you!"
    hide personnage
    scene ville1

label scenario1:
    show screen simple_stats_screen
    show text "A group of traders arrives in the village with exotic goods, but some members of the population object to their presence. Should we allow the traders to stay ?" at truecenter

    menu:
        "Yes and potentially increase wealth.":
            jump choice1_1
        "Ask them to leave to potentially preserve morale.":
            jump choice1_2

label choice1_1:
    $ a = renpy.random.choice([0,1])
    $ menu_flag = True
    if a==0 :
        "The traders bring novelty to the village!"
        $ money +=2
        $ population +=10
        jump choice_done

    elif a==1 :
        "The traders were suspicious..."
        $ happiness -= 10
        jump choice_done

label choice1_2:
    $ menu_flag = False
    "No changes in resources"
    jump choice_done

###################################################### Event2
label scenario2:
    show text "A famine strikes the village causing a drop in morale, what should we do ?" at truecenter

    menu:

        "Distributing all resources and taking care of the people":
            jump choice2_1
        "Distribute some resources but save most for later.":
            jump choice2_2

label choice2_1:
    $ menu_flag = True
    "You have been able to take care of our village and this leads to an increase in morale and trust of the village in the long term."
    $ happiness +=20
    $ money -=20
    jump choice_done

label choice2_2:
    $ menu_flag = False
    "The village resents you for keeping these resources, and you lost a few people."
    $ money -= 5
    $ happiness -= 20
    $ population -= 10
    jump choice_done

###################################################### Event3
label scenario3:
    $ a = renpy.random.randint(10,100)
    show text "A neighboring tribe (power = %d) is attacking the village, what should we do ?" % a at truecenter

    menu:
        "Declare war (potentially gain ressources)":
            jump choice3_1
        "Try to negotiate (potentially don’t lose any villagers)":
            jump choice3_2

label choice3_1:
    $ menu_flag = True
    if power>=a :
        "We succeeded in repelling the enemies ! We were able to seize their resources but we lost many fighters and the morale of the village is at its lowest."
        $ happiness -=10
        $ money +=10
        $ population -=10
        $ power +=10

    elif power< a :
        "The enemies were stronger than us, the village was almost destroyed…"
        $ happiness =0
        $ money =0
        $ population -=10
        $ power =10

    jump choice_done

label choice3_2:
    $ menu_flag = True
    if money> 70 :
        "An agreement has been reached with the neighboring village. We lost some resources but gained a great ally."
        $ money -=10
        $ power +=40

    elif money< 70 :
        "An agreement hasn’t been reached, we go to war"
        jump choice3_1

    jump choice_done

###################################################### Event4
label scenario4:
    $ p = renpy.random.randint(10,100)
    show text "A nearby village is being attacked by raiders !" at truecenter

    menu:
        "Offer aid and potentially gain allies":
            jump choice4_1
        "Ignore":
            jump choice4_2

label choice4_1:
    $ menu_flag = True
    if power>=p :
        "We succeeded in repelling the enemies ! We lost some fighters but gained a new ally !"
        $ money +=10
        $ population -=10
        $ power +=30

    elif power< p :
        "The enemies were stronger than us, the village was almost destroyed…"
        $ happiness =0
        $ money =0
        $ population -=10
        $ power =10

    jump choice_done

label choice4_2:
    $ menu_flag = True
    "You have lost the trust of the people...."
    $ happiness -=10
    jump choice_done

###################################################### Event5
label scenario5:
    show text "A group of nomads passes through the village, offering to share their knowledge of survival skills in exchange for resources." at truecenter

    menu:
        "Trust the nomads and potentially gain valuable skills":
            jump choice5_1
        "Reject their offer and preserve resources":
            jump choice5_2

label choice5_1:
    $ a = renpy.random.choice([0,1])
    $ menu_flag = True
    if a==0 :
        "Good choice! You are strengthening your village."
        $ money -=10
        $ population +=10
        $ happiness +=10
        $ power +=20

    elif a==1 :
        "The traders were suspicious..."
        $ happiness -= 10
        $ money -= 10

    jump choice_done

label choice5_2:
    $ menu_flag = True
    "..."
    jump choice_done

###################################################### Event6
label scenario6:
    show text "The fishing of the day has been good! You are earning a lot of resources!" at truecenter
    $ happiness += 20
    $ money += 20
    jump choice_done
