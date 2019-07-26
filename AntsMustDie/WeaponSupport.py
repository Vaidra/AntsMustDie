import random
from WeaponSupportFeature import * 

class WeaponSupport(object):
    """description of tower"""

    def __init__ (
        self, 
        _x_position,
        _y_position,
        _life           = 100,
        _damage         = 5, 
        _fire_speed     = 1,
        _weapon_number  = 1,

    ):
        self.x_position = _x_position
        self.y_position = _y_position
        self.damage     = _damage
        self.fire_speed = _fire_speed
        self.life       = _life

    def __init__ (self): 
        self.age                    = 0 # Age du support
        self.x_position             = 0 # Position ligne
        self.y_position             = 0 # Position colonne
        self.life                   = 0 # Vie du support
        self.weapon_number          = 0 # Nombre d'arme portée
        self.bloc_number            = 0 # Nombre de bloc du support
        self.bloc_shape             = 0 # Forme du support
        self.targeting_methode      = 0 # Méthode de ciblage de la cible
        self.target_change_methode  = 0 # Méthode de changement de la cible

    # Getteur
    def getAge(self):
        return self.age

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

    def getWeaponNumber(self):
        return self.weapon_number

    def getBlocNumber(self):
        return self.bloc_number

    def getBlocShape(self):
        return self.bloc_shape

    def getTargetingMethode(self):
        return self.targeting_methode

    def getTargetChangeMethode(self):
        return self.target_change_methode

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

    #############################
    def getAgeName(self):
        if self.getAge() == WeaponSupportFeature.AGE.PREHISTORIC :
            return "Prehistoric support"
        elif self.getAge() == WeaponSupportFeature.AGE.MIDDLE_AGES :
            return "MiddleAge support"

    #############################
    def getTargetingMethodeName(self):
        targeting_methode = WeaponSupportFeature.TARGETING_METHODE
        if self.getTargetingMethode() == targeting_methode.NEAREST_TARGET :
            return "Nearest Target"
        elif self.getTargetingMethode() == targeting_methode.FARTHEST_TARGET :
            return "Farthest Target"

    #############################
    def getTargetChangeMethodeName(self):
        target_change_methode = WeaponSupportFeature.TARGET_CHANGE_METHODE
        if self.getTargetChangeMethode() == target_change_methode.EACH_SHOT :
            return "Each Shot"
        if self.getTargetChangeMethode() == target_change_methode.NO_TARGET :
            return "No Target"
        if self.getTargetChangeMethode() == target_change_methode.COUNT :
            return "Count"
        if self.getTargetChangeMethode() == target_change_methode.TIME :
            return "Time"

    #############################
    def getBlocShapeName(self):
        shape_methode = WeaponSupportFeature.SHAPE
        if self.getBlocShape() == shape_methode.HORIZONTAL_LINE :
            return "Horizontal Line"
        elif self.getBlocShape() == shape_methode.VERTICAL_LINE :
            return "Vertical Line"
        elif self.getBlocShape() == shape_methode.SQUARE :
            return "Square"
        elif self.getBlocShape() == shape_methode.CROSS :
            return "Cross"

    #############################
    # Affichage des paramètres
    def displayInformations(self):
        print(" ### Support ###")
        print(self.getAgeName())
        print("life : " + str(self.getLife()))
        print("bloc number : " + str(self.getBlocNumber()))
        print("bloc shape : " + self.getBlocShapeName())
        print("self.targeting_methode : "+ self.getTargetingMethodeName())
        print("target_change_methode : "+ self.getTargetChangeMethodeName())
        print(" ###############")

    #############################
    # Generation

    def generate(self):
        # Declaration des variables
        support_feature = -1
        # Tirage aléatoire pour définir l'age
        self.age = random.randint(0,WeaponSupportFeature.AGE.N_AGE-1)

        # Récuperation des noms des armes poru initialiser les valeurs des caractéristiques
        #############################
        if self.age == WeaponSupportFeature.AGE.PREHISTORIC:
            support_feature = WeaponSupportFeature.AGE.PREHISTORIC_SUPPORT
        #############################
        elif self.age == WeaponSupportFeature.AGE.MIDDLE_AGES:
            support_feature = WeaponSupportFeature.AGE.MIDDLEAGES_SUPPORT
        #############################

        # Tirage aléatoire pour définir le support
        ### Initialisation des valeurs
        # Life
        self.life = random.randint(
            support_feature.LIFE_MIN, 
            support_feature.LIFE_MAX
        )

        # BlocNumber
        self.bloc_number = random.randint(
            support_feature.BLOC_NUMBER_MIN, 
            support_feature.BLOC_NUMBER_MAX
        )

        # Shape
        if self.bloc_number == 1 :
            self.bloc_shape = WeaponSupportFeature.SHAPE.SQUARE
        elif self.bloc_number == 2 :
            self.bloc_shape = random.randint(
                WeaponSupportFeature.SHAPE.HORIZONTAL_LINE,
                WeaponSupportFeature.SHAPE.VERTICAL_LINE
            )
        elif self.bloc_number == 3 :
            self.bloc_shape = random.randint(
                WeaponSupportFeature.SHAPE.HORIZONTAL_LINE,
                WeaponSupportFeature.SHAPE.VERTICAL_LINE
            )
        elif self.bloc_number == 4 :
            self.bloc_shape = random.randint(
                WeaponSupportFeature.SHAPE.HORIZONTAL_LINE,
                WeaponSupportFeature.SHAPE.SQUARE
            )

        elif self.bloc_number == 5 :
            self.bloc_shape = random.randint(
                0,
                WeaponSupportFeature.SHAPE.NB_SHAPE - 1
            )
        
    #############################
    # to string
    def toString(self):
        s = str(
            str(self.getAge())                   + ";" +
            str(self.getLife())                  + ";" +
            str(self.getWeaponNumber())          + ";" +
            str(self.getBlocNumber())            + ";" +
            str(self.getBlocShape())             + ";" +
            str(self.getTargetingMethode())      + ";" +
            str(self.getTargetChangeMethode())
        )
        return s

    #############################
    # Sauvegarde de l'arme
    def save(self,_filename):
        file = open(_filename, "w")
        file.write(str(self.toString()+"\n"))
        file.close()

    #############################

