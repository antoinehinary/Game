# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define player1 = Character("Player 1")
define player2 = Character("Player 2")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg room
    show first :
        zoom 1.5


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show player1 :
        xalign 0.75
        yalign 1.0
 
    # These display lines of dialogue.
    player1 "I've created a new Ren'Py game."


    hide player1

    show player2:
    

    # These display lines of dialogue.
    player2 "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
