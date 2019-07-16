from random import randint
class BlueCardSetup():
    card_type = 'Purple'

    def __init__(self):
        self.cardlist = [self.Purple01]
    def card_selector(self):
        card_id = randint(1,len(self.cardlist))
        card = [x for x in self.cardlist if card_id == x.id][0]
        return print(card())

    class purpleCards():

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

    class Purple01(purpleCards):

        """The great and terrible Mr. Moon! Disrupts the tides and summons werewolves across the map!
        Not made of cheese! Maybe made of cheese!"""
        id = 1

        def __init__(self):
            super().__init__()
            self.card_title = 'Mr. Moon'
            self.subtitle = 'Waxing and Waning'
            self.type = 'Wondertainment'
            self.stats = {'atk': 19, 'def': 20, 'hp': 20}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass