import turtle
import time
import random

cizim_ekrani = turtle.Screen()
cizim_ekrani.bgcolor("white")
cizim_ekrani.title("Python Turtle Game")
cizim_ekrani.screensize(500, 500)


skor_tutucu = turtle.Turtle()
skor_tutucu.hideturtle()
skor_tutucu.penup()
skor_tutucu.color("green3")
skor_tutucu.setpos(0, 350)
skor = 0
skor_tutucu.write("Puan: {}".format(skor), align="left", move=False, font=("Arial", 20, "normal"))

sure_bilgi = int(turtle.numinput("Merhaba Oyuncu", "Lütfen Süreyi Giriniz:"))
sure_tutucu = turtle.Turtle()
sure_tutucu.hideturtle()
sure_tutucu.penup()
sure_tutucu.color("green3")
sure_tutucu.setpos(0, 320)
sure_tutucu.write("Süre: {}".format(sure_bilgi), align="left", move=False, font=("Arial", 20, "normal"))

player = turtle.Turtle()
player.color("DodgerBlue")
player.shape("turtle")
player.shapesize(4)
player.penup()
player.speed(2)

def puan_guncelle(x, y):
    global skor
    skor_tutucu.clear()
    skor += 1
    skor_tutucu.write("Puan: {}".format(skor), align="left", font=("Arial", 20, "normal"))

def turtleye_tikla(x, y):
    if player.distance(x, y) < 20:
        puan_guncelle(x, y)

baslangic_zamani = time.time()

while time.time() - baslangic_zamani < sure_bilgi:
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.onscreenclick(turtleye_tikla)
    kalan_sure = int(sure_bilgi - (time.time() - baslangic_zamani))
    sure_tutucu.clear()
    sure_tutucu.write("Süre: {}".format(kalan_sure), align="left", move=False, font=("Arial", 20, "normal"))
    player.goto(x, y)
    if kalan_sure <= 0:
        oyun_bitti = True
        sure_tutucu.clear()
        skor_tutucu.clear()
        sure_tutucu.write("Game Over", align="left", move=False, font=("Arial", 20, "normal"))

turtle.mainloop()
