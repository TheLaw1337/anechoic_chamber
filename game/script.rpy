# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character('Narrator', color="#c8ffc8")
define l = Character('Lucas', color="#FF0000")
#images
init:
    image bg black = "#000000"
    image bg room = "room.jpg"
    image bg news = "news3.jpg"


# The game starts here.


label start:

    scene bg black

    centered "{size=24}That's story happened some time ago...{/size}" with fade
    

    hide text with fade

    scene bg room with fade

    n "Lucas returned home..."
    l "Home sweet home."
    n "...sitted on the desk...{p=1.0}...and switched on computer."

    scene bg news with fade

    l "What the..."
    


return