# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
init:
    image bg black = "#000000"

# The game starts here.
label start:

    scene bg black

    e "Utworzyłeś grę na Ren'Py."

    e "Dodaj tylko historię, obrazy i muzykę, potem możesz ją puścić w świat!"

    return
