import pyxel

pyxel.init(256, 144)
pyxel.load("assets/my_game.pyxres")


class Player:
    x = 2
    y = 9


player = Player()


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btn(pyxel.KEY_RIGHT):
        player.x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        player.x -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        player.y += 1
    if pyxel.btn(pyxel.KEY_UP):
        player.y -= 1


def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
    pyxel.blt(
        player.x,  # position X
        player.y,  # position Y
        0,  # image bank
        19,  # position x in image bank
        1,  # position y in image bank
        8,  # width
        13,  # height
        0  # transparent color
    )


pyxel.run(update, draw)
