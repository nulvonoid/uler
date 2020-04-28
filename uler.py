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
def gerak():                            # ini bikin fungsi kalo up jadi apa, down jadi apa. tiap turtle itu punya xcor dan ycor. itu yang diganti2.
    if kepala.direction == 'up':
        y = kepala.ycor()
        kepala.sety(y+20)               #sety ini kita define ycor baru buat si kepala. bikin efek pindah gitu. 

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
    if kepala direction != "down":
        kepala.direction = "up"

def go_down():
    if kepala direction != "up":
        kepala.direction = "down"

def go_left():
    if kepala direction != "right":
        kepala.direction = "left"

def go_right():
    if kepala direction != "left":
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

    #kepala kena border
    if kepala.xcor()>290 or kepala.xcor()<-290 or kepala.ycor()>290 or kepala.ycor()<-290:
        time.sleep(1)
        kepala.goto(0,0)
        kepala.direction = "stop"

        #segmen ilang
        for segmen_baru in segmen:
            segmen_baru.goto(1000,1000)

        segmen.clear()


    if kepala.distance (emam) <20:              #ini artinya collide, default ukuran turtle 20x20. jadi kalo jarak udah dibawah 20, berarti udah ketemu (kemakan)
        #pindahin emam random
        x = random.randint(-290, 290)           #kenapa 290 karena ukuran layar kan 600 600, berarti di kiri -300, kanan 300 dst. kalo pas di pasang 300, nanti dia ilang setengah,
        y = random.randint(-290, 290)           #turtlenya kan 20x20, berarti tengah2nya 0,0; bates kirinya -10 bates kanannya 10. jadi kalo di set di 290, dia bakal tetep keliatan full kotak di ujung, center turtlenya di 290. 
        emam.goto(x,y)

        #buat nambahin segment
        segmen_baru = turtle.Turtle()           #badan itu segmen_baru. dia di def kaya objek turtle baru
        segmen_baru.speed(0)
        segmen_baru.shape("square")
        segmen_baru.color("grey")
        segmen_baru.penup()
        segmen.append(segmen_baru)      #ini nambah segmen_baru ke list segmen di atas

    #pindahin segmen terakhir ke pertama tapi urutannya kebalik
    for index in range(len(segmen)-1,0,-1):         #ini harus baca lagi ttg list. 
        x = segmen[index-1].xcor()                  
        y = segmen[index-1].ycor()
        segmen[index].goto(x,y)                        #intinya segmen barunya bakal ke tempat segmen sebelomnya yg terakhir.  

    #pindahin segmen ke - 0 ke tempat kepala
    if len(segmen) > 0:         # ini kali pertama makan, len list segmen langung nambah.
        x = kepala.xcor()
        y = kepala.ycor()
        segmen[0].goto(x,y)     #list segmen pindah ke tempat kepala sebelomnya. ini bikin efek badan ngikutin pala.

    gerak()

    #cek tumbukan sama badan
    for segmen_baru in segmen:
        if segmen_baru.distance(kepala) < 20:
            time.sleep(1)
            kepala.goto(0,0)
            kepala.direction="stop"

            for segmen_baru in segmen:
                segmen_baru.goto(1000,1000)


            segmen.clear()

    time.sleep(delay)       # biar ga kecepetan, jadi ada delaynya. delay di set diatas



layar.mainloop()            #ini baris terakhir banget