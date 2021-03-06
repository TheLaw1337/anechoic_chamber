﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character('', color="#c8ffc8")
define l = Character('Lucas', color="#FF0000")
define w = Character('Watchman', color="#eee62d")
define g = Character('???', color="#99ccff")
define p = Character('Philoson', color="#99ccff")
#images and other


init:
    image bg black = "#000000"
    image bg title = "title.png"
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
    image bg beers = "beers.jpg"
    image bg chamber_inside = "chamber_inside.jpg"
    image bg chamber_ruin = "chamber_ruin.jpg"
    image bg chamber_fire = "chamber_fire.jpg"
    image bg chamber_fire_run1 = "chamber_fire_run1.jpg"
    image bg chamber_fire_run2 = "chamber_fire_run2.jpg" 
    image bg chamber_fire_run3 = "chamber_fire_run3.jpg"
    image bg chamber_fire_run4 = "chamber_fire_run4.jpg"

    $ x1 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.2)
    $ x2 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.4)
    $ x3 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.6)
    $ x4 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.8)

    $ c1 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.6)
    $ c2 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.7)
    $ c3 = Position(xanchor = 0.5, xpos = 0.5, yalign = 0.8)


    $ flash = Fade(.25, 0, .75, color="#fff")
    $ fade_end = Dissolve(5)
    

# The game starts here.


label start:

    scene bg black

    centered "{size=24}{cps=10}This story happened some time ago...{/cps}{/size}" with fade
    

    hide text with fade

    play music "./sounds/door.wav" noloop

    scene bg room with fade

    n "Lucas came back home..."
    l "Home, sweet home."
    n "...sat in a chair...{p=1.0}...and turned computer on."

    scene bg news with dissolve 
    with Pause(1)

    l "What the..."
    l "\"Speakers factory will be demolished\"{p=1.0}\"12 years after shutting down Silton speakers factory, townhall decided to deconstruct all its buildings.\""
    
    scene bg factory1 with dissolve
    l "My dad has been working in Silton...{p=1.0}...because of love to sounds and music. He was a true audiophile."
    
    show columns with dissolve

    l "Silton's column speakers were everywhere in the country, part of products has been exported over the entire world."

    scene bg factory2 with dissolve

    l "Without factory my city became less prosperous."

    scene bg room with dissolve

    l "I need some fresh air, I'll go for a walk."

    play music "./sounds/door.wav" noloop

    scene bg park with fade

    play music "./sounds/park.wav"

    n "The park has a long alley. Along the alley flows a little river.{p=1.0}Summer will end soon."

    scene bg graffiti with dissolve
    
    l "Ehh, that local art..."

    scene bg park with dissolve

    n "And then..." 

    scene bg leak with dissolve

    l "Hm...very interesting...{p=2.0}Maybe I'll go inside?{p=2.0}YOLO!!!"

    
    scene bg black with fade

    play sound "./sounds/wire.wav" noloop

    $ renpy.pause(2)

    scene bg terrain with dissolve

    l "Hm...There is not much left.{p=1.0}I'll look around. Maybe I'll shoot a few photos?"

    scene bg black with fade

    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg private with dissolve

    n "PRIVATE PROPERTY - NO TRESSPASSING" 

    l "Fuck this..."

    scene bg fact_room1 with dissolve

    l "Hm...{p=1.0}Nothing here."

    scene bg terrain2 with dissolve

    l "Hobos were here..." #chodzi mi o żuli

    play sound "./sounds/camerashot.wav" noloop

    scene bg terrain2 with flash

    $ renpy.pause(1)

    scene bg rubbish with dissolve

    l "Rubbish, rubbish, rubbish." #zdjęcie dołu ze śmieciami

    play sound "./sounds/camerashot.wav" noloop

    scene bg rubbish with flash

    $ renpy.pause(1)

    scene bg canal with dissolve

    l "So close...{p=1.0}I need to be careful."

    scene bg brick with dissolve

    l "Yet another one of many bricks here."

    play sound "./sounds/camerashot.wav" noloop

    scene bg brick with flash

    $ renpy.pause(1)

    scene bg cables with dissolve

    l "Cables from factory's bloodstream."

    play sound "./sounds/camerashot.wav" noloop

    scene bg cables with flash

    $ renpy.pause(1)

    scene bg electroplating with dissolve

    l "This place was electroplating factory." #galwanizernia, przynajmniej tak powiedział Wujek Google :D

    play sound "./sounds/camerashot.wav" noloop

    scene bg electroplating with flash

    $ renpy.pause(1)

    scene bg entrance with dissolve

    l "Hm...{p=1.0}"

    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(1.5)

    scene bg floor with dissolve

    l "Maybe here will be something interesting..."

    scene bg beers with dissolve

    l "Another trace of hobos..." #kolejny ślad po żulach (butelki po piwie)

    play sound "./sounds/camerashot.wav" noloop

    scene bg beers with flash

    $ renpy.pause(1)

    scene bg book with dissolve

    l "That's been a good photo..."

    play sound "./sounds/camerashot.wav" noloop

    scene bg book with flash

    $ renpy.pause(1)

    l "Done." 

    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg entrance with dissolve

    w "Hey, you! Get the fuck out!!!"

    l "SHIT!{p=1.0}Maybe I'll continue next time..."

    scene bg black with fade

    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(3)

    centered "{size=36}{cps=10}Few days later...{/cps}{/size}"

    hide text with fade

    scene bg leak with dissolve

    l "Here we go again..."

    scene bg black with fade

    play sound "./sounds/wire.wav" noloop

    $ renpy.pause(2)

    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(3)

    scene bg chamber with dissolve

    l "Wow! Anechoic Chamber! That's what my dad's stories where about..." # anechoic chamber - komora bezechowa
    l "It was used to test speakers - electroacoustic measurements etc."
    l "it is said to dampen sounds so well that you can hear your heartbeat..."
    l "...but after some time it can cause hallucinations."

    l "Well, check it out!"

    scene bg black with fade

    stop music fadeout 1.0

    play sound "./sounds/chamber_door.mp3" noloop

    $ renpy.pause(6)

    scene bg chamber_inside with dissolve

    play music "./sounds/heartbeat.wav" loop

    l "WOW! That's true!"
    l "My dream is coming real..."

    n "Lucas listened to his heartbeat..."

    stop music fadeout(2)
    $ renpy.music.play("./sounds/attackpad.mp3",loop=True,fadeout=1.0,fadein=1.0) 

    $ renpy.pause(3)

    l "What the..."

    n "Suddenly a weird sounds started surrounding Lucas..." #nagle Lucasa zaczęły otaczać dziwne dźwięki

    n "By some miracle for Lucas these waves sounds like human voice..."

    g "Do you hear me?"

    l "{cps=2}...{/cps}Yes, I hear you.{p=1.0}Loud and clear."

    g "You have an unusual talent..."
    g "For most people that's only sine, square, triangle waves.{p=1.0}For you this is someting more...{p=1.0}...this is a human speech." #dla większości ludzi to tylko sinusoidy, fale kwadratowe czy trójkątne. Dla ciebie to coś więcej...to mowa ludzka.

    l "OK, but what do you want from me?"

    g "Well, I'm only residue after Philosons - sound lovers ancient civilization" #Cóż, jestem jedyną pozostałością po Filosonach (gr. philos - kochający, esp. sono - dźwięk) - starożytnej cywilizacji miłośników dźwięku
    p "We were living here thousands years ago. Sound was our god. Over the years we were learning how to use useful sounds i.e. constructing more and more complicated musical instruments." #nie wiem czy dobrze robie z tym were
    p "Our time has passed, but you can keep our achievements alive." #będzie jakieś lepsze określenie na utrzymanie w sensie dorobku cywilizacji?
    p "Do you agree? That knowledge can be useful for humanity."

    menu:

        "Yes":

            jump choice_yes

        "No":

            jump choice_no

    label choice_yes:

    l "Yes, I'll have to pass on your achievements." #tak, chcę przekazać wasz dorobek

    p "Great, stay awhile and listen..."

    scene bg black with dissolve

    centered "That day Philoson gave to Lucas a part of his knowledge..."

    centered "Lucas was regularly comming to the chamber to acquire informations about Philosons technologies..."

    centered "He has began to write this for posperity..."

    stop music fadeout(7)

    $ renpy.pause(7, hard=True)

    centered "...but one day..."

    play music "./sounds/firealarm.mp3" noloop


    scene bg chamber_fire with fade_end
    
    play voice "./sounds/scream.wav"

    l "NOOO!{p=2.0}I can't leave him alone!" #nie mogę go zostawić

    play music "./sounds/bigfire.mp3" fadein 1.0 fadeout 1.0

    l "Goodbye{cps=3}...{/cps}everybody..."

    scene bg chamber_fire_run1 with Dissolve(1)

    $ renpy.pause(1, hard=True)

    scene bg chamber_fire_run2 with Dissolve(1)

    $ renpy.pause(1, hard=True)

    scene bg chamber_fire_run3 with Dissolve(1)

    $ renpy.pause(1, hard=True)

    scene bg chamber_fire_run4 with Dissolve(1)

    $ renpy.pause(1, hard=True)

    scene bg black with fade_end


    $ renpy.music.set_volume(0.5, delay=0, channel="music")

    play voice "./sounds/die_pain.mp3" noloop

    centered "{size=48}Bad Ending...{/size}"


    centered "{size=48}...and True Ending{/size}"

    stop music fadeout 1.0

    jump credits

    



    return





    label choice_no:

    l "Sorry, but{cps=3}...{/cps}I'm{cps=3}...{/cps}not ready for this."

    p "Your choice..."

    stop music fadeout(5)

    $ renpy.pause(5, hard=True)

    l "He's gone...{p=2.0}Now time to go out..." #

    scene bg black with fade

    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(3)

    centered "{size=36}Few weeks later...{/size}"

    $ renpy.pause(1)

    play music "./sounds/park.wav"

    play sound "./sounds/wire.wav" noloop

    $ renpy.pause(2)
    
    play sound "./sounds/footsteps.wav" noloop

    $ renpy.pause(2)

    scene bg chamber_ruin with dissolve

    

    play voice "./sounds/scream.wav" noloop
    
    l "NOOO!"

    scene bg black with fade_end


    show text "That was my big mistake..." at x1 as line1 with dissolve
    $ renpy.pause(3)
   
    show text "Philosons knowledge had been irretrievably lost..." at x2 as line2 with dissolve
    $ renpy.pause(3)       
   
    show text "I'm not scientist, but that all could be really useful for humanity..." at x3 as line3 with dissolve
    $ renpy.pause(3)
       
    show text "Now I must live with the consequences of the choice I made..." at x4 as line4 with dissolve
    $ renpy.pause(3)

    hide line1
    hide line2
    hide line3
    hide line4
    with fade_end

    centered "{size=48}Bad Ending{/size}"

    stop music fadeout 2.0

    jump credits


    return


    label credits:

    scene bg title with fade_end

    show text "a visual novel game by Daniel \"TheLaw1337\" Sobczak \n for Ludum Dare 36" at c1 as line1 with dissolve
    $ renpy.pause(3)
   
    show text "Thanks to weeman and Kuba for text correction" at c2 as line2 with dissolve
    $ renpy.pause(3) 

    show text "Thank you for playing" at c3 as line3 with dissolve
    $ renpy.pause(3) 

    scene bg black with dissolve

    hide line1
    hide line2
    hide line3
    with fade_end

    return
