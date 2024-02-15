import turtle
import time
import random

cizim_ekrani = turtle.Screen()
cizim_ekrani.bgcolor("white")
cizim_ekrani.title("Python Turtle")
cizim_ekrani.screensize(500, 500)

player = turtle.Turtle()
player.shape("turtle")
player.color("DodgerBlue")
player.shapesize(1)
player.penup()



bilgi = int(turtle.numinput("Merhaba Oyuncu", "Lütfen Süreyi Giriniz:"))
puan = 0
def puan_guncelle(x, y):
    global puan
    puan += 1
    player.clear()
    player.write("Puan: {}".format(puan), align="right", font=("Arial", 16, "normal",))
cizim_ekrani.onscreenclick(puan_guncelle)
player.write("Puan: {}".format(puan), align="center", font=("Arial", 16, "normal"))

for i in range(bilgi):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    player.teleport(x, y)
    time.sleep(1)  # Kaldırıldı

turtle.mainloop()
