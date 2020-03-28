import pyxel

from typing import Any, Dict, List

_PLAYER_SPRITES: Dict[str, List[Any]] = {
    'walkingRight': [(4, 2, 6, 14), (19, 1, 8, 14), (34, 1, 10, 13), (51, 2, 8, 13)],
    'walkingLeft': [(4, 18, 6, 14), (19, 17, 8, 14), (34, 17, 10, 13), (51, 18, 8, 13)],
    'standing': [(4, 34, 7, 14)],
    'jumpingRight': [],
    'jumpingLeft': []
}


class Player:

    def __init__(self, x=5, y=10):
        self.sprite_ord: int = 0
        self.pos_x: int = x
        self.pos_y: int = y
        self.coor_current_sprite = 0
        self.state = 'standing'

    def moveRight(self):
        self.pos_x += 1
        if self.state == 'walkingRight':
            self.coor_current_sprite = (
                self.coor_current_sprite + 1) % (len(_PLAYER_SPRITES[self.state])*2)

        else:
            self.state = 'walkingRight'
            self.coor_current_sprite = 0

    def moveLeft(self):
        self.pos_x -= 1
        if self.state == 'walkingLeft':
            self.coor_current_sprite = (self.coor_current_sprite +
                                        1) % (len(_PLAYER_SPRITES[self.state])*2)
        else:
            self.state = 'walkingLeft'
            self.coor_current_sprite = 0

    def stop(self):
        self.coor_current_sprite = 0
        self.state = 'standing'

    def draw(self):
        sprite = _PLAYER_SPRITES[self.state][self.coor_current_sprite//2]
        pyxel.blt(
            self.pos_x,  # position X
            self.pos_y,  # position Y
            0,  # image bank
            *sprite,
            0  # transparent color
        )
