from random import randint
class BlueCardSetup():
    card_type = 'Blue'

    def __init__(self):
        pass
        self.cardlist = [self.Blue01,self.Blue02,self.Blue03,self.Blue04,
                         self.Blue05]
    def card_selector(self):
        card_id = randint(1,len(self.cardlist))
        card = [x for x in self.cardlist if card_id == x.id][0]
        return print(card())

    class blueCards():

        def __init__(self):
            self.card_type = 'BLUE'
            self.card_title = 'n/a'
            self.subtitle = 'n/a'
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

    class Blue01(blueCards):

        """Summons SCP Site-19 Director Moose to act as your companion. Is a literal moose.
        When riding Director Moose, gain +7 DEF against memes and cognitive hazards."""
        id = 1

        def __init__(self):
            super().__init__()
            self.card_title = 'Director Tilda Moose'
            self.subtitle = 'Not sure how they got here.'
            self.type = 'Companion'
            self.stats = {'atk': 5, 'def': 8, 'hp': 9}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass
    class Blue02(blueCards):

        """ Spawns A Sea Slug to act as your companion.
        Wields an anti-materiel rifle. Talks a lot.
        Can summon a ghostly butler to do your bidding (with limitations!),
        but has a 10 round cool-down."""
        id = 2

        def __init__(self):
            super().__init__()
            self.card_title = 'A Sea Slug'
            self.subtitle = 'A Proper Gentleman'
            self.type = 'Companion'
            self.stats = {'atk': 13, 'def': 2, 'hp': 4}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass


    class Blue03(blueCards):

        """ Summons a Librarian to act as your companion.
        Has innate knowledge about a vast array of creatures and realms.
        Might be able to read your opponent’s hands, who knows.
        If attacked, they’ll flee back to their Library. Typical."""
        id = 3

        def __init__(self):
            super().__init__()
            self.card_title = 'A Librarian'
            self.subtitle = 'A Wanderer'
            self.type = 'Companion'
            self.stats = {'atk': 3, 'def': 3, 'hp': 6}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Blue04(blueCards):

        """ Summons some sort of awful eldritch abomination stuffed into the body of a small bird to act as your
        companion. Despicably loud. Can stun foes and entities, and commune with fellow anomalies. Unless otherwise
        protected, players who spend too much time in the presence of A Very Loud Bird will slowly lose their minds. """
        id = 4

        def __init__(self):
            super().__init__()
            self.card_title = 'A Very Loud Bird'
            self.subtitle = 'oh god make it stop'
            self.type = 'Companion'
            self.stats = {'atk': 8, 'def': 4, 'hp': 4}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Blue05(blueCards):

        """ Summons a ghostly Surf Rock Band to act as your companion. Provides your journey with cool evening tunes
        and casts a calming influence on everything you encounter. May also be able to commune with the Starfish. May
        also just smoke a lot of weed. """
        id = 5

        def __init__(self):
            super().__init__()
            self.card_title = 'Surf Rock Band'
            self.subtitle = 'Cruising The Starry Skies'
            self.type = 'Companion'
            self.stats = {'atk': 5, 'def': 5, 'hp': 6}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass


