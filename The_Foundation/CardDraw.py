

from collections import defaultdict
from random import randint
from The_Foundation.Cards import BlackCards,BlueCards,GreenCards,OrangeCards,PurpleCards,RedCards,WhiteCards,YellowCards


class cardDraw:



    def __init__(self):
        PurpleCardSetup = PurpleCards.PurpleCardSetup
        WhiteCardSetup = WhiteCards.WhiteCardSetup
        GreenCardSetup = GreenCards.GreenCardSetup
        OrangeCardSetup = OrangeCards.OrangeCardSetup

        RedCardSetup = RedCards.RedCardSetup
        YellowCardSetup = YellowCards.YellowCardSetup
        BlackCardSetup = BlackCards.BlackCardSetup
        BlueCardSetup = BlueCards.BlueCardSetup

        self.cards = [PurpleCardSetup(), WhiteCardSetup(), GreenCardSetup(), YellowCardSetup(),
                 OrangeCardSetup(), RedCardSetup(), BlueCardSetup(), BlackCardSetup()]
        colors = ['Blue', 'Black', 'Red', 'Yellow', 'Orange', 'White', 'Purple', 'Green']
        self.colors = defaultdict(list)
        [self.colors[i].append(c) for i,c in enumerate(colors)]
        print(self.cards,self.colors)

    def random_draw(self):
        card_color = self.colors[randint(0,7)]
        print(card_color)
        drawn_card = [x.card_selector() for x in self.cards if x.card_type in card_color][0]
        print(drawn_card())



card = cardDraw()
card.random_draw()