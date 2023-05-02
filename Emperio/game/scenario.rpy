transform offscrennbottomleft :
    xpos 0.0 xanchor 0.0 ypos 2.0 yanchor 1.0

default counter8 = 0
default counter9 = 0
default counter10 = 0
default counter11 = 0
default counter12 = 0
default counter13 = 0
default counter14 = 0
default counter15 = 0
default counter16 = 0
default counter17 = 0
default counter18 = 0
default counter19 = 0
default counter20 = 0
default counter21 = 0
default counter22 = 0
default counter23 = 0
default positif8 = False
default negatif8 = False
default positif9 = False
default negatif9 = False
default positif10 = False
default negatif10 = False
default positif11 = False
default negatif11 = False
default positif12 = False
default negatif12 = False
default positif13 = False
default negatif13 = False
default positif14 = False
default negatif14 = False
default positif15 = False
default negatif15 = False
default positif16 = False
default negatif16 = False
default positif17 = False
default negatif17 = False
default positif18 = False
default negatif18 = False
default positif19 = False
default negatif19 = False
default positif20 = False
default negatif20 = False
default positif21 = False
default negatif21 = False
default choice20_1 = False
default choice20_2 = False
default choice20_3 = False


define leftside = MoveTransition(delay=0.3,
                                enter = offscrennbottomleft,
                                leave = offscrennbottomleft,
                                old = False,
                                layers = ["master"],
                                time_warp = ease,
                                enter_time_warp=None,
                                leave_time_warp =None)

label no_money :
    "You don't have enough money to do this investissement ...."
    jump choice_done

label scenario1:
    $ counter1 = counter
    $counter += 1
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
        show character with leftside  :
            xzoom 0.3 yzoom 0.3
            xalign 1.0 yalign 1.0
 
        "The traders bring novelty to the village! \n Gain : money {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
        $ money +=10
        $ population +=10
        hide character
        jump conditions

    elif a==1 :
        show character_sad with leftside  :
            xzoom 0.3 yzoom 0.3
            xalign 1.0 yalign 1.0
        "The traders were suspicious...  \n Gain : happiness {image=arrow_down.png} 10 ?"
        $ happiness -= 10
        hide character_sad
        jump conditions

label choice1_2:
    $ menu_flag = False
    "No changes in resources"
    jump choice_done

###################################################### Event2
label scenario2:
    $counter += 1
    $ counter2 = counter
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
    jump conditions

label choice2_2:
    $ menu_flag = False
    "The village resents you for keeping these resources, and you lost a few people."
    $ money -= 5
    $ happiness -= 20
    $ population -= 10
    jump conditions

###################################################### Event3
label scenario3:
    $ counter3 = counter
    $ counter += 1
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
        $ happiness /=2
        $ money /=2
        $ population /=3
        $ power /= 2

    jump conditions

label choice3_2:
    $ menu_flag = True
    if money> 30 :
        "An agreement has been reached with the neighboring village. We lost some resources but gained a great ally."
        $ money -=10
        $ power +=40

    elif money <= 30 :
        "An agreement hasn’t been reached, we go to war"
        jump choice3_1

    jump conditions

###################################################### Event4
label scenario4:
    $ counter4 = counter
    $ counter += 1
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

    jump conditions

label choice4_2:
    $ menu_flag = True
    "You have lost the trust of the people...."
    $ happiness -=10
    jump conditions

###################################################### Event5
label scenario5:
    $ counter5 = counter
    $ counter += 1
    show text "A group of nomads passes through the village, offering to share their knowledge of survival skills in exchange for resources." at truecenter

    menu:
        "Trust the nomads and potentially gain valuable skills":
            jump choice5_1
        "Reject their offer and preserve resources":
            jump choice5_2

label choice5_1:
    $ a = renpy.random.randint(10,100)
    $ menu_flag = True
    if a < 80 :
        "Good choice! You are strengthening your village."
        $ money -=10
        $ population +=10
        $ happiness +=10
        $ power +=20

    else :
        "The traders were suspicious..."
        $ happiness -= 10
        $ money -= 10

    jump conditions

label choice5_2:
    $ menu_flag = True
    "..."
    jump conditions

###################################################### Events Positifs
label scenario6:
    show character with leftside :
            xzoom 0.3 yzoom 0.3
            xalign 1.0 yalign 1.0
    show text "The fishing of the day has been good! You are earning a lot of resources!" at truecenter
    $ happiness += 20
    $ money += 20
    hide character
    jump choice_done


label scenario7:
    show text "A neighboring village offers an alliance to our village. Some members of the population are suspicious… Do you accept the offer and potentially gain allies, or reject it and potentially preserve morale ?" at truecenter
    menu:
        "Sign an alliance.":
            jump choice7_1
        "Refuse the alliance.":
            jump choice7_2

label choice7_1:
    $ menu_flag = True
    " Gain : happiness {image=arrow_down.png} 5, power {image=arrow_up.png} 30"
    $ happiness -=5
    $ power += 30
    jump conditions

label choice7_2:
    $ menu_flag = True
    jump conditions



###################################################### Event8 : The Genius
label scenario8:
    $ counter8 = counter
    $ counter += 1
    $ positif8 = False
    $ negatif8 = False
    show text "A genius scientist passes by your village and wants to join." at truecenter

    menu:
        "Hire him":
            jump choice8_1
        "Ask him to leave.":
            jump choice8_2

label choice8_1:
    $ positif8 = True
    $ menu_flag = True
    "He was able to create technological advancement but he needed a lot of researche"
    $ population +=10
    jump conditions

label choice8_2:
    $ negatif8 = True
    $ menu_flag = True
    "He returned to his home village"
    jump conditions


###################################################### Event9
label scenario9:
    $ counter9 = counter
    $ counter += 1
    $ p = renpy.random.randint(10,100)
    show text "A new technology has become available for purchase. What should we do? " at truecenter

    menu:
        "Invest in purchasing the technology and potentially increase production or efficiency":
            jump choice9_1
        "Do not purchase the technology and save resources for other needs.":
            jump choice9_2

label choice9_1:
    $ menu_flag = True
    if 80 >= p :
        "The technology takes time to prosper"

    else:
        "The research came back without a reslut"
        $ money -=10

    jump choice_done

label choice9_2:
    $ menu_flag = True
    "You passed on the opportunity"
    jump conditions


###################################################### Event10
label scenario10:
    $ counter10 = counter
    $ counter += 1
    $ p = renpy.random.randint(10,100)
    show text "A rival village has become a major player in the region's trade network. " at truecenter

    menu:
        "Invest in developing our own trade network and potentially increase profits.":
            jump choice10_1
        "Do not purchase the technology and save resources for other needs.":
            jump choice10_2

label choice10_1:
    $ menu_flag = True
    if 60 >= p :
        "The network is successfully built"
        $ money -=20
        $ power +=10
        $ population +=10

    else:
        "You failed to create the network on your own"
        $ money -=10

    jump conditions

label choice10_2:
    $ menu_flag = True
    "You have lost an ally"
    $ power -=10
    jump conditions

###################################################### Event11
label scenario11:
    $ counter11 = counter
    $ counter += 1
    show text "A group of skilled craftsmen has offered to set up a workshop in the village" at truecenter

    menu:
        "Allow the craftsmen to set up shop and potentially increase the village's production capabilities.":
            jump choice11_1
        "Reject the offer and potentially miss out on production opportunities.":
            jump choice11_2

label choice11_1:
    $ menu_flag = True
    "The workshop was a great success"
    $ money +=20
    $ happiness +=10
    $ population +=10
    jump conditions

label choice11_2:
    $ menu_flag = True
    "You lost a good opportunity and the people are not satisfied"
    $ happiness -=10
    jump conditions


###################################################### Event12
label scenario12:
    $ counter12 = counter
    $ counter += 1
    show text "The village's population has grown exponentially, putting a strain on resources." at truecenter

    menu:
        "Enforce a law forbidding people from having more than 1 child.":
            jump choice12_1
        "Ignore it and ensure the population's happiness.":
            jump choice12_2

label choice12_1:
    $ positif12= True
    $ menu_flag = True
    "The population growth was reduced but the people are not happy with your decision"
    $ money +=10
    $ happiness -=20
    jump conditions

label choice12_2:
    $ negatif12 = True
    $ menu_flag = True
    "You have gained the love of the people but need to deal with the increase of the population"
    $ money -=20
    $ population +=10
    jump conditions


###################################################### Event13
label scenario13:
    $ counter13 = counter
    $ counter += 1
    show text "T A nearby wealthy village offered to buy land from your village." at truecenter

    menu:
        "Sell the land and potentially increase profits.":
            jump choice13_1
        "Reject the offer.":
            jump choice13_2

label choice13_1:
    $ menu_flag = True
    "You have formed an alliance and got money but lost power on such lands"
    $ money +=10
    $ power -=10
    jump conditions

label choice13_2:
    $ menu_flag = True
    "You rejected the land and held you kingdome steady"
    jump conditions


###################################################### Event14
label scenario14:
    $ counter14 = counter
    $ counter += 1
    show text "The village's education system is outdated and causing a skills gap in the workforce. What should we do?" at truecenter

    menu:
        "Invest in upgrading the education system and potentially increase economic efficiency.":
            jump choice14_1
        "Ignore the problem.":
            jump choice14_2

label choice14_1:
    $ menu_flag = True
    "You have upgraded your educational system and thus securing a future for the new generation"
    $ money -=10
    $ power +=10
    $ happiness +=10
    # $ money += 10 (in 7 turns)
    jump conditions

label choice14_2:
    $ menu_flag = True
    "You stayed with your current system"
    jump conditions

###################################################### Event15
label scenario15:
    $ counter15 = counter
    $ counter += 1
    show text "A neighboring village is experiencing a natural disaster and needs aid. What should we do?" at truecenter

    menu:
        "Provide aid to the neighboring village and potentially gain allies.":
            jump choice15_1
        "Ignore the situation and potentially damage relations with the neighboring village.":
            jump choice15_2

label choice15_1:
    $ positif15 = True
    #Rep: -money (now) ++power (++ 2 tour) ++happiness (+ 1 tour ++ 2 tour)
    jump conditions

label choice15_2:
    $ negatif15 = True
    #Rep: -power (- 1 tour) -happiness (- 1 tour)
    jump conditions


###################################################### Event16
label scenario16:
    $ counter16 = counter
    $ counter += 1
    show text "The village's infrastructure, such as roads and buildings, are in need of repair. What should we do?" at truecenter

    menu:
        "Invest in repairing the infrastructure and potentially improve efficiency.":
            jump choice16_1
        "Ignore the problem and potentially risk safety and efficiency.":
            jump choice16_2

label choice16_1:
    $ money -= 10
    #Rep: - money (now) + power (+ 1 tour) + happiness (+ 1 tour)
    $ positif16 = True
    jump conditions

label choice16_2:
    #Rep: -power (- 1 tour - - 2 tour) - happiness (- 1 tour - - 2 tour)
    $ negatif16 = True
    jump conditions


###################################################### Event17
label scenario17:
    $ p = renpy.random.randint(10,100)
    $ counter17 = counter
    $ counter += 1
    show text "A new crop has been introduced to the region which can potentially bring in more profits." at truecenter

    menu:
        "Invest in testing and cultivating the new crop and potentially increase profits.":
            jump choice17_1
        "Ignore the new crop and continue with current production.":
            jump choice17_2

label choice17_1:
    if p < 95 :
        $ positif17 = True
        $ money -=10
    #Rep: - money (now) ++money (++ 2 tour +++ 5 tour) (maybe! P = 95%)
    jump conditions

label choice17_2:
    $ negatif17 = True
    #Rep: no changes
    jump conditions


###################################################### Event18
label scenario18:
    show text "The village elders propose investing in science and technology to improve the quality of life in the village, but it requires a significant amount of resources. What should we do ?" at truecenter
    $ counter18 = counter
    $ counter += 1
    $ positif18 = False
    $ negatif18 = False
    menu:
        "Invest heavily in science and technology research and development.":
            if money >= 20 :
                jump choice18_1
            else :
                jump no_money
        "Save resources for other pressing needs.":
            jump choice18_2

label choice18_1:
    $ positif18 = True
    # Rep: ++happiness ++power (2 tours)
    $ menu_flag = True
    "Gain : money {image=arrow_down.png} :20"
    $ money -=20
    jump conditions

label choice18_2:
    $ negatif18 = True
    $ menu_flag = True
    show character_sad with leftside :
            xzoom 0.3 yzoom 0.3
            xalign 1.0 yalign 1.0
    "The villagers become frustrated with the lack of progress and innovation. \n Gain : happiness {image=arrow_down.png} 10"
    $ happiness -=10
    jump conditions

###################################################### Event19
label scenario19:
    $ counter19 = counter
    $ counter += 1
    show text "Your village having expanded a lot, do you want to invest in new schools?" at truecenter

    menu:
        "Invest heavily in education by building schools and hiring qualified teachers, despite the high costs.":
            if money >= 20 :
                jump choice19_1
            else :
                jump no_money
            
        "Invest minimally in education, citing the high costs and the need to prioritize other pressing needs. ":
            jump choice19_2

label choice19_1:
    $ positif19= True
    # Rep: ++happiness, ++power, + argent (3 tours)
    $ menu_flag = True
    "Gain : money {image=arrow_down.png} :20"
    $ money -=20
    jump conditions

label choice19_2:
    $ negatif19 = True
    # Rep : -happiness, -population (3tours)
    $ menu_flag = True
    "Gain : happiness {image=arrow_down.png} 10, population {image=arrow_down.png} 10"
    $ happiness -=10
    $ population -=10
    jump conditions


###################################################### Event20
label scenario20:
    $ counter20 = counter
    $ counter += 1
    show text "A technological breakthrough presents the opportunity to increase the village’s wealth and resources, but some members of the population areconcerned about the ethical implications of the technology and the player must decide whether to pursue it or not." at truecenter

    menu:
        "Make a significant investment in science research and development, despite the high costs.":
            if money >= 30 :
                jump choice20_1
            else :
                jump no_money
        "Make a moderate investment in science research and development, balancing the need for progress with fiscal responsibility.":
            if money >= 20 :
                jump choice20_2
            else :
                jump no_money
        "Make a minimal investment in science research and development, citing the high costs and the need to prioritize other pressing needs." :
            if money >= 10 :
                jump choice20_3
            else :
                jump no_money

label choice20_1:
    $ choice20_1 = True
    # Rep : +++happiness, +++power (2tours)
    $ menu_flag = True
    " Gain : money {image=arrow_down.png}30"
    $ money -=30
    jump conditions

label choice20_2:
    $ choice20_2 = True
    # Rep : ++happiness, ++power (2tours)
    "Gain : money {image=arrow_down.png} 20"
    $ money -=20
    jump choice_done

label choice20_3:
    $ hoice20_3 = True
    # Rep : -happiness, +power (2tours)
    $ menu_flag = True
    "Gain : money {image=arrow_down.png} 10"
    $ money -=10
    jump conditions


###################################################### Events negatifs
label scenario21:
    show character_sad with leftside :
        xzoom 0.3 yzoom 0.3
        xalign 1.0 yalign 1.0
    show text "A disease outbreak is spreading in the village causing some villagers to become ill. \n Gain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 5, population {image=arrow_down.png} 10 " at truecenter
    $ happiness -= 5
    $ money -= 5
    $ population -= 10
    hide character_sad
    jump conditions

label scenario22:
    show character_sad with leftside :
            xzoom 0.3 yzoom 0.3
            xalign 1.0 yalign 1.0
    show text " A severe cold snap has hit the region, causing crops to fail and leaving the village without food.\n Gain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 10, population {image=arrow_down.png} 5 " at truecenter
    $ happiness -= 5
    $ money -= 10
    $ population -= 5
    hide character_sad
    jump conditions

label conditions: 
    if counter > (counter8) and negatif8 == True:
        $ money += 10 
    if counter > (counter8 + 1) and negatif8 == True:
        $ money += 20
    if counter > (counter9) and negatif9 == True:
        $ money += 10 
    if counter > (counter9 + 1) and negatif9 == True:
        $ money += 10
    if counter > (counter9 + 2) and negatif9 == True:
        $ money += 10
        $negatif9 = False
    if counter > (counter10 + 2):
        $ money += 20
    if counter > (counter10):
        $ power += 10
    if counter > (counter11):
        $ money += 10
    if counter > (counter11 + 1):
        $ happiness += 10
    if counter > (counter12) and negatif12 == True:
        $ population += 10
    if counter > (counter12 + 1) and negatif12 == True:
        $ population += 10
    if counter > (counter12 + 2) and negatif12 == True:
        $ population += 10
        $ negatif12 = False
    if counter > (counter14):
        $ power += 10
        $ happiness += 10
    if counter > (counter14 + 2):
        $ money += 10
    if counter > (counter15 + 1) and (positif15 == True):
        $ power += 20
        $ happiness += 10
    if counter > (counter15 + 1) and (negatif15 == True):
        $ power -= 10
        $ happiness -= 10
    if counter > (counter16) and (positif16 == True):
        $ power += 10
        $ happiness += 10
    if counter > (counter16) and (negatif16 == True):
        $ power -= 10
        $ happiness -= 10
    if counter > (counter16 + 1) and (negatif16 == True):
        $ power -= 20
        $ happiness -= 20
    if counter > (counter17) and (positif17 == True):
        $ money += 20
        $ happiness -= 10
    if counter > (counter17 + 1) and (negatif17 == True):
        $ money += 10
    if counter > (counter18 + 1) and (positif18 == True):
        $ power += 10
        $ happiness += 10
    if counter > (counter19 + 1) and (positif19 == True):
        $ power += 10
        $ happiness += 10   
        $ money += 10
    if counter > (counter19 + 1) and (negatif19 == True):
        $ happiness -= 10
        $ population -= 10
    if counter > (counter20 + 1) and (choice20_1 == True):
        $ happiness += 30
        $power += 30
    if counter > (counter20 + 1) and (choice20_2 == True):
        $ happiness += 20
        $ power += 20
    if counter > (counter19 + 1) and (choice20_3 == True):
        $ happiness -= 10
        $ population += 10
    jump choice_done