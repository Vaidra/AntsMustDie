import random
from WeaponFeature import * 

class Weapon(object):
    """description of Weapon"""

    def __init__ (self):
        self.x_position         = 0 # Position ligne
        self.y_position         = 0 # Position colonne
        self.age                = 0 # Age de l'arme
        self.damage_min         = 0 # Dégats minimaux
        self.damage_max         = 0 # Dégats maximaux
        self.damage             = 0 # Dégats aléatoire entre le min et max
        self.fire_speed         = 0 # Vitesse de tir
        self.reloading_time     = 0 # Temps de rechargement
        self.range              = 0 # Distance
        self.ammunition         = 0 # Munition dans un chargeur
        self.magasine           = 0 # Chargeur
        self.projectile_number  = 0 # Projectile par balle tirée

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

    def getAmmunition(self):
        return self.ammunition

    def getMagasine(self):
        return self.magasine

    def getProjectileNumber(self):
        return self.projectile_number

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

    def setAmmunition(self, _ammunition):
        self.ammunition = _ammunition

    def setMagasine(self, _magasine):
        self.magasine =_magasine

    def setProjectileNumber(self, _projectile_number):
        self.projectile_number = _projectile_number



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
