
from random import randint
class GreenCardSetup():

    def __init__(self):
        self.cards = 'Green'
        self.cardlist = [self.Green01,self.Green02,self.Green03,self.Green04,
                         self.Green05,self.Green06]
    def card_selector(self):
        card_id = randint(1,6)
        card = [x for x in self.cardlist if card_id == x.id][0]
        return print(card())

    class greenCards():

        def __init__(self):
            self.card_type = 'GREEN'
            self.card_title = 'City of the Gods'
            self.subtitle = 'n/a'
            self.type = 'n/a'

        def __str__(self):

            title = self.card_title.split()
            print(title)


            e = '''
            __________________ 
           |      '''+self.card_type+'''       |
           |'''+'{:^18}'.format(title[0])+'''|
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
           |                  |
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''\
            \
            if len(title) == 1 else\
                '''
                 __________________ 
                |      ''' + self.card_type + '''       |
                |''' + '{:^18}'.format(title[0]+' '+title[1]) + '''|
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                 '''\
            if len(title) == 2 else\
                 '''
                 __________________ 
                |      ''' + self.card_type + '''       |
                |''' + '{:^18}'.format(title[0]+' '+title[1]) + '''|
                |''' + '{:^18}'.format(title[2]) + '''|
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                |                  |
                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                 '''\
            if len(title) == 3 else \
                '''
             __________________ 
            |      ''' + self.card_type + '''       |
            |''' + '{:^18}'.format(title[0] + ' ' + title[1]) + '''|
            |''' + '{:^18}'.format(title[2]+' ' + title[3]) + '''|
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
             ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
             '''


            return e

    class Green01(greenCards):

        """Spawns a machine that, after a random amount of time, will transport anything nearby into the Darkness
        Between Dimensions. Players in the Darkness Between Dimensions can be saved by divine grace, or with the item
        “Scranton’s Grappling Hook”. After a random amount of time, players will be returned to the board. They will
        come back… squishier. """
        id = 1

        def __init__(self):
            super().__init__()
            self.card_title = 'Darkness Between Dimensions'
            self.subtitle = 'A Red Reality'
            self.type = 'Land'


        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Green02(greenCards):

        """Spawns the Babel Spire on a square of your choosing within line of sight.
        Nearby animals join your side, and gain +2 attack. Those who do not are sacrificed to Babel.
        Aya aya aya blood blood blood."""
        id = 2

        def __init__(self):
            super().__init__()
            self.card_title = 'Babel’s Spire'
            self.subtitle = 'The Friendly Union of Man and Beast'
            self.type = 'Structure'


        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Green03(greenCards):
        """If you are at sea, this card spawns an Island Turtle to ferry you around.
        If you’re not, the turtle spawns anyway, and dies from dehydration."""
        id = 3

        def __init__(self):
            super().__init__()
            self.card_title = 'Island Turtle'
            self.subtitle = 'Lazy Archipelago'
            self.type = 'Land'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Green04(greenCards):
        """Spawns a haunted city on a square of your choosing within line of sight.
        Opponents entering City of the Gods have a high chance of being attacked by a +15 ATK / +12 DEF angry deity."""
        id = 4

        def __init__(self):
            super().__init__()
            self.card_title = 'City of the Gods'
            self.subtitle = 'Coming Soon To Your Home Town!'
            self.type = 'Structure'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Green05(greenCards):
        """ If indoors, creates an infinite maze that opponents can only exit with assistance from outside forces. If outdoors, the effect isn’t noticeable, but trust us when we say it’s really bad."""
        id = 5

        def __init__(self):
            super().__init__()
            self.card_title = 'A Funny Little Statue'
            self.subtitle = 'ctrl+c ctrl+v'
            self.type = 'Trap'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Green06(greenCards):
        """  Spawns a friendly and welcoming department store. Players unfortunate enough to be inside the store when
        it opens will have to fight their way out, if they can get out at all. Bring your own instructions. """
        id = 6

        def __init__(self):
            super().__init__()
            self.card_title = 'A Swedish Furniture Store'
            self.subtitle = 'Perfectly Normal'
            self.type = 'Trap'

        def effect_on_action(self):
            # TODO - implementation of effect
            pass



g = GreenCardSetup()
g.card_selector()
print(g)