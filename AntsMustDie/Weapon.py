import random
from WeaponFeature import * 

class Weapon(object):
    """description of Weapon"""

    def __init__ (self):
        self.x_position         = 0#= _x_position
        self.y_position         = 0#= _y_position
        self.age                = 0#= _age
        self.damage_min         = 0#= _damage_min
        self.damage_max         = 0#= _damage_max
        self.damage             = 0#= _damage
        self.fire_speed         = 0#= _fire_speed
        self.reloading_time     = 0#= _reload_time
        self.range              = 0#= _range


    #def __init__ (
    #    self, 
    #    _x_position,
    #    _y_position,
    #    _age,
    #    _damage_min,
    #    _damage_max,
    #    _damage, 
    #    _fire_speed,
    #    _reload_time,
    #    _range_min,
    #    _range_max,
    #    _range
    #):
    #    self.x_position         = _x_position
    #    self.y_position         = _y_position
    #    self.age                = _age
    #    self.damage_min         = _damage_min
    #    self.damage_max         = _damage_max
    #    self.damage             = _damage
    #    self.fire_speed         = _fire_speed
    #    self.reloading_time     = _reload_time
    #    self.range_min          = _range_min
    #    self.range_max          = _range_max
    #    self.range              = _range

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

    def getFireSpeed(self):
        return self.fire_speed

    def getReloadingTime(self):
        return self.reloading_time

    def getRange(self):
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

    def setFireSpeed(self, _fire_speed):
        self.fire_speed = _fire_speed

    def setReloadingTime(self, _reload_time):
        self.reloading_time = _reload_time

    def setRange(self, _range):
        self.range = _range


    #############################
    #############################
    

    #############################
    # Generation

    def generate(self):
        # Tirage aléatoire pour définir l'age
        print("nb age "+str( WeaponFeature.AGE.N_AGE))
        self.age = random.randint(0,WeaponFeature.AGE.N_AGE)
        print("age "+str(self.age))
        if self.age == WeaponFeature.AGE.PREHISTORIC:
            # Tirage aléatoire pour définir l'arme
            weapon = random.randint(0,WeaponFeature.AGE.PREHISTORIC_WEAPON.N_PREHISTORIC_WEAPON)
            #############################
            if weapon == PrehistoricWeapon.BOW:
                # Initialisation des valeurs
                val1 = random.randint(
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.DAMAGE_MIN, 
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.DAMAGE_MAX
                )
                #tt=WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW
                #tt.
                val2 = random.randint(
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.DAMAGE_MIN, 
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.DAMAGE_MAX
                )
                if val1 > val2:
                    self.damage_min = val2
                    self.damage_max = val1
                else:
                    self.damage_min = val1
                    self.damage_max = val2
                self.fire_speed = random.randint(
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.FIRE_SPEED_MIN,
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.FIRE_SPEED_MAX
                )
                self.reloading_time = random.randint(
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.RELOAD_TIME_MIN,
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.RELOAD_TIME_MAX
                )
                self.range = random.randint(
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.RANGE_MIN,
                    WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW.RANGE_MAX
                )
                
            #############################

        ##########################################################
        elif self.age == WeaponFeature.AGE.MIDDLE_AGES:
            toto = 2

        #self.type=rand(0,2)

        #min = self.type*rangeAge
        #min = (self.type+1)*rangeAge


        #if TypeError==PREHIUST:
        #    min_value = 0
        #    max_value = 100


        #dgt=rand(main,id,max=)
        #self.type=preHist.type(rand))

        #dgt=ArcDgt(rand(0,1))
        #range=range(Arc (rand(0,1)))
