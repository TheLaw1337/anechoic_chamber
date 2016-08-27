# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define h = Character('', color="#c8ffc8")

#images
init:
    image bg black = "#000000"


# The game starts here.


label start:

    scene bg black

    show text "Witaj, przyjacielu..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)


    return
