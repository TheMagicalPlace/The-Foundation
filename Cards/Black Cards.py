from random import randint
class BlackCardSetup():
    card_type = 'Black'

    def __init__(self):
        self.cardlist = [self.Black01,self.Black02,self.Black03,self.Black04,self.Black05]
    def card_selector(self):
        card_id = randint(1,len(self.cardlist))
        card = [x for x in self.cardlist if card_id == x.id][0]
        return print(card())

    class blackCards():

        def __init__(self):
            self.card_type = 'BLACK'
            self.card_title = 'n/q'
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
           |                     |
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
           |                     |
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
           |                     |
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
           |                     |
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
             '''


            return e

    class Black01(blackCards):

        """Someone has a grudge! The Sun God Nergal punches you! Ouch!"""
        id = 1

        def __init__(self):
            super().__init__()
            self.card_title = 'Fuck This Guy Specifically'

        def effect_on_action(self):
            """Effect: The player is punched by a Supreme Divine being, and dies."""
            # TODO - implementation of effect
            pass

    class Black02(blackCards):

        """Description: Oh no! All of your contained anomalies are loose! What a disastrous circumstance!

            Effect: Any contained anomalies return to the gameboard."""
        id = 2

        def __init__(self):
            super().__init__()
            self.card_title = 'Containment Breach'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Black03(blackCards):

        """Description: Your companion betrays you, seeking glory only for themselves!

            Effect: Any companions become hostile to the player."""
        id = 3

        def __init__(self):
            super().__init__()
            self.card_title = 'Friend or Foe'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Black04(blackCards):

        """Description: A deal is signed. The Foundation dissolves! Only the Coalition remains!

            Effect: Removes the MR. CONTAINMENT and MR. FOUNDATION win conditions."""
        id = 4

        def __init__(self):
            super().__init__()
            self.card_title = ' Consolidation'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass



    class Black05(blackCards):

        """Description: Bad luck, hombre.

         Effect: Player is killed.12"""
        id = 5

        def __init__(self):
            super().__init__()
            self.card_title = '(••/•••••/••/•)'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass