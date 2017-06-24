class WeaponFeature(object):
    """description of class"""


    # Définition des ages
    class AGE():
        PREHISTORIC = 0
        MIDDLE_AGES = 1
        N_AGE = 2

        ##########################################################
        ##########################################################

        # Définition des armes Prehistorique
        class PREHISTORIC_WEAPON():
            BOW     = 0 # ARC
            SLING   = 1 # FRONDE
            SPEAR   = 2 # LANCE
            JAVELIN = 3 # JAVELOT
            N_PREHISTORIC_WEAPON = 4

            #############################

            class PREHISTORIC_BOW():
                DAMAGE_MIN      = 0
                DAMAGE_MAX      = 100
                FIRE_SPEED_MIN  = 0 
                FIRE_SPEED_MAX  = 100
                RELOAD_TIME_MIN = 0
                RELOAD_TIME_MAX = 100
                RANGE_MIN       = 0
                RANGE_MAX       = 100

            #############################
            #############################
            #############################

        ##########################################################
        ##########################################################

        # Définition des armes du MoyenAge
        class MIDDLEAGES_WEAPON():
            BOW         = 0 # ARC
            CROSSBOW    = 1 # ARBALETE
            THROW_AX    = 2 # HACHE DE JET
            JAVELIN     = 3 # JAVELOT
            N_MIDDLE_AGE_WEAPON = 4
