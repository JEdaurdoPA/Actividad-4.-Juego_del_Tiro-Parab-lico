"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # AUMENTA VELOCIDAD DEL PROYECTIL (antes era /25)
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(30) == 0:  # MÁS FRECUENTE (antes era 40)
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.5  # AUMENTA VELOCIDAD DE LOS TARGETS (antes era 0.5)
        if target.x < -200:
            target.x = 200
            target.y = randrange(-150, 150)

    if inside(ball):
        speed.y -= 0.7  # AUMENTA EFECTO DE LA GRAVEDAD (antes era 0.35)
        ball.move(speed)
    else:
        ball.x, ball.y = -200, -200
        speed.x, speed.y = 0, 0

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 30)  # MÁS ACTUALIZACIONES POR SEGUNDO (antes era 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
