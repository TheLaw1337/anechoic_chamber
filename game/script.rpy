# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define h = Character('', color="#c8ffc8")

#images
init:
    image bg black = "#000000"
    image bg room = "room.jpg"


# The game starts here.


label start:

    scene bg black

    centered "{size=24}That's story happened some time ago...{/size}" with fade
    

    hide text with fade

    scene bg room with fade

    h "Home sweet home"
    


return