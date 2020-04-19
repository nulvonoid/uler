#bikin uler-uleran https://www.youtube.com/watch?v=BP7KMlbvtOo

import turtle               #install dulu, apt install python3-tk 
import time
import random

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

#makanan uler (kopas aja kepalanya)
emam = turtle.Turtle()
emam.speed(0)
emam.shape("square")
emam.color("green")
emam.penup()                  
emam.goto(0,100)

segmen = []       #tiap kali kepala emam, kelapa nambah segment.



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

    if kepala.distance (emam) <20:              #ini artinya collide, default ukuran turtle 20x20. jadi kalo jarak udah dibawah 20, berarti udah ketemu (kemakan)
        #pindahin emam random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        emam.goto(x,y)

        #buat nambahin segment
        segmen_baru = turtle.Turtle()
        segmen_baru.speed(0)
        segmen_baru.shape("square")
        segmen_baru.color("grey")
        segmen_baru.penup()
        segmen.append(segmen_baru)      #ini nambah segmen_baru ke list segmen di atas

    #pindahin segmen terakhir ke pertama tapi urutannya kebalik
    for index in range(len(segmen)-1,0,-1):
        x = segmen[index-1].xcor()
        y = segmen[index-1].ycor()
        segmen[index].goto(x,y)

    #pindahin segmen ke - 0 ke tempat kepala
    if len(segmen) > 0:
        x = kepala.xcor()
        y = kepala.ycor()
        segmen[0].goto(x,y)

    gerak()

    time.sleep(delay)



layar.mainloop()            #ini baris terakhir banget