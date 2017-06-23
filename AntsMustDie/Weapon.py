class Weapon(object):
    """description of Weapon"""


    def __init__ (
        self, 
        _x_position,
        _y_position,
        _damage_min,
        _damage_max,
        _damage, 
        _fire_speed_min,
        _fire_speed_max,
        _fire_speed,
        _reload_time_min,
        _reload_time_max,
        _reload_time,
        _range_min,
        _range_max,
        _range
    ):
        self.x_position         = _x_position
        self.y_position         = _y_position
        self.damage_min         = _damage_min
        self.damage_max         = _damage_max
        self.damage             = _damage
        self.fire_speed_min     = _fire_speed_min
        self.fire_speed_max     = _fire_speed_max
        self.fire_speed         = _fire_speed
        self.reloading_time_min = _reload_time_min
        self.reloading_time_max = _reload_time_max
        self.reloading_time        = _reload_time
        self.range_min          = _range_min
        self.range_max          = _range_max
        self.range              = _range

    # Getteur
    def getXPosition(self):
        return self.x_position

    def getYPosition(self):
        return self.y_position

    def getDamageMin(self):
        return self.damage_min

    def getDamageMax(self):
        return self.damage_max

    def getDamage(self):
        return self.damage

    def getFireSpeedMin(self):
        return self.fire_speed_min

    def getFireSpeedMax(self):
        return self.fire_speed_max

    def getFireSpeed(self):
        return self.fire_speed

    def getReloadingTimeMin(self):
        return self.reloading_time_min

    def getReloadingTimeMax(self):
        return self.reloading_time_max

    def getReloadingTime(self):
        return self.reloading_time

    def getRangeMin(self):
        return self.range_min

    def getRangeMax(self):
        return self.range_max

    def getRangeMin(self):
        return self.range


    # Setteur
    def setXPosition(self, _x_position):
        self.x_position = _x_position

    def setYPosition(self, _y_position):
        self.y_position = _y_position

    def setDamageMin(self, _damage_min):
        self.damage_min = _damage_min

    def setDamageMax(self, _damage_max):
        self.damage_max = _damage_max

    def setDamage(self, _damage):
        self.damage = _damage

    def setFireSpeedMin(self, _fire_speed_min):
        self.fire_speed_min = _fire_speed_min

    def setFireSpeedMax(self, _fire_speed_max):
        self.fire_speed_max = _fire_speed_max

    def setFireSpeed(self, _fire_speed):
        self.fire_speed = _fire_speed

    def setReloadingTimeMin(self, _reload_time_min):
        self.reloading_time_min = _reload_time_min

    def setReloadingTimeMax(self, _reload_time_max):
        self.reloading_time_max = _reload_time_max

    def setReloadingTime(self, _reload_time):
        self.reloading_time = _reload_time

    def setRangeMin(self, _range_min):
        self.range_min = _range_min
    
    def setRangeMax(self, _range_max):
        self.range_max = _range_max

    def setRange(self, _range):
        self.range = _range
