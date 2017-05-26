class Tower(object):
    """description of tower"""

    def __init__ (        
        self, 
        x_position,
        y_position,
        _damage     = 5, 
        _fire_speed = 1,
        _life       = 100
    ):
        self.damage     = _damage
        self.fire_speed = _fire_speed
        self.life       = _life

    def getDamage(self):
        return self.damage

    def getFireSpeed(self):
        return self.fire_speed

    def getLife(self):
        return self.life

    def setLife(self, _life):
        self.life = _life

