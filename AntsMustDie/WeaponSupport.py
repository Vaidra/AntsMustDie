class WeaponSupport(object):
    """description of tower"""

    def __init__ (
        self, 
        _x_position,
        _y_position,
        _life       = 100,
        _damage     = 5, 
        _fire_speed = 1
    ):
        self.x_position = _x_position
        self.y_position = _y_position
        self.damage     = _damage
        self.fire_speed = _fire_speed
        self.life       = _life

    # Getteur
    def getXPosition(self):
        return self.x_position

    def getYPosition(self):
        return self.y_position

    def getDamage(self):
        return self.damage

    def getFireSpeed(self):
        return self.fire_speed

    def getLife(self):
        return self.life

    # Setteur
    def setXPosition(self, _x_position):
        self.x_position = _x_position

    def setYPosition(self, _y_position):
        self.y_position = _y_position

    def setDamage(self, _damage):
        self.damage = _damage

    def setFireSpeed(self, _fire_speed):
        self.fire_speed = _fire_speed

    def setLife(self, _life):
        self.life = _life

