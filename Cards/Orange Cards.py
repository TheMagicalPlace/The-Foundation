from random import randint
class OrangeCardSetup():
    card_type = 'Orange'

    def __init__(self):
        pass
        self.cardlist = [self.Orange01,self.Orange02,self.Orange03,self.Orange04,
                         self.Orange05,self.Orange06,self.Orange07,self.Orange08
                         ,self.Orange09,self.Orange10]
    def card_selector(self):
        card_id = randint(1,len(self.cardlist))
        card = [x for x in self.cardlist if card_id == x.id][0]
        return print(card())

    class orangeCards():

        def __init__(self):
            self.card_type = 'BLUE'
            self.card_title = 'n/a'
            self.subtitle = 'n/a'
            self.type = []
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

    class Orange01(orangeCards):

        """Description: An ancient and mysterious creature that fell from the stars and broke the masquerade. Incredibly powerful."""
        id = 1

        def __init__(self):
            super().__init__()
            self.card_title = 'DEER'
            self.type = ['Anomaly', 'Unknown', 'Supreme Divine']
            self.stats = {'atk': 34, 'def': 28, 'hp': 40}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass


    class Orange02(orangeCards):

        """A multicolor, ethereal goat. Said to fill the dreams of its victims with incessant bleating. Impervious to physical attacks."""
        id = 2

        def __init__(self):
            super().__init__()
            self.card_title = 'Technicolor Dream Goat'
            self.type = ['Anomaly', 'Sentient', 'Animal']
            self.stats = {'atk': 2, 'def': 3, 'hp': 4}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Orange03(orangeCards):
        """ An old man with a penchant for the dramatic. Hasn’t worn anything other than sandals for a thousand years. Needs to get off his high horse."""
        id = 3

        def __init__(self):
            super().__init__()
            self.card_title = 'Mr. God'
            self.type = ['Anomaly', 'Sentient', 'Divine']
            self.stats = {'atk': 15, 'def': 8, 'hp': 23}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Orange04(orangeCards):
        """ Little statue people made of elements. Tend to engage in shenanigans. Legend has it they unite once a year to form a powerful Anart Mecha, but this is unconfirmed."""
        id = 4

        def __init__(self):
            super().__init__()
            self.card_title = 'A Bundle Of Golems'
            self.type = ['Anomaly', 'Sentient', 'Construct']
            self.stats = {'atk': 5, 'def': 8, 'hp': 5}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass


    class Orange05(orangeCards):
        """ A furious ball of plasma and gas with a specific hatred for Planet Earth. The reason for its rage is uncertain, though it is known that Alto Clef owes it $23.50."""
        id = 5

        def __init__(self):
            super().__init__()
            self.card_title = 'A Very Angry Star'
            self.type = ['Anomaly', 'Sentient', 'Divine']
            self.stats = {'atk': 24, 'def': 18, 'hp': 20}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass


    class Orange06(orangeCards):
        """ A ghastly former soldier turned into a living nightmare. Steals children for probably horrible reasons. Lives in an attic above the Darkness Between Dimensions."""
        id = 6

        def __init__(self):
            super().__init__()
            self.card_title = 'Corrosion Man'
            self.type = ['Anomaly', 'Sentient', 'Humanoid']
            self.stats = {'atk': 9, 'def': 9, 'hp': 9}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Orange07(orangeCards):
        """ An immensely long corgi. Used for public transportation. A very good boy."""
        id = 7

        def __init__(self):
            super().__init__()
            self.card_title = 'L-O-N-G C-O-R-G'
            self.type = ['Anomaly', 'Sentient', 'Animal']
            self.stats = {'atk': 3, 'def': 5, 'hp': 18}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Orange08(orangeCards):
        """A demon possessed by speed incarnate. Horrifying and unrelenting. All entities nearby lose -2 to DEF against psychological threats."""
        id = 8

        def __init__(self):
            super().__init__()
            self.card_title = 'Wretched Bovine Heart'
            self.type = ['Anomaly', 'Sentient', 'Biological']
            self.stats = {'atk': 17, 'def': 5, 'hp': 6}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Orange09(orangeCards):
        """Tricked Adam El Asem into eating from the Tree of Knowledge, freeing itself from its prison. Legends say the Wanderer’s Library is built on its back. Thinks it knows everything. Probably does."""
        id = 9

        def __init__(self):
            super().__init__()
            self.card_title = 'The Serpent'
            self.type = ['Anomaly', 'Sentient', 'Supreme Divine']
            self.stats = {'atk': 10, 'def': 35, 'hp': 45}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass

    class Orange10(orangeCards):
        """Tricked Adam El Asem into eating from the Tree of Knowledge, freeing itself from its prison. Legends say the Wanderer’s Library is built on its back. Thinks it knows everything. Probably does."""
        id = 10

        def __init__(self):
            super().__init__()
            self.card_title = 'The Serpent'
            self.type = ['Anomaly', 'Sentient', 'Construct']
            self.stats = {'atk': 4, 'def': 9, 'hp': 8}

        def effect_on_action(self):
            # TODO - implementation of effect
            pass
