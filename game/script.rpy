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
    image bg leak = "leak.jpg"
    image bg graffiti = "graffiti.jpg"
    image bg terrain = "terrain.jpg"
    image bg private = "private_terrain.jpg"

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

    n "The park has a long alley. Along the alley flows a little river.{p=1.0}Summer will end soon."

    scene bg graffiti with dissolve
    
    l "Ehh, that local art..."

    scene bg park with dissolve

    n "And then..." 

    scene bg leak with dissolve

    l "Hm...very interesting...{p=2.0}Maybe I'll go inside?{p=2.0}YOLO!!!"

    
    scene bg black with fade

    play music "wire.wav" noloop

    $ renpy.pause(2)

    scene bg terrain with dissolve

    l "Hm...Coraz mniej tego zostało.{p=1.0}I'll look around."  #nie wiem jak to pierwsze przetłumaczyć

    scene bg black with fade

    play music "footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg private with dissolve

    n "PRIVATE PROPERTY - NO TRESSPASSING" 

    l "Fuck this..."
return