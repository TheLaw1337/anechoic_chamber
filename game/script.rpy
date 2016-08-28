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
    image bg factory1 = "album1.jpg"
    image columns = "columns2.png"
    image bg factory2 = "factory2.jpg"

# The game starts here.


label start:

    scene bg black

    centered "{size=24}{cps=10}That's story happened some time ago...{/cps}{/size}" with fade
    

    hide text with fade

    scene bg room with fade

    n "Lucas returned home..."
    l "Home sweet home."
    n "...sitted on the desk...{p=1.0}...and switched on computer."

    scene bg news with dissolve 
    with Pause(1)

    l "What the..."
    l "\"Speakers factory will be demolished\"{p=1.0}\"12 years after shut down the speakers factory Silton, government of city has decided to allow deconstruction of factory's buildings.\""
    
    scene bg factory1 with dissolve
    l "My dad worked in Silton...{p=1.0}...from love to sounds and music."
    
    show columns with dissolve

    l "Silton's column speakers were everywhere in country, part of products was exported to whole world."

    scene bg factory2 with dissolve

    l "Without factory my city become less prosperous."


return