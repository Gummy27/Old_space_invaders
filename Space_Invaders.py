import turtle


# Skjár
skjar = turtle.Screen()
skjar.title("Space Invaders")
skjar.bgcolor("black")
skjar.setup(width=800, height=800)
skjar.bgpic("Space_Invaders.png")

# Rammi
RammaTeiknari = turtle.Turtle()
RammaTeiknari.penup()
RammaTeiknari.setposition(-300, -300)
RammaTeiknari.pendown()
RammaTeiknari.pencolor("white")
RammaTeiknari.speed(0)
for x in range(4):
    RammaTeiknari.forward(600)
    RammaTeiknari.left(90)
RammaTeiknari.hideturtle()


## Spilari
# Spilarinn er skilgreindur
spilari = turtle.Turtle()
spilari.penup()
spilari.color("blue")
spilari.shape("triangle")
spilari.setposition(0, -280)
spilari.setheading(90)
spilari.speed(0)

spilaraHradi = 15

# Föll svo að spilarinn geti fært sig.
def haegri():
    x = spilari.xcor()
    x += spilaraHradi
    if x > 285:
        x = 285
    spilari.setx(x)
    skjar.update()

def vinstri():
    x = spilari.xcor()
    x -= spilaraHradi
    if x < -285:
        x = -285
    spilari.setx(x)
    skjar.update()



## Skot
# Skotið er skilgreint
skot = turtle.Turtle()
skot.penup()
skot.color("yellow")
skot.shape("triangle")
skot.shapesize(0.25, 0.25)
skot.setposition(-300, -300)
skot.hideturtle()
skot.setheading(90)
skot.speed(0)

skotHradi = 10

def skjota():
    skot.showturtle()
    skot.setposition(spilari.xcor(), spilari.ycor()+8)

## Óvinur
# Óvinurinn skilgreindur
ovinir = []
for y in range(0, 60, 30):
    for x in range(0, 100, 50):
        ovinur = turtle.Turtle()
        ovinur.penup()
        ovinur.color("white")
        ovinur.shape("circle")
        ovinur.speed(0)
        ovinur.setposition(-260+x, 260-y)
        ovinir.append(ovinur)


ovinarHradi = 5

turtle.listen()
turtle.onkeypress(haegri, "Right")
turtle.onkeypress(vinstri, "Left")
turtle.onkeypress(skjota, "space")

while True:
    # Hreyfa óvininn
    if ovinir[0].xcor() < -285 or ovinir[3].xcor() > 285:
        ovinarHradi *= -1
        for ovinur in ovinir:
            ovinur.sety(ovinur.ycor()-30)
    for ovinur in ovinir:
        x = ovinur.xcor()
        x += ovinarHradi
        ovinur.setx(x)

    # Hreyfa skotið
    y = skot.ycor()
    y += skotHradi
    skot.sety(y)
    if skot.ycor() > 300:
        skot.hideturtle()
    for ovinur in ovinir:
        if skot.distance(ovinur) < 10:
            ovinur.hideturtle()
            skot.hideturtle()
