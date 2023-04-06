################################################ Event Mixtes

label scenario1:
    $ hubmenu = True 
    show screen simple_stats_screen
    show text "A group of traders arrives in the village with exotic goods, but some members of the population object to their presence. Should we allow the traders to stay ?" at truecenter

    menu:
        "Yes and potentially increase wealth.":
            jump choice1_1
        "Ask them to leave to preserve morale.":
            jump choice1_2

label choice1_1:
    $ a = renpy.random.choice([0,1])
    $ menu_flag = True
    if a==0 :
        show character at left :
            xzoom 0.3 yzoom 0.3
        "The traders bring novelty to the village! \n Gain : money {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
        $ money +=10
        $ population +=10
        hide character
        jump choice_done

    elif a==1 :
        show character_sad at left :
            xzoom 0.3 yzoom 0.3
        "The traders were suspicious...  \n Gain : happiness {image=arrow_down.png} 10 ?"
        $ happiness -= 10
        hide character_sad
        jump choice_done

label choice1_2:
    $ menu_flag = False
    "No changes in resources"
    jump choice_done

###################################################### Event2
label scenario2:
    show text "A famine strikes the village causing a drop in morale, what should we do ?" at truecenter

    menu:

        "Distributing all resources and taking care of the people.":
            jump choice2_1
        "Distribute some resources but save most for later.":
            jump choice2_2

label choice2_1:
    $ menu_flag = True
    "You have been able to take care of our village and this leads to an increase in morale and trust of the village in the long term.\n Gain : happiness {image=arrow_up.png} 20, money {image=arrow_down.png} 20"
    $ happiness +=20
    $ money -=20
    jump choice_done

label choice2_2:
    $ menu_flag = False
    "The village resents you for keeping these resources, and you lost a few people.  \n Gain : happiness {image=arrow_down.png} 10, money {image=arrow_down.png} 5, population {image=arrow_down.png} 10"
    $ money -= 5
    $ happiness -= 10
    $ population -= 10
    jump choice_done

###################################################### Event3
label scenario3:
    $ a = renpy.random.randint(10,100)
    show text "A neighboring tribe (power = %d) is attacking the village, what should we do ?" % a at truecenter

    menu:
        "Declare war and potentially gain ressources":
            jump choice3_1
        "Try to negotiate and potentially don’t lose any villagers)":
            jump choice3_2

label choice3_1:
    $ menu_flag = True
    if power>=a :
        show character_fight at left :
            xzoom 0.3 yzoom 0.3
        "We succeeded in repelling the enemies ! We were able to seize their resources but we lost many fighters and the morale of the village is at its lowest. \n Gain : happiness {image=arrow_down.png} 10, money {image=arrow_up.png} 20, population {image=arrow_down.png} 10, power {image=arrow_up.png} 20"
        $ happiness -=10
        $ money +=20
        $ population -=10
        $ power +=20
        hide character_fight

    elif power< a :
        show character_sad at left :
            xzoom 0.3 yzoom 0.3
        "The enemies were stronger than us, the village was almost destroyed… \n Gain : happiness {image=arrow_down.png} =0, money {image=arrow_down.png} =0, population {image=arrow_down.png} 10, power {image=arrow_down.png} 10"
        $ happiness =0
        $ money =0
        $ population -=10
        $ power =-10
        hide character_sad

    jump choice_done

label choice3_2:
    $ menu_flag = True
    if money + power > 40 :
        show character at left :
            xzoom 0.3 yzoom 0.3
        "An agreement has been reached with the neighboring village. We lost some resources but gained a great ally.\n Gain : money {image=arrow_down.png} 10, power {image=arrow_up.png} 40"
        $ money -=10
        $ power +=40
        hide character

    elif money< 70 :
        show character_sad at left :
            xzoom 0.3 yzoom 0.3
        "An agreement hasn’t been reached, we are paying a heavy tol, \n Gain : money {image=arrow_down.png} /5"
        $ money /=5
        hide character_sad

    jump choice_done

###################################################### Event4
label scenario4:
    $ p = renpy.random.randint(10,50)
    show text "A nearby village is being attacked by raiders !" at truecenter

    menu:
        "Offer aid and potentially gain allies":
            jump choice4_1
        "Ignore":
            jump choice4_2

label choice4_1:
    $ menu_flag = True
    if power>=p :
        show character_fight at left :
            xzoom 0.3 yzoom 0.3
        "We succeeded in repelling the enemies ! We lost some fighters but gained a new ally !\n Gain :money {image=arrow_up.png} 10, population {image=arrow_down.png} 10, power {image=arrow_up.png} 30"
        $ money +=10
        $ population -=10
        $ power +=30
        hide character_fight

    elif power< p :
        show character_sad at left :
            xzoom 0.3 yzoom 0.3
        "The enemies were stronger than us, the village was almost destroyed… \n Gain : happiness {image=arrow_down.png} =0, money {image=arrow_down.png} =0, population {image=arrow_down.png} 10, power {image=arrow_down.png} 10"
        $ happiness =0
        $ money =0
        $ population -=10
        $ power -=10
        hide character_sad

    jump choice_done

label choice4_2:
    $ menu_flag = True
    show character_sad at left :
            xzoom 0.3 yzoom 0.3
    "You have lost the trust of the people.... \n Gain : happiness {image=arrow_down.png} 10"
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
        show character at left :
            xzoom 0.3 yzoom 0.3
        "Good choice! You are strengthening your village. \n Gain : happiness {image=arrow_up.png} 10, money {image=arrow_down.png} 10, population {image=arrow_up.png} 10, power {image=arrow_up.png} 20"
        $ money -=10
        $ population +=10
        $ happiness +=10
        $ power +=20
        hide character

    elif a==1 :
        show character_sad at left :
            xzoom 0.3 yzoom 0.3
        "The traders were suspicious... \n Gain : happiness {image=arrow_down.png} 10, money {image=arrow_down.png} 10"
        $ happiness -= 10
        $ money -= 10
        hide character_sad

    jump choice_done

label choice5_2:
    $ menu_flag = True
    "..."
    jump choice_done

###################################################### Event6
label scenario6:
    show text "A group of refugees arrive in the village seeking shelter. You must decide whether to accept them and potentially gain allies, or reject them and potentially preserve resources." at truecenter

    menu:
        "Accept them":
            jump choice6_1
        "Reject them":
            jump choice6_2

label choice6_1:
    $ menu_flag = True
    "Gain : money {image=arrow_down.png} 20, population {image=arrow_up.png} 10, power {image=arrow_up.png} 10"
    $ power += 10
    $ population +=10
    $ money -= 20
    jump choice_done

label choice6_2:
    $ menu_flag = True
    jump choice_done


###################################################### Event7
label scenario7:
    show text "A band of bandits is terrorizing the village’s trade routes !" at truecenter

    menu:
        "Invest resources in hiring more guards":
            jump choice7_1
        "Prioritize other needs.":
            jump choice7_2

label choice7_1:
    $ menu_flag = True
    show character at left :
            xzoom 0.3 yzoom 0.3
    "Gain : money {image=arrow_down.png} 20, power {image=arrow_up.png} 10"
    $ power += 10
    $ money -= 10
    jump choice_done
    hide character

label choice7_2:
    $ menu_flag = True
    "Gain : population {image=arrow_down.png} 10"
    jump choice_done


###################################################### Events positifs
label scenariop1:
    show character at left :
            xzoom 0.3 yzoom 0.3
    show text "The fishing of the day has been good! You are earning a lot of resources!" at truecenter
    $ happiness += 20
    $ money += 20
    hide character
    jump choice_done


label scenariop2:
    show text "A neighboring village offers an alliance to our village. Some members of the population are suspicious… Do you accept the offer and potentially gain allies, or reject it and potentially preserve morale ?" at truecenter
    menu:
        "Sign an alliance.":
            jump choicep2_1
        "Refuse the alliance.":
            jump choicep2_2

label choicep2_1:
    $ menu_flag = True
    " Gain : happiness {image=arrow_down.png} 5, power {image=arrow_up.png} 30"
    $ happiness -=5
    $ power += 30
    jump choice_done

label choicep2_2:
    $ menu_flag = True
    jump choice_done
    

###################################################### Events negatifs
label scenarion1:
    show character_sad at left :
        xzoom 0.3 yzoom 0.3
    show text "A disease outbreak is spreading in the village causing some villagers to become ill. \n Gain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 5, population {image=arrow_down.png} 10 " at truecenter
    $ happiness -= 5
    $ money -= 5
    $ population -= 10
    hide character_sad
    jump choice_done

label scenarion2:
    show character_sad at left :
            xzoom 0.3 yzoom 0.3
    show text " A severe cold snap has hit the region, causing crops to fail and leaving the village without food.\n Gain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 10, population {image=arrow_down.png} 5 " at truecenter
    $ happiness -= 5
    $ money -= 10
    $ population -= 5
    hide character_sad
    jump choice_done