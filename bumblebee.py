import random
import pgzrun

WIDTH=600
HEIGHT=500
TITLE="capture the flag game"
score=0
game_over=False

astronaut=Actor("astronew.png")
flag=Actor("flag.jpg")

def draw():
    screen.blit("bg.png",(0,0))
    astronaut.draw()
    flag.draw()
    screen.draw.text("SCORE: " + str(score),color="white",topleft=(20,20))

    if game_over:
        screen.fill("black")
        screen.draw.text("TIME IS UP YOUR FINAL SCORE IS "+ str(score),color="white",topleft=(20,20))

def place_flag():
    flag.x=random.randint(50,550)
    flag.y=random.randint(50,450)

def timeup():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        astronaut.x-=5
    if keyboard.right:
        astronaut.x+=5
    if keyboard.up:
        astronaut.y-=5
    if keyboard.down:
        astronaut.y+=5
    
    flag_collected=astronaut.colliderect(flag)
    if flag_collected==True:
        score+=10
        place_flag()

clock.schedule(timeup,20)
pgzrun.go()
    