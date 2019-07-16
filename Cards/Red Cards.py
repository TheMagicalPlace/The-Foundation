from random import randint
class RedCardSetup():
    card_type = 'Red'

    def __init__(self):
        pass
        self.cardlist = [self.Red01,self.Red02,self.Red03,self.Red04,
                         self.Red05,self.Red06,self.Red07,self.Red08,
                         self.Red09]
    def card_selector(self):
        card_id = randint(1,len(self.cardlist))
        card = [x for x in self.cardlist if card_id == x.id][0]
        return print(card())

    class redCards():
            #TODO update string for speed instead of hp
        def __init__(self):
            self.card_type = 'RED'
            self.card_title = 'n/a'
            self.subtitle = 'n/a'
            self.type = 'n/a'
            self.subtype = 'n/a'
            self.type = 'n/a'
            self.stats = {'atk':-1,'def':-1,'hp':-1}
        def __str__(self):

            title = self.card_title.split() if ' ' in self.card_title else [self.card_title]

            e = '''
            _____________________  
           |        '''+self.card_type+'''         |
           |'''+'{:^2}'.format(title[0])+'''|
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |'''+' ATK:{0[0]:^2}/DEF:{0[1]:^2}/HP:{0[2]:^2} '.format(list(self.stats.values()))+'''|
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''\
            if len(title) == 1 else\
                '''
            _____________________ 
           |''' + '{:^21}'.format(self.card_type) + '''|
           |''' + '{:^21}'.format(title[0]+' '+title[1]) + '''|
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |'''+' ATK:{0[0]:^2}/DEF:{0[1]:^2}/HP:{0[2]:^2} '.format(list(self.stats.values()))+'''|
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                 '''\
            if len(title) == 2 else\
                 '''
            _____________________ 
           |''' + '{:^21}'.format(self.card_type) + '''|
           |''' + '{:^21}'.format(title[0]+' '+title[1]) + '''|
           |''' + '{:^21}'.format(title[2]) + '''|
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |'''+' ATK:{0[0]:^2}/DEF:{0[1]:^2}/HP:{0[2]:^2} '.format(list(self.stats.values()))+'''|
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                 '''\
            if len(title) == 3 else \
                '''
            _____________________ 
           |''' + '{:^21}'.format(self.card_type) + '''|
           |''' + '{:^21}'.format(title[0]+' '+title[1]) + '''|
           |''' + '{:^21}'.format(title[2] + ' '+ title[3]) + '''|
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |                     |
           |'''+' ATK:{0[0]:^2}/DEF:{0[1]:^2}/HP:{0[2]:^2} '.format(list(self.stats.values()))+'''|
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
             '''


            return e

    class Red01(redCards):

        """A massive harpoon gun designed to make mortals of gods.
        Can only be used on Cosmic, Divine, or Supreme Divine beings."""
        id = 1

        def __init__(self):
            super().__init__()
            self.card_title = 'Spear of the Nonbeliever'
            self.type,self.subtype = 'Weapon','Ranged'
            self.stats = {'atk': 20, 'def': -1, 'spd': -5}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass


    class Red02(redCards):

        """A big sword. Requires two hands to hold. Can cleft a man in twain with a single swing.
         Reduces stealth. Increases upper arm gains."""
        id = 2

        def __init__(self):
            super().__init__()
            self.card_title = 'Buster Sword'
            self.type,self.subtype = 'Weapon','Melee'
            self.stats = {'atk': 8, 'def': 0, 'spd': -3}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red03(redCards):

        """A cheap sword. Low damage, low attack speed. The first choice of suburban ninjas everywhere.
        Minus points to attack if wearing a fedora"""
        id = 3

        def __init__(self):
            super().__init__()
            self.card_title = 'K-Mart Katana'
            self.type,self.subtype = 'Weapon','Melee'
            self.stats = {'atk': -5, 'def': 0, 'spd': -5}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red04(redCards):

        """Allows the user to wield the great and terrible cosmic power of time, in very small increments.
        Users may return up to 10 seconds into the past. Expires after three uses. Paradoxes not included."""
        id = 4

        def __init__(self):
            super().__init__()
            self.card_title = 'Temporal Tinkering'
            self.type,self.subtype = 'Ability','Temporal'
            self.stats = {'atk': 0, 'def': 0, 'spd': 0}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red05(redCards):

        """A remarkably powerful .50BMG. Definitely not something you want to use yourself.
        Give it as a gift to an enemy, or anyone else you’d like to see spend the last few seconds of their life as a tiny,
        remarkably dense, screaming projectile. Expires after use."""
        id = 5

        def __init__(self):
            super().__init__()
            self.card_title = 'A Gun That Shoots People'
            self.type,self.subtype = 'Weapon','Ranged'
            self.stats = {'atk': 19, 'def': 0, 'spd': 0}
            # TODO add +5 ACC bonus
        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red06(redCards):

        """Provides the user with innate knowledge of very simple anomalous memes.
        If used correctly, can be really annoying. If used incorrectly, can be even more annoying."""
        id = 6

        def __init__(self):
            super().__init__()
            self.card_title = 'Intro to Memetics'
            self.type,self.subtype = 'Ability','Memetic'
            self.stats = {'atk': 0, 'def': 0, 'spd': 0}
        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red07(redCards):

        """A revolver used by infamous Foundation doctor Everett Mann. Bonus to accuracy.
        Bonus to damage vs. undead. Bonus to lunacy."""
        id = 7

        def __init__(self):
            super().__init__()
            self.card_title = 'Dr. Mann’s Six-Shooter'
            self.type,self.subtype = 'Weapon','Ranged'
            self.stats = {'atk': 10, 'def': 0, 'spd': 0}
            # TODO add +3 ACC bonus
        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red08(redCards):

        """Anyone holding this book receives a +3 bonus to smooth-talking,
        negotiations, salesmanship, and swindling. Side effects include greasy combed-back hair and cheap suits."""
        id = 8

        def __init__(self):
            super().__init__()
            self.card_title = 'Unethical Business Practices, 5th Edition'
            self.type,self.subtype = 'Ability','Memetic'
            self.stats = {'atk': 0, 'def': 0, 'spd': 0}
        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Red09(redCards):

        """A gun made of a god bound by the shredded souls of nine innocents. Instantly annihilates one being or
        artifact anywhere on the board, so long as the user is able to describe it. Expires after use. """
        id = 9

        def __init__(self):
            super().__init__()
            self.card_title = 'Unethical Business Practices, 5th Edition'
            self.type, self.subtype = 'Weapon','Ranged'
            self.stats = {'atk': '∞', 'def': 0, 'spd': 0}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass