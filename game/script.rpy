# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character('', color="#c8ffc8")
define l = Character('Lucas', color="#FF0000")
define w = Character('Watchman', color="#eee62d")
#images and other
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
    image bg fact_room1 = "fact_room1.jpg"
    image bg terrain2 = "terrain2.jpg"
    image bg rubbish = "rubbish.jpg"
    image bg canal = "canal.jpg"
    image bg brick = "brick.jpg"
    image bg cables = "cables.jpg"
    image bg electroplating = "electroplating.jpg"
    image bg entrance = "entrance.jpg"
    image bg floor = "floor.jpg"
    image bg book = "book.jpg"
    image bg chamber = "chamber.jpg"


    $ flash = Fade(.25, 0, .75, color="#fff")

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

    l "Hm...Coraz mniej tego zostało.{p=1.0}I'll look around. Maybe I'll shot few photos?"  #nie wiem jak to pierwsze przetłumaczyć

    scene bg black with fade

    play music "footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg private with dissolve

    n "PRIVATE PROPERTY - NO TRESSPASSING" 

    l "Fuck this..."

    scene bg fact_room1 with dissolve

    l "Hm...{p=1.0}Nothing here."

    scene bg terrain2 with dissolve

    l "Hobos were here..." #chodzi mi o żuli

    play music "camerashot.wav" noloop

    scene bg terrain2 with flash

    $ renpy.pause(1)

    scene bg rubbish with dissolve

    l "Rubbish, rubbish, rubbish." #zdjęcie dołu ze śmieciami

    play music "camerashot.wav" noloop

    scene bg rubbish with flash

    $ renpy.pause(1)

    scene bg canal with dissolve

    l "So close...{p=1.0}I need to be careful."

    scene bg brick with dissolve

    l "Yet, another one of many bricks here."

    play music "camerashot.wav" noloop

    scene bg brick with flash

    $ renpy.pause(1)

    scene bg cables with dissolve

    l "Cables from factory's bloodstream."

    play music "camerashot.wav" noloop

    scene bg cables with flash

    $ renpy.pause(1)

    scene bg electroplating with dissolve

    l "This place was electroplating factory." #galwanizernia, przynajmniej tak powiedział Wujek Google :D

    play music "camerashot.wav" noloop

    scene bg electroplating with flash

    $ renpy.pause(1)

    scene bg entrance with dissolve

    l "Hm...{p=1.0}"

    play music "footsteps.wav" noloop

    $ renpy.pause(1.5)

    scene bg floor with dissolve

    l "Maybe here will be something interesting..."

    scene bg book with dissolve

    l "That's been a good photo..."

    play music "camerashot.wav" noloop

    scene bg book with flash

    $ renpy.pause(1)

    l "Done." 

    play music "footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg entrance with dissolve

    w "Hey, you! Get fuckin' out!!!"

    l "SHIT!{p=1.0}Maybe I'll continue next time..."

    scene bg black with fade

    play music "footsteps.wav" noloop

    $ renpy.pause(3)

    centered "{size=36}{cps=10}Few days later...{/cps}{/size}"

    hide text with fade

    scene bg leak with dissolve

    l "Here we go again..."

    scene bg black with fade

    play music "wire.wav" noloop

    $ renpy.pause(2)

    play music "footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg chamber with dissolve

    l "Wow! Anechoic Chamber! To o niej tyle mi opowiadał tata..." # anechoic chamber - komora bezechowa
    l "Służyła ona do testowania kolumn - pomiary elektroakustyczne etc."
    l "Podobno tak dobrze tłumi dźwięki z zewnątrz, że można usłyszeć bicie swojego serca..."
    l "...ale od dłuższego pobytu w niej dostaje się halucynacji."

    l "Well, check it out!"

    scene bg black with fade

    play music "chamber_door.mp3" noloop

    $ renpy.pause(6)

    scene bg book with dissolve

    l "TODO"



return