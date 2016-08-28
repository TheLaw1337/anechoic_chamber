# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character('', color="#c8ffc8")
define l = Character('Lucas', color="#FF0000")
#images
init:
    image bg black = "#000000"
    image bg room = "room.jpg"
    image bg news = "news3.jpg"
    image bg factory1 = "album1.jpg"
    image columns = "columns2.png"
    image bg factory2 = "factory2.jpg"
    image bg park = "park.png"

# The game starts here.


label start:

    scene bg black

    centered "{size=24}{cps=10}This story happened some time ago...{/cps}{/size}" with fade
    

    hide text with fade

    scene bg room with fade

    n "Lucas came back home..."
    l "Home, sweet home."
    n "...sat in a chair...{p=1.0}...and turned on computer."

    scene bg news with dissolve 
    with Pause(1)

    l "What the..."
    l "\"Speakers factory will be demolished\"{p=1.0}\"12 years after shutting down Silton speakers factory, townhall decided to deconstruct all its buildings.\""
    
    scene bg factory1 with dissolve
    l "My dad have been working in Silton...{p=1.0}...because of love to sounds and music. He was true audiophile."
    
    show columns with dissolve

    l "Silton's column speakers were everywhere in country, part of products had been exported over entire world. world."

    scene bg factory2 with dissolve

    l "Without factory my city became less prosperous."

    scene bg room with dissolve

    l "I need some fresh air, I'll go for a walk."

    scene bg park with dissolve

    l "The park has a long alley. Along the alley flows a little river."


return