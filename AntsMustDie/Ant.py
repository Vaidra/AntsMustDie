class Ant(object):
    """description of ant"""

    def __init__ (
        self, 
        _damage     = 5, 
        _fire_speed = 1,
        _life       = 100,
        _move_speed = 1
    ):
        self.damage     = _damage
        self.fire_speed = _fire_speed
        self.life       = _life
        self.move_speed = _move_speed

    def getDamage(self):
        return self.damage

    def getFireSpeed(self):
        return self.fire_speed

    def getLife(self):
        return self.life

    def setLife(self, _life):
        self.life = _life




