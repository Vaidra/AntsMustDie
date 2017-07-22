import random
from WeaponFeature import * 

class Weapon(object):
    """description of Weapon"""

    def __init__ (self):
        self.age                = 0 # Age de l'arme
        self.type               = 0 # Type de l'arme
        self.x_position         = 0 # Position ligne
        self.y_position         = 0 # Position colonne
        self.damage_min         = 0 # Dégats minimaux
        self.damage_max         = 0 # Dégats maximaux
        self.damage             = 0 # Dégats aléatoire entre le min et max
        self.fire_speed         = 0 # Vitesse de tir
        self.reloading_time     = 0 # Temps de rechargement
        self.distance_max       = 0 # Distance maximale
        self.ammunition         = 1 # Munition dans un chargeur
        self.magasine           = 0 # Chargeur
        self.projectile_number  = 1 # Projectile par balle tirée

    # Getteur
    def getAge(self):
        return self.age

    def getType(self):
        return self.type

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

    def getDistanceMax(self):
        return self.distance_max

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

    def setDistanceMax(self, _distance_max):
        self.distance_max = _distance_max

    def setAmmunition(self, _ammunition):
        self.ammunition = _ammunition

    def setMagasine(self, _magasine):
        self.magasine =_magasine

    def setProjectileNumber(self, _projectile_number):
        self.projectile_number = _projectile_number

    #############################
    def getAgeName(self):
        if self.getAge() == WeaponFeature.AGE.PREHISTORIC :
            return "Prehistoric"
        elif self.getAge() == WeaponFeature.AGE.MIDDLE_AGES :
            return "MiddleAge"

    #def getTypeName(self):
        #if getType(self) == WeaponFeature.

    def getWeaponName(self):
        if self.getAge() == WeaponFeature.AGE.PREHISTORIC :
            if self.getType() == WeaponFeature.AGE.PREHISTORIC_WEAPON.BOW :
                return "Prehistoric Bow"
            elif self.getType() == WeaponFeature.AGE.PREHISTORIC_WEAPON.SLING :
                return "Prehistoric Sling"
            elif self.getType() == WeaponFeature.AGE.PREHISTORIC_WEAPON.SPEAR :
                return "Prehistoric Spear"
            elif self.getType() == WeaponFeature.AGE.PREHISTORIC_WEAPON.JAVELIN :
                return "Prehistoric Javelin"
        elif self.getAge() == WeaponFeature.AGE.MIDDLE_AGES :
            if self.getType() == WeaponFeature.AGE.MIDDLEAGES_WEAPON.BOW :
                return "Middle Ages Bow"
            elif self.getType() == WeaponFeature.AGE.MIDDLEAGES_WEAPON.CROSSBOW :
                return "Middle Ages CrossBow"
            elif self.getType() == WeaponFeature.AGE.MIDDLEAGES_WEAPON.THROW_AX :
                return "Middle Ages Throw Ax"
            elif self.getType() == WeaponFeature.AGE.MIDDLEAGES_WEAPON.JAVELIN :
                return "Middle Ages Javelin"



    #############################
    # Affichage des paramètres
    def displayInformations(self):
        print(" ### Weapon ###")
        print(self.getWeaponName())
        print("damage : "+str(self.damage_min) + " ; " + str(self.damage_max))
        print("fire speed : "+str(self.fire_speed))
        print("reloading time : "+str(self.getReloadingTime()))
        print("range : " + str(self.getDistanceMax()))
        print("Ammunition : " + str(self.getAmmunition()))
        print("Magasine : " + str(self.getMagasine()))
        print("ProjectileNumber : " + str(self.getProjectileNumber()))
        print(" ##############")        

    #############################
    # Generation

    def generate(self):
        # Declaration des variables
        weapon_feature = -1
        age_weapons = WeaponFeature.AGE.UNKNOWN
        weapon_id = -1

        # Tirage aléatoire pour définir l'age
        print("nb age "+str( WeaponFeature.AGE.N_AGE))
        self.age = random.randint(0,WeaponFeature.AGE.N_AGE-1)
        print("age "+str(self.age))

        # Récuperation des noms des armes poru initialiser les valeurs des caractéristiques
        #############################
        if self.age == WeaponFeature.AGE.PREHISTORIC:
            age_weapons = WeaponFeature.AGE.PREHISTORIC_WEAPON
            # Tirage aléatoire pour définir l'arme
            weapon_id = random.randint(0, age_weapons.N_PREHISTORIC_WEAPON-1)
            print(" id = " + str(weapon_id))
            self.type = weapon_id
            #############################
            if weapon_id == age_weapons.BOW:
                weapon_feature = age_weapons.PREHISTORIC_BOW
            elif weapon_id == age_weapons.SLING :
                weapon_feature = age_weapons.PREHISTORIC_SLING
            elif weapon_id == age_weapons.SPEAR :
                weapon_feature = age_weapons.PREHISTORIC_SPEAR
            elif weapon_id == age_weapons.JAVELIN :
                weapon_feature = age_weapons.PREHISTORIC_JAVELIN
        #############################
        elif self.age == WeaponFeature.AGE.MIDDLE_AGES:
            age_weapons = WeaponFeature.AGE.MIDDLEAGES_WEAPON
            weapon_id = random.randint(0,WeaponFeature.AGE.MIDDLEAGES_WEAPON.N_MIDDLE_AGE_WEAPON-1)
            print(" id = " + str(weapon_id))
            self.type = weapon_id
            #############################
            if weapon_id == age_weapons.BOW:
                weapon_feature = age_weapons.MIDDLEAGES_BOW
            elif weapon_id == age_weapons.CROSSBOW :
                weapon_feature = age_weapons.MIDDLEAGES_CROSSBOW
            elif weapon_id == age_weapons.THROW_AX :
                weapon_feature = age_weapons.MIDDLEAGES_THROW_AX
            elif weapon_id == age_weapons.JAVELIN :
                weapon_feature = age_weapons.MIDDLEAGES_JAVELIN
        #############################
        ### Initialisation des valeurs
        # Damage
        val1 = random.randint(
            weapon_feature.DAMAGE_MIN, 
            weapon_feature.DAMAGE_MAX
        )
        #tt=WeaponFeature.AGE.PREHISTORIC_WEAPON.PREHISTORIC_BOW
        #tt.
        val2 = random.randint(
            weapon_feature.DAMAGE_MIN, 
            weapon_feature.DAMAGE_MAX
        )
        if val1 > val2:
            self.damage_min = val2
            self.damage_max = val1
        else:
            self.damage_min = val1
            self.damage_max = val2
        self.fire_speed = random.randint(
            weapon_feature.FIRE_SPEED_MIN,
            weapon_feature.FIRE_SPEED_MAX
        )
        self.reloading_time = random.randint(
            weapon_feature.RELOAD_TIME_MIN,
            weapon_feature.RELOAD_TIME_MAX
        )
        self.distance_max = random.randint(
            weapon_feature.RANGE_MIN,
            weapon_feature.RANGE_MAX
        )
                
    #############################
    # to string
    def toString(self):
        s = str(
            str(self.getAge())               + ";" +
            str(self.getType())              + ";" +
            str(self.getDamageMin())         + ";" +
            str(self.getDamageMax())         + ";" +
            str(self.getFireSpeed())         + ";" +
            str(self.getReloadingTime())     + ";" +
            str(self.getDistanceMax())       + ";" +
            str(self.getAmmunition())        + ";" +
            str(self.getMagasine())          + ";" +
            str(self.getProjectileNumber())
        )
        return s

    #############################
    # Sauvegarde de l'arme
    def save(self,_filename):
        file = open(_filename, "w")
        file.write(str(self.toString()+"\n"))
        file.close()

    #############################
