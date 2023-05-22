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
default counter24 = 0

default actif8 = False
default actif9 = False
default actif10 = False
default actif11 = False
default actif12 = False
default actif14 = False
default actif15 = False
default actif16 = False
default actif17 = False
default actif18 = False
default actif19 = False
default actif20 = False
default actif24 = False

default positif15 = False
default negatif15 = False
default positif16 = False
default negatif16 = False
default positif19 = False
default negatif19 = False

default choice20_1 = False
default choice20_2 = False
default choice20_3 = False

define leftside = MoveTransition(delay=0.3,enter = offscrennbottomleft,leave = offscrennbottomleft,old = False,layers = ["master"],time_warp = ease,enter_time_warp=None,leave_time_warp =None)

label no_money :
    "You don't have enough money to do this investissement ...."
    jump conditions

label scenario1:
    $ tips = "{b}Tips{/b} : If you choose to trust the traders, you may as well gain power and population but also lose happiness in the event of a scam."
    show screen gameUI
    $ theory_text = "{b}Theory{/b} : Free trade is good for the economy: new goods are introduced, shortages of materials or food can be easily filled. However, if the state does not control the gradual entry of this system, the local economy can suffer if too many goods arrive too quickly at a price that defies all competition. There may also be negative consequences if industry or crafts are too concentrated in single markets."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ counter1 = counter
    show screen simple_stats_screen
    $ situation = "A group of traders arrives in the village with exotic goods, but some members of the population object to their presence. Should we allow the traders to stay ?"
    show screen s

    menu:
        "Yes and potentially increase money." :
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice1_1
        "Ask them to leave to potentially preserve happiness.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice1_2

label choice1_1:
    $ a = renpy.random.choice([0,1])
    $ menu_flag = True
    if a==0 :
        if avatar ==1:
            show sprite_happy with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_happy2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        image money animated = Movie(play="animation_gain_money.webm", loop=False)
        show money animated at truecenter
        "The traders bring novelty to the village ! \nGain : money {image=arrow_up.png} 10, population {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10"
        $ money +=10
        $ population +=10
        $ happiness +=10
        if avatar ==1 :
            hide sprite_happy with leftside
        if avatar == 2 :
            hide sprite_happy2 with leftside
        jump conditions

    elif a==1 :
        if avatar ==1:
            show sprite_hurt with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_hurt2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "The traders were suspicious...  \nGain : happiness {image=arrow_down.png} 5"
        $ happiness -= 5
        if avatar ==1 :
            hide sprite_hurt with leftside
        if avatar == 2 :
            hide sprite_hurt with leftside
        jump conditions

label choice1_2:
    $ menu_flag = False
    "No changes in resources"
    jump conditions

###################################################### Event2
label scenario2:
    $ theory_text = "{b}Theory{/b} : Crises are recurrent events for all civilisations and economies. During such a shock, if the stocks of capital, i.e. the wealth saved, are sufficient, the economy can quickly return to its equilibrium level, i.e. the level before the crisis. However, the village will be temporarily impoverished because it must reinvest to repair the damage caused."
    $ counter += 1
    $ counter2 = counter
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "A famine strikes the village causing a drop in morale, what should we do ?"
    show screen s

    menu:
        "Distributing all resources and taking care of the people":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice2_1
        "Distribute some resources but save most for later.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice2_2

label choice2_1:
    $ menu_flag = True
    "You have been able to take care of our village and this leads to an increase in morale and trust of the village in the long term. \nGain : happiness {image=arrow_up.png} 20, money {image=arrow_down.png} 20"
    $ happiness +=20
    $ money -=20
    jump conditions

label choice2_2:
    $ menu_flag = False
    "The village resents you for keeping these resources, and you lost a few people.  \nGain : happiness {image=arrow_down.png} 10, money {image=arrow_down.png} 5, population {image=arrow_down.png} 10"
    $ money -= 5
    $ happiness -= 10
    $ population -= 10
    jump conditions

###################################################### Event3
label scenario3:
    $ tips = "{b}Tips{/b} : Look carefully at your village's power before fighting ! "
    $ theory_text = "{b}Theory{/b} : War has always shaped history. While they can be destructive to people, investments in technology to gain a technological advantage are of the utmost importance. It is important not to underestimate technology in order to ensure a reputable and powerful economy."
    show screen gameUI
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ counter3 = counter
    $ a = renpy.random.randint(10,100)

    if (world == 0 ):
        $ situation = "A neighboring tribe (power = %d) is attacking the village, what should we do ?" % a
        show screen s
    elif (world == 1) :
        $ situation = "A neighboring castle (power = %d) is attacking the village, what should we do ?" % a 
        show screen s

    menu:
        "Declare war and potentially gain ressources":
            with hpunch
            hide screen gameUI
            hide screen s
            hide screen theory
            hide perso animated
            jump choice3_1
        "Try to negotiate and potentially don’t lose any villagers)":
            hide screen gameUI
            hide screen theory
            hide perso animated
            hide screen s
            jump choice3_2

label choice3_1:
    $ menu_flag = True

    if power>=a :
        if avatar ==1:
            show sprite_attack with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_attack2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "We succeeded in repelling the enemies ! We were able to seize their resources but we lost many fighters and the morale of the village is at its lowest. \n Gain : happiness {image=arrow_down.png} 10, money {image=arrow_up.png} 20, population {image=arrow_down.png} 10, power {image=arrow_up.png} 20"
        $ happiness -=10
        $ money +=20
        $ population -=10
        $ power +=20
        if avatar ==1 :
            hide sprite_attack with leftside
        if avatar == 2 :
            hide sprite_attack2 with leftside

    elif power< a :
        if avatar ==1:
            show sprite_hurt with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_hurt2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "The enemies were stronger than us, the village was almost destroyed… \nGain : happiness {image=arrow_down.png} /2, money {image=arrow_down.png} /2, population {image=arrow_down.png} 10, power {image=arrow_down.png} 10"
        $ happiness = int(happiness /2)
        if money<0 :
            $ money -=5
        else :
            $ money = int (money /2)
        $ population -=10
        $ power =-10
        if avatar ==1 :
            hide sprite_hurt with leftside
        if avatar == 2 :
            hide sprite_hurt2 with leftside

    jump conditions

label choice3_2:
    $ menu_flag = True
    if money + power > 60 :
        if avatar ==1:
            show sprite_happy with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_happy2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        image deal animated = Movie(play="animation_deal.webm", loop=False)
        show deal animated at truecenter
        "An agreement has been reached with the neighboring village. We lost some resources but gained a great ally.\nGain : money {image=arrow_down.png} 10, power {image=arrow_up.png} 40, population {image=arrow_up.png} 10"
        $ money -=10
        $ power +=40
        $ population += 10
        if avatar ==1 :
            hide sprite_happy with leftside
        if avatar == 2 :
            hide sprite_happy2 with leftside

    elif  money + power <= 60 :
        if avatar ==1:
            show sprite_hurt with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_hurt2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "An agreement hasn’t been reached, we are paying a heavy tol, \nGain : money {image=arrow_down.png} /5"
        if money<0 :
            $ money -=5
        else :
            $ money = int (money /5)
        if avatar ==1 :
            hide sprite_hurt with leftside
        if avatar == 2 :
            hide sprite_hurt2 with leftside

    jump conditions

###################################################### Event4
label scenario4:
    $ tips = "{b}Tips{/b} : Look carefully at your village's power before fighting ! "
    show screen gameUI
    $ theory_text = "{b}Theory{/b} : If an economy is said to be open, i.e. if it trades with its neighbours, it will benefit from strong economic spin-offs in times of peace. Goods can be exchanged in an advantageous way between the different countries. However, if one of the two economies suffers a shock, the other will also feel the negative impact."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ counter4 = counter
    $ p = renpy.random.randint(10,100)
    if world == 0 :
        $ situation = "A nearby village is being attacked by raiders !"
    elif world == 1 :
        $ situation = "The neighboring castle is being attacked by raiders !"

    show screen s

    menu:
        "Offer aid and potentially gain allies":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice4_1
        "Ignore":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice4_2

label choice4_1:
    $ menu_flag = True
    if power>=p :
        if avatar ==1:
            show sprite_hurt with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_hurt2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "We succeeded in repelling the enemies ! We lost some fighters but gained a new ally !\nGain : money {image=arrow_up.png} 10, population {image=arrow_down.png} 10, power {image=arrow_up.png} 30"
        $ money += 10
        $ population -=10
        $ power +=30
        if avatar ==1 :
            hide sprite_hurt with leftside
        if avatar == 2 :
            hide sprite_hurt2 with leftside

    elif power< p :
        if avatar ==1:
            show sprite_hurt with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_hurt2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        image fire animated = Movie(play="animation_fire.webm", loop=False)
        show fire animated at truecenter
        "The enemies were stronger than us, the village was almost destroyed… \nGain : happiness {image=arrow_down.png}, money {image=arrow_down.png}, population {image=arrow_down.png} 10, power {image=arrow_down.png}"
        $ happiness = int(happiness/3)
        if money<0 :
            $ money -=5
        else :
            $ money = int (money /3)
        $ population -=10
        $ power = int(power/3)
        if avatar ==1 :
            hide sprite_hurt with leftside
        if avatar == 2 :
            hide sprite_hurt2 with leftside

    jump conditions

label choice4_2:
    $ menu_flag = True
    if avatar ==1:
        show sprite_hurt with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_hurt2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    "You have lost the trust of the people.... \nGain : happiness {image=arrow_down.png} 10"
    $ happiness -=10
    if avatar ==1 :
        hide sprite_hurt with leftside
    if avatar == 2 :
        hide sprite_hurt with leftside
    jump conditions

###################################################### Event5
label scenario5:
    $ tips = "{b}Tips{/b} : If you choose to trust the nomads, you may as well gain power and population but also lose money and happiness in the event of a scam."
    show screen gameUI
    $ counter += 1
    $ situation = "A group of nomads passes through the village, offering to share their knowledge of survival skills in exchange of money."
    show screen s

    menu:
        "Trust the nomads and potentially gain valuable skills":
            hide screen s
            hide screen gameUI
            jump choice5_1
        "Reject their offer and preserve resources":
            hide screen s
            hide screen gameUI
            jump choice5_2

label choice5_1:
    $ a = renpy.random.choice([0,1])
    $ menu_flag = True
    if a==0 :
        if avatar ==1:
            show sprite_happy with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_happy2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "Good choice! You are strengthening your village. \nGain : happiness {image=arrow_up.png} 10, money {image=arrow_down.png} 10, population {image=arrow_up.png} 10, power {image=arrow_up.png} 20"
        $ money -=10
        $ population +=10
        $ happiness +=10
        $ power +=20
        if avatar ==1 :
            hide sprite_happy with leftside
        if avatar == 2 :
            hide sprite_happy2 with leftside

    elif a==1 :
        if avatar ==1:
            show sprite_hurt with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        if avatar == 2 :
            show sprite_hurt2 with leftside :
                xzoom 4  yzoom 4
                xalign 0.95 yalign 0.6
        "The traders were suspicious... \nGain : happiness {image=arrow_down.png} 10, money {image=arrow_down.png} 10"
        $ happiness -= 10
        $ money -= 10
        if avatar ==1 :
            hide sprite_hurt with leftside
        if avatar == 2 :
            hide sprite_hurt2 with leftside

    jump conditions

label choice5_2:
    $ menu_flag = True
    "..."
    jump conditions

###################################################### Events Positifs
label scenario6:
    $ counter += 1
    if avatar ==1:
        show sprite_happy with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_happy2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6

    if (world == 0 ):
        $ situation = "The fishing of the day has been good! You are earning a lot of resources!"
        show screen s
        "Gain : happiness {image=arrow_up.png} 20, money {image=arrow_up.png} 20"
    elif (world == 1 ):
        $ situation = "The hunt of the day has been good! You are earning a lot of resources!"
        show screen s
        "Gain : happiness {image=arrow_up.png} 20, money {image=arrow_up.png} 20"
    $ happiness += 20
    $ money += 20
    if avatar ==1 :
        hide sprite_happy with leftside
    if avatar == 2 :
        hide sprite_happy2 with leftside
    hide screen s
    jump conditions

label scenario7:
    $ counter += 1
    $ situation = "A neighboring village offers an alliance to our village. Some members of the population are suspicious… Do you accept the offer and gain allies, or reject it and potentially preserve happiness ?"
    show screen s

    menu:
        "Sign an alliance.":
            hide screen s
            jump choice7_1
        "Refuse the alliance.":
            hide screen s
            jump choice7_2

label choice7_1:
    $ menu_flag = True
    image deal animated = Movie(play="animation_deal.webm", loop=False)
    show deal animated at truecenter
    "Gain : happiness {image=arrow_down.png} 5, power {image=arrow_up.png} 30"
    $ happiness -=5
    $ power += 30
    jump conditions

label choice7_2:
    $ menu_flag = True
    jump conditions



###################################################### Event8 : The Genius
label scenario8:
    $ tips = "{b}Tips{/b} : Scientific researches can brought in money but needs a first investissement"
    show screen gameUI
    $ theory_text = "{b}Theory{/b} : Römer states that for technical progress, which best pushes an economy upwards, depends among other things on the number of scientists present in an economy. Since there are not enough of them, it is necessary to hire one to improve productivity. If there were already many more, it would not be beneficial to do so. Indeed, the likelihood that they would be looking for the same things and be inefficient by extension would be multiplied."
    $ counter += 1
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    if world ==0 :
        $ situation = "A genius scientist passes by your village and wants to join."
    if world ==1 :
        $ situation = "A genius master mason passes by your castle and wants to join."
    show screen s

    menu:
        "Hire him":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice8_1
        "Ask him to leave.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice8_2

label choice8_1:
    $ menu_flag = True
    $ counter8 = counter
    $ actif8 = True
    image invention animated = Movie(play="animation_invention.webm", loop=False)
    show invention animated at truecenter
    "He was able to create technological advancement but he needed a lot of ressources. \nGain : money {image=arrow_down.png} 10,  happiness {image=arrow_up.png} 10"
    $ money -=10
    $ happiness +=10
    jump conditions

label choice8_2:
    $ menu_flag = True
    "He returned to his home village"
    jump conditions


###################################################### Event9
label scenario9:
    $ tips = "{b}Tips{/b} : An investement can be a success or a failure... Up to you to estimate if you can take the risk !"
    $ theory_text = "{b}Theory{/b} : To increase production, according to Swan and Solow, this is done through better productivity per worker. While there are different methods in the short run, the economy will always return to a stable point, called the equilibrium point. In order to shift this point and thus strengthen an economy in a sustainable and robust manner, technological progress must be maximised as the engine of growth and the reason for shifting this point. "
    show screen gameUI
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ p = renpy.random.randint(10,100)

    if (world == 0 ):
        $ situation = "A new artisanry has become available for purchase. What should we do? "
        show screen s
    elif (world == 1 ):
        $ situation = "A new war machine has become available for purchase. What should we do? "
        show screen s

    menu:
        "Invest in purchasing the technology and potentially increase production or efficiency":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice9_1
        "Do not purchase the technology and save resources for other needs.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice9_2

label choice9_1:
    $ menu_flag = True
    if 80 >= p :
        $ counter9 = counter
        $ actif9 = True
        image invention animated = Movie(play="animation_invention.webm", loop=False)
        show invention animated at truecenter
        "The technology takes time to prosper... \nGain : money {image=arrow_down.png} 20"
        $ money -=20

    else:
        "The research came back without a result \nGain : money {image=arrow_down.png} 10"
        $ money -=10

    jump conditions

label choice9_2:
    $ menu_flag = True
    "You passed on the opportunity"
    jump conditions


###################################################### Event10
label scenario10:
    $ tips = "{b}Tips{/b} : An investement can be a success or a failure... Up to you to estimate if you can take the risk !"
    $ theory_text = "{b}Theory{/b} : The principle of free trade and an open economy is to have multiple suppliers, competing with each other to bring quality products at the lowest prices. However, if an economy forgets this principle of competition and becomes a dependent customer of another economy, in the event of turmoil, crisis or shock, it will be far less resilient than if it had remained autonomous and self-reliant."
    show screen gameUI
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ p = renpy.random.randint(10,100)
    $ situation = "A rival village has become a major player in the region's trade network."
    show screen s

    menu:
        "Invest in developing our own trade network and potentially increase profits.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice10_1
        "Do not invest and save resources for other needs.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice10_2

label choice10_1:
    $ menu_flag = True
    if 60 >= p :
        $ counter10 = counter
        $ actif10 = True
        "The network is successfully built ! \nGain : money {image=arrow_down.png} 20,  happiness {image=arrow_up.png} 10"
        $ money -=20
        $ happiness +=10

    else:
        "You failed to create the network on your own. \nGain : money {image=arrow_down.png} 10"
        $ money -=10

    jump conditions

label choice10_2:
    $ menu_flag = True
    "You have lost an ally"
    $ power -=10
    jump conditions

###################################################### Event11
label scenario11:
    $ tips = "{b}Tips{/b} : The worshop can be a success or a failure... Up to you to estimate if you can take the risk !"
    $ theory_text = "{b}Theory{/b} : To have good technical progress, source of good growth according to Solow, it is necessary to invest not only in research, but also in the implementation of these technologies in companies. It is therefore also necessary to develop the industrial fabric to have the best results and benefit from the advantages of the improved productivity of the workers."
    show screen gameUI
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ situation = "A group of skilled craftsmen has offered to set up a workshop in the village"
    show screen s

    menu:
        "Allow the craftsmen to set up shop and potentially increase the village's production capabilities.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice11_1
        "Reject the offer and potentially miss out on production opportunities.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice11_2

label choice11_1:
    $ menu_flag = True
    if avatar ==1:
        show sprite_happy with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_happy2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    $ counter11 = counter
    $ actif11 = True
    image money animated = Movie(play="animation_gain_money.webm", loop=False)
    show money animated at truecenter
    "The workshop was a great success ! \nGain : happiness {image=arrow_up.png} 10, money {image=arrow_up.png} 20, population {image=arrow_up.png} 10"
    $ money +=20
    $ happiness +=10
    $ population +=10
    if avatar ==1 :
        hide sprite_happy with leftside
    if avatar == 2 :
        hide sprite_happy2 with leftside
    jump conditions

label choice11_2:
    $ menu_flag = True
    if avatar ==1:
        show sprite_hurt with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_hurt2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    "You lost a good opportunity and the people are not satisfied \nGain : happiness {image=arrow_down.png} 10"
    $ happiness -=10
    if avatar ==1 :
        hide sprite_hurt with leftside
    if avatar == 2 :
        hide sprite_hurt2 with leftside
    jump conditions


###################################################### Event12
label scenario12:
    $ tips = "{b}Tips{/b} : Establish this low will make the population unhappy but you will keep all your other ressources. \n If you ignore it, the population of the village will increase and this will cost you a lot of money."
    $ theory_text = "{b}Theory{/b} : In the event of a strong increase in the population, it is necessary to adapt various economic parameters to tend again towards the point of equilibrium, that is to say the optimal status of growth. If the population increases but savings and technological investments are not adapted, the stock of capital per inhabitant will logically decrease, the economy will decline until it returns to a point of equilibrium."
    show screen gameUI
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ situation = "The village's population has grown exponentially, putting a strain on resources."
    show screen s

    menu:
        "Enforce a law forbidding people from having more than 1 child.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice12_1
        "Ignore it and ensure the population's happiness.":
            hide screen s
            hide screen gameUI
            hide screen theory
            hide perso animated
            jump choice12_2

label choice12_1:
    $ menu_flag = True
    "The population growth was reduced but the people are not happy with your decision. \nGain : happiness {image=arrow_down.png} 20, money {image=arrow_up.png} 10"
    $ money +=10
    $ happiness -=20
    jump conditions

label choice12_2:
    $ menu_flag = True
    $ counter12 = counter
    $ actif12 = True
    image population animated = Movie(play="animation_population.webm", loop=False)
    show population animated at truecenter
    "You have gained the love of the people but need to deal with the increase of the population. \nGain : money {image=arrow_down.png} 20, population {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10"
    $ money -=20
    $ population +=10
    $ happiness += 10
    jump conditions


###################################################### Event13
label scenario13:
    $ counter += 1
    $ situation = "A nearby wealthy village offered to buy land from your village."
    show screen s

    menu:
        "Sell the land to make money.":
            hide screen s
            jump choice13_1
        "Reject the offer.":
            hide screen s
            jump choice13_2

label choice13_1:
    $ menu_flag = True
    image deal animated = Movie(play="animation_deal.webm", loop=False)
    show deal animated at truecenter
    "You have formed an alliance and got money but lost power on such lands. \nGain : power {image=arrow_down.png} 10, money {image=arrow_up.png} 10"
    $ money +=10
    $ power -=10
    jump conditions

label choice13_2:
    $ menu_flag = True
    "You rejected the land and held you kingdome steady"
    jump conditions


###################################################### Event14
label scenario14:
    $ counter += 1
    $ theory_text = "{b}Theory{/b} : To have good technical progress, source of good growth according to Solow, it is necessary to invest not only in research, but also in the implementation of these technologies in companies. It is therefore also necessary to develop the industrial fabric to have the best results and benefit from the advantages of the improved productivity of the workers."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "The village's education system is outdated and causing a skills gap in the workforce. What should we do?"
    show screen s

    menu:
        "Invest in upgrading the education system and potentially increase economic efficiency.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice14_1
        "Ignore the problem.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice14_2

label choice14_1:
    $ menu_flag = True
    $ counter14 = counter
    $ actif14 = True
    "You have upgraded your educational system and thus securing a future for the new generation.  \nGain : power {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10, money {image=arrow_down.png} 10"
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
    $ counter += 1
    $ counter15 = counter
    $ actif15 = True
    $ theory_text = "{b}Theory{/b} : Using our own resources to help another economy can seem like a hole in our budget. However, with our open economy, it is important to restore free trade as soon as possible. A natural disaster causes a reduction in the stock of capital: it is necessary to repair the destroyed infrastructures. The sooner we help them, the sooner we can regain our pre-disaster economy."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "A neighboring village is experiencing a natural disaster and needs aid. What should we do?"
    show screen s

    menu:
        "Provide aid to the neighboring village and potentially gain allies and power.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice15_1
        "Ignore the situation and potentially damage relations with the neighboring village.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice15_2

label choice15_1:
    $ positif15 = True
    image deal animated = Movie(play="animation_deal.webm", loop=False)
    show deal animated at truecenter
    "You gain a new ally !"
    #Rep: -money (now) ++power (++ 2 tour) ++happiness (+ 1 tour ++ 2 tour)
    jump conditions

label choice15_2:
    $ negatif15 = True
    "..."
    #Rep: -power (- 1 tour) -happiness (- 1 tour)
    jump conditions


###################################################### Event16
label scenario16:
    $ tips = "{b}Tips{/b} : I hope that you have enough money to invest in this event or it will be disastrous..."
    show screen gameUI
    $ theory_text = "{b}Theory{/b} : For capital, and therefore wealth, to increase, it must be ensured that it can be distributed, moved and allocated in the most effective and efficient way possible. Good infrastructure is the heart of these logistics operations necessary for any continued growth. If we neglect these expenses, they are more and more heavy and will be more and more difficult to reimburse, because the economy will be slower and the sum necessary to revive it higher."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ counter16 = counter
    $ actif16 = True
    $ situation = "The village's infrastructure, such as roads and buildings, are in need of repair. What should we do?"
    show screen s

    menu:
        "Invest in repairing the infrastructure and potentially improve efficiency.":
            if money >= 20 :
                hide screen gameUI
                hide screen s
                hide screen theory
                hide perso animated
                jump choice16_1
            else :
                hide screen gameUI
                hide screen theory
                hide perso animated
                hide screen s
                jump no_money
        "Ignore the problem and potentially risk safety and efficiency but save money.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice16_2

label choice16_1:
    "You invest in the infrastructure. \nGain : money {image=arrow_down.png} 20"
    $ money -= 20
    #Rep: - money (now) + power (+ 1 tour) + happiness (+ 1 tour)
    $ positif16 = True
    jump conditions

label choice16_2:
    $ population -= 10
    "You lost some people... \nGain : population {image=arrow_down.png} 10"
    #Rep: -power (- 1 tour - - 2 tour) - happiness (- 1 tour - - 2 tour)
    $ negatif16 = True
    jump conditions

###################################################### Event17
label scenario17:
    $ p = renpy.random.randint(10,100)
    $ counter += 1
    $ theory_text = "{b}Theory{/b} : Adopting a technology can be a risky bet on the future. But if the economy is well structured, with a good composition: good number of qualified workers and scientists, necessary investments in technical progress, investments for the well-being of the population... then the risks are minimum and the advantages collected through technology improves everyone's life."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "A new crop has been introduced to the region which can potentially bring in more profits."
    show screen s

    menu:
        "Invest in testing and cultivating the new crop and potentially increase money.":
            if money >= 20 :
                hide screen s
                hide screen theory
                hide perso animated
                jump choice17_1
            else :
                hide screen s
                hide screen theory
                hide perso animated
                jump no_money
        "Ignore the new crop and continue with current production.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice17_2


label choice17_1:
    $ money -= 20
    "You made an investisement! \nGain : money {image=arrow_down.png} 20"
    if p < 95 :
        $ counter17 = counter
        $ actif17 = True
    #Rep: - money (now) ++money (++ 2 tour +++ 5 tour) (maybe! P = 95%)
    jump conditions

label choice17_2:
    #Rep: no changes
    jump conditions

###################################################### Event18
label scenario18:
    $ situation = "The village elders propose investing in science and technology to improve the quality of life in the village, but it requires a significant amount of resources. What should we do ?"
    $ counter += 1
    $ theory_text = "{b}Theory{/b} : According to Keynes, technical progress is the only sustainable vector of growth, thus improving the standard of living, the ease of living and the comfort and economic power of a country. Sustained investment is good for the village, because the money invested will be largely repaid by improved productivity and quality."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    show screen s
    menu:
        "Invest heavily in science and technology research and development.":
            if money >= 20 :
                hide screen s
                hide screen theory
                hide perso animated
                jump choice18_1
            else :
                hide screen s
                hide screen theory
                hide perso animated
                jump no_money
        "Save resources for other pressing needs.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice18_2

label choice18_1:
    $ counter18 = counter
    $ actif18 = True
    # Rep: ++happiness ++power (2 tours)
    $ menu_flag = True
    "Gain : money {image=arrow_down.png} :20"
    $ money -=20
    jump conditions

label choice18_2:
    $ menu_flag = True
    if avatar ==1:
        show sprite_hurt with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_hurt2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    "The villagers become frustrated with the lack of progress and innovation. \nGain : happiness {image=arrow_down.png} 10"
    $ happiness -=10
    if avatar ==1 :
        hide sprite_hurt with leftside
    if avatar == 2 :
        hide sprite_hurt2 with leftside
    jump conditions

###################################################### Event19
label scenario19:
    $ counter += 1
    $ counter19 = counter
    $ actif19 = True
    $ theory_text = "{b}Theory{/b} : According to Römer and his economic model, the economic situation can be improved if investments in education and knowledge sharing are made. However, if too many people are working on new ideas, they risk working on the same subjects without knowing it and end up wasting their time. It is therefore necessary to optimise these investments so that they do not lend themselves to other sectors, while not ignoring them."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "Your village having expanded a lot, do you want to invest in new schools?"
    show screen s

    menu:
        "Invest heavily in education by building schools and hiring qualified teachers, despite the high costs.":
            if money >= 20 :
                hide screen s
                hide screen theory
                hide perso animated
                jump choice19_1
            else :
                hide screen s
                hide screen theory
                hide perso animated
                jump no_money
            
        "Invest minimally in education, citing the high costs and the need to prioritize other pressing needs. ":
            hide screen s
            hide screen theory
            hide perso animated
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
    $ tips = "{b}Tips{/b} : The more you invest, the better the reward but the higher the risk is."
    show screen gameUI
    $ theory_text = "{b}Theory{/b} : For technical progress to combine effectively with the happiness of the population, it is necessary to invest equally. If the needs of the population are not addressed, technical progress will not be able to flow equally through the different strata of the population."
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ counter += 1
    $ counter20 = counter
    $ actif20 = True
    $ situation = "A technological breakthrough presents the opportunity to increase the village’s wealth and resources, but some members of the population are concerned about the ethical implications of the technology and the player must decide whether to pursue it or not."
    show screen s

    menu:
        "Make a significant investment in science research and development, despite the high costs.":
            if money >= 30 :
                hide screen gameUI
                hide screen theory
                hide perso animated
                hide screen s
                jump choice20_1
            else :
                hide screen s
                hide screen gameUI
                hide screen theory
                hide perso animated
                jump no_money
        "Make a moderate investment in science research and development, balancing the need for progress with fiscal responsibility.":
            if money >= 20 :
                hide screen s
                hide screen gameUI
                hide screen theory
                hide perso animated
                jump choice20_2
            else :
                hide screen s
                hide screen gameUI
                hide screen theory
                hide perso animated
                jump no_money
        "Make a minimal investment in science research and development, citing the high costs and the need to prioritize other pressing needs." :
            if money >= 10 :
                hide screen s
                hide screen gameUI
                hide screen theory
                hide perso animated
                jump choice20_3
            else :
                hide screen s
                hide screen gameUI
                hide screen theory
                hide perso animated
                jump no_money

label choice20_1:
    $ choice20_1 = True
    # Rep : +++happiness, +++power (2tours)
    $ menu_flag = True
    " Gain : money {image=arrow_down.png} 30"
    $ money -=30
    jump conditions

label choice20_2:
    $ choice20_2 = True
    # Rep : ++happiness, ++power (2tours)
    "Gain : money {image=arrow_down.png} 20"
    $ money -=20
    jump conditions

label choice20_3:
    $ hoice20_3 = True
    # Rep : -happiness, +power (2tours)
    $ menu_flag = True
    "Gain : money {image=arrow_down.png} 10"
    $ money -=10
    jump conditions


###################################################### Events negatifs
label scenario21:
    if avatar ==1:
        show sprite_hurt with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_hurt2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    image virus animated = Movie(play="animation_virus.webm", loop=False)
    show virus animated at truecenter
    $ situation = "A disease outbreak is spreading in the village causing some villagers to become ill."
    show screen s
    $ happiness -= 5
    $ money -= 5
    $ population -= 10
    "Gain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 5, population {image=arrow_down.png} 10"
    if avatar ==1 :
        hide sprite_hurt with leftside
    if avatar == 2 :
        hide sprite_hurt2 with leftside
    hide screen s
    jump conditions

label scenario22:
    if avatar ==1:
        show sprite_hurt with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if avatar == 2 :
        show sprite_hurt2 with leftside :
            xzoom 4  yzoom 4
            xalign 0.95 yalign 0.6
    if world == 0 :
        $ situation = " A severe cold snap has hit the region, causing crops to fail and leaving the village without food."
        show screen s
    elif world == 1 :
        $ situation = " A severe drought has hit the region, causing crops to fail and leaving the village without food."
        show screen s
    "Gain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 10, population {image=arrow_down.png} 5"
    $ happiness -= 5
    $ money -= 10
    $ population -= 5
    if avatar ==1 :
        hide sprite_hurt with leftside
    if avatar == 2 :
        hide sprite_hurt2 with leftside
    hide screen s
    jump conditions

label scenario23:
    $ theory_text = "{b}Theory{/b} : A sudden increase in population can increase impoverishment. Indeed, if there is a finite amount of workplaces and there are more workers, they will have less bargaining power than the bosses, who will take advantage of this to lower wages. However, if you are wise and control this power, integrate new infrastructure and promote economic development, this workforce will be useful and the economy will be stronger."
    $ counter += 1
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "A group of refugees arrive in the village seeking shelter."
    show screen s

    menu:
        "Accept them and potentially gain allies.":
            hide screen s
            hide screen theory
            hide perso animated
            hide perso animated
            jump choice23_1
        "Reject them and potentially preserve resources.":
            hide screen s
            hide screen theory
            hide perso animated
            hide perso animated
            jump choice23_2

label choice23_1:
    $ menu_flag = True
    image population animated = Movie(play="animation_population.webm", loop=False)
    show population animated at truecenter
    "Your population and needs increase ! \nGain : population {image=arrow_up.png} 10, money {image=arrow_down.png} 10,  power {image=arrow_up.png} 10 "
    $ money -=10
    $ population +=10
    $ power += 10
    jump conditions

label choice23_2:
    $ menu_flag = True
    "No changes in ressources"
    jump conditions


label scenario24:
    $ theory_text = "{b}Theory{/b} : If an economy is dependent on trade, it is exposed to a higher contagion to external crises. It loses autonomy, but gains wealth in peacetime. This wealth can be accumulated, invested and saved to prevent a future crisis."
    $ counter += 1
    show screen theory
    show perso animated :
        xzoom 2  yzoom 2
        xalign 0.1 yalign 1.0
    $ situation = "A band of bandits is terrorizing the village’s trade routes !"
    show screen s

    menu:
        "Invest money to restore routes.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice24_1
        "Preserve money.":
            hide screen s
            hide screen theory
            hide perso animated
            jump choice24_2

label choice24_1:
    $ menu_flag = True
    $ counter24 = counter
    $ actif24 = True
    "The village's trage route is safe now ! \nGain : happiness {image=arrow_up.png} 10, money {image=arrow_down.png} 5"
    $ money -=5
    $ happiness +=10
    jump conditions

label choice24_2:
    $ menu_flag = True
    "Your economy has dropped dramatically... \nGain : happiness {image=arrow_down.png} 5, money {image=arrow_down.png} 20"
    $ money -= 20
    $ happiness +-5
    jump conditions



label conditions: 
    hide text

    if actif8== True :
        if (counter )== (counter8+1) :
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Scientific research has brought in money! \nGain : money {image=arrow_up.png} 10"
            $ money += 10  
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

        if (counter) == (counter8+2):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Scientific research has brought in money! \nGain : money {image=arrow_up.png} 20, happiness {image=arrow_up.png} 10"
            $ money += 20
            $ happiness += 10 
            $ actif8 = False
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

    if actif9== True :
        if (counter)== (counter9 +1) :
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Our investment in research is paying off! \nGain : money {image=arrow_up.png} 10"
            $ money += 10 
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside
        if (counter) == (counter9 +2):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Our investment in research is paying off! \nGain : money {image=arrow_up.png} 20"
            $ money += 20
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside
        if (counter) == (counter9 +3):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Our investment in research is paying off! \nGain : money {image=arrow_up.png} 20"
            $ money += 20
            $ actif9 = False
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

    if actif10== True :
        if (counter)== (counter10 +1) :
            "Investing in the development of our own trade network has resulted in significant profits and made our village a major player in the regional trade network. \n Gain : money {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
            $ power += 10 
            $ population += 10
        if (counter) == (counter10 +3):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Investing in the development of our own trade network has resulted in significant profits and made our village a major player in the regional trade network. \n Gain : money {image=arrow_up.png} 20"
            $ money += 20
            $ actif10 = False
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

    if actif11== True :
        if (counter )== (counter11+1) :
            "After allowing the craftsmen to set up shop, the village's production capabilities have greatly increased ! \n Gain : money {image=arrow_up.png} 10 "
            $ money += 10 
        if (counter) == (counter11 +2):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "After allowing the craftsmen to set up shop, the village's production capabilities have greatly increased ! \n Gain : happiness {image=arrow_up.png} 10 "
            $ happiness += 10
            $ actif11 = False
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside
  
    if actif12== True :
        if (counter )== (counter12+1) :
            "The population is growing... \nGain : money {image=arrow_down.png} 10, population {image=arrow_up.png} 10"
            $ population += 10 
            $ money -= 10 
        if (counter) == (counter12 +2):
            "The population is growing... \nGain : money {image=arrow_down.png} 10, population {image=arrow_up.png} 10"
            $ population += 10
            $ money -= 10 
        if (counter) == (counter12 +3):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "The population is expending... \nGain : money {image=arrow_down.png} 10, population {image=arrow_up.png} 10"
            $ population += 10
            $ money -= 10 
            $ actif12 = False
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

    if actif14== True :
        if (counter )== (counter14 +1) :
            "Your investment in schools is paying off! \nGain : money {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
            $ power += 10 
            $ happiness += 10 
            $ population += 10
            $ money += 10
        if (counter) == (counter14 +3):
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Your investment in schools is paying off! \nGain : money {image=arrow_up.png} 10"
            $ money += 10
            $ actif14 = False
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

    if actif15== True :
        if counter == (counter15 + 1) and (positif15 == True):
            "Your alliance with the neighboring village is increasing the power of the village! \nGain : power {image=arrow_up.png} 20, happiness {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
            $ power += 20
            $ happiness += 10
            $ population += 10
        if counter == (counter15 + 1) and (negatif15 == True):
            if avatar ==1:
                show sprite_hurt with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_hurt2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Your bad relationship with the neighboring village is weakening you... \nGain : power {image=arrow_down.png} 10, happiness {image=arrow_down.png} 10"
            $ power -= 10
            $ happiness -= 10
            if avatar ==1 :
                hide sprite_hurt with leftside
            if avatar == 2 :
                hide sprite_hurt2 with leftside
        $ actif15 = False

    if actif16== True :
        if counter == (counter16+1) and (positif16 == True):
            "After investing in repairing the infrastructure, the efficiency of the village has significantly improved, resulting in faster production times. \nGain : power {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10"
            $ power += 10
            $ happiness += 10
            $ actif16 = False
        if counter == (counter16+1) and (negatif16 == True):
            "Ignoring the problem of the village's deteriorating infrastructure risk safety and efficiency... You would have been better off keeping some money aside for essential needs. \nGain : power {image=arrow_down.png} 10, happiness {image=arrow_down.png} 10"
            $ power -= 10
            $ happiness -= 10
        if counter > (counter16 + 2) and (negatif16 == True):
            if avatar ==1:
                show sprite_hurt with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_hurt2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Ignoring the problem of the village's deteriorating infrastructure risk safety and efficiency... You should have kept some money for essential needs. \nGain : power {image=arrow_down.png} 20, happiness {image=arrow_down.png} 20"
            $ power -= 20
            $ happiness -= 20
            $ actif16 = False
            if avatar ==1 :
                hide sprite_hurt with leftside
            if avatar == 2 :
                hide sprite_hurt2 with leftside

    if actif17== True :
        if counter == (counter17+1):
            "The crops yield profits ! \nGain : money {image=arrow_up.png} 20"
            $ money += 20
            $ actif17 = False

    if actif18== True :
        if counter == (counter18 + 2):
            "The investment in science pays off in the long term with the development of new tools and technologies that improve the lives of the villagers. The villagers appreciate the forward thinking and become more innovative and productive. \nGain : power {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
            $ power += 10
            $ happiness += 10
            $ population += 10
            $ actif18 = False

    if actif19== True : 
        if counter == (counter19 + 2) and (positif19 == True):
            "The investment in education pays off in the long term as the children become more educated, literate, and numerate. The village becomes known for its educated population, which attracts new businesses and opportunities. \nGain : power {image=arrow_up.png} 10, money {image=arrow_up.png} 10, happiness {image=arrow_up.png} 10, population {image=arrow_up.png} 10"
            $ power += 10
            $ happiness += 10   
            $ money += 10
            $ population += 10
            $ actif19 = False
        if counter == (counter19 + 2) and (negatif19 == True):
            if avatar ==1:
                show sprite_hurt with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_hurt2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "The village falls behind other communities in terms of progress and development, and the villagers become frustrated with the lack of education opportunities. The younger generation may seek to leave the village for better education opportunities elsewhere, leading to a brain drain and further hindering the development of the village.\nGain : population {image=arrow_down.png} 10, happiness {image=arrow_down.png} 10"
            $ happiness -= 10
            $ population -= 10
            $ actif19 = False
            if avatar ==1 :
                hide sprite_hurt with leftside
            if avatar == 2 :
                hide sprite_hurt2 with leftside

    if actif20== True : 
        if counter == (counter20 + 2) and (choice20_1 == True):
            "The investment in science research and development pays off in the long term as the village ! New industries emerge, providing jobs and improving the overall economic outlook of the village. \nGain : power {image=arrow_up.png} 30, happiness {image=arrow_up.png} 30"
            $ happiness += 20
            $ power += 30
            $ actif20 = False
            hide character
        if counter == (counter20 + 2) and (choice20_2 == True):
            "The investment in science research and development pays off in the long term as the village ! New industries emerge, providing jobs and improving the overall economic outlook of the village. \nGain : power {image=arrow_up.png} 20, happiness {image=arrow_up.png} 20"
            $ happiness += 20
            $ power += 20
            $ actif20 = False
        if counter == (counter20 + 2) and (choice20_3 == True):
            "The lack of investment in science research and development means the village falls behind other communities in terms of progress and development.  \nGain : population {image=arrow_down.png} 10, happiness {image=arrow_down.png} 10"
            $ happiness -= 10
            $ population -= 10
            $ actif20 = False

    if actif24== True :
        if (counter )== (counter24+1) :
            if avatar ==1:
                show sprite_happy with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            if avatar == 2 :
                show sprite_happy2 with leftside :
                    xzoom 4  yzoom 4
                    xalign 0.95 yalign 0.6
            "Trade has brought in money! \nGain : money {image=arrow_up.png} 10"
            $ money += 10  
            if avatar ==1 :
                hide sprite_happy with leftside
            if avatar == 2 :
                hide sprite_happy2 with leftside

    jump choice_done