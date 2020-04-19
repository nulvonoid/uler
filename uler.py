#bikin uler-uleran https://www.youtube.com/watch?v=BP7KMlbvtOo

import turtle               #install dulu, apt install python3-tk 
import time

delay = 0.1

layar = turtle.Screen()
layar.title("Game Uler")
layar.bgcolor("black")
layar.setup(width = 600, height = 600)
layar.tracer(0)             # turns off screen update


#kepala uler
kepala = turtle.Turtle()
kepala.speed(0)
kepala.shape("square")
kepala.color("brown")
kepala.penup()                  #jadi kalo jalan ga bikin garis.
kepala.goto(0,0)
kepala.direction = "stop"

#function
def gerak():
    if kepala.direction == 'up':
        y = kepala.ycor()
        kepala.sety(y+20)

    if kepala.direction == 'down':
        y = kepala.ycor()
        kepala.sety(y-20)

    if kepala.direction == 'left':
        x = kepala.xcor()
        kepala.setx(x-20)

    if kepala.direction == 'right':
        x = kepala.xcor()
        kepala.setx(x+20)

def go_up():
    kepala.direction = "up"

def go_down():
    kepala.direction = "down"

def go_left():
    kepala.direction = "left"

def go_right():
    kepala.direction = "right"

# Keyboard bindings
layar.listen()
layar.onkeypress(go_up, "Up")           #function disini ga pake ()
layar.onkeypress(go_down, "Down")
layar.onkeypress(go_left, "Left")
layar.onkeypress(go_right, "Right")



#game utama loop
while True:
    layar.update()          #ini loop buat selalu update layar

    gerak()

    time.sleep(delay)



layar.mainloop()            #ini baris terakhir banget