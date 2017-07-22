class WeaponSupportFeature(object):
    """description of class"""


    # Définition des ages
    class AGE():
        UNKNOWN    = -1
        PREHISTORIC = 0
        MIDDLE_AGES = 1
        N_AGE       = 2

        ##########################################################
        ##########################################################

        # Définition des armes Prehistorique
        class PREHISTORIC_SUPPORT():
            LIFE_MIN            = 0
            LIFE_MAX            = 100
            WEAPON_NUMBER_MIN   = 0 
            WEAPON_NUMBER_MAX   = 4

        #############################

        class MIDDLEAGES_SUPPORT():
            LIFE_MIN            = 0
            LIFE_MAX            = 200
            WEAPON_NUMBER_MIN   = 0 
            WEAPON_NUMBER_MAX   = 10

        #############################

        ##########################################################
        ##########################################################
    class TARGETING_METHODE():
        UNKNOWN = -1
        NEAREST_TARGET = 0 # Cible la plus proche
        FARTHEST_TARGET = 1 # Cible la plus éloignée


    class TARGET_CHANGE_METHODE():
        UNKNOWN = -1
        EACH_SHOT = 0 # à chaque tir
        NO_TARGET = 1 # Disparition de la cible
        COUNT = 2 # Compteur de tir
        TIME = 3 # Compteur de temps
        

