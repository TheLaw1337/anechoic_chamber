# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define h_intro = Character('', color="#c8ffc8", size=24)

#images
init:
    image bg black = "#000000"


# The game starts here.


label start:

    scene bg black

    centered "{size=48}Hello, friend{/size}"
    

    hide text
    with Pause(1)

    centered "{size=36}It's good to see you.{/size}"

    hide text
    with Pause(1)

    return
