import pyxel
from Player import *


player = Player()


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btn(pyxel.KEY_RIGHT):
        player.moveRight()
    elif pyxel.btn(pyxel.KEY_LEFT):
        player.moveLeft()
    else:
        player.stop()


def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
    player.draw()


pyxel.init(256, 144)
pyxel.load("assets/my_game.pyxres")
pyxel.run(update, draw)
