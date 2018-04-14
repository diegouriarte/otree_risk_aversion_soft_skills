from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'loteria'
    players_per_group = None
    num_rounds = 5
    loto_pay = {'1': [c(18), c(18)],
                '2': [c(14), c(26)],
                '3': [c(10), c(34)],
                '4': [c(6), c(42)],
                '5': [c(2), c(50)],
                '6': [c(-2), c(54)]
               }


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.coin = random.randint(1, 10)
           # p.set_payoff()

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    loteria = models.StringField(
        choices=['1', '2', '3', '4', '5', '6'],
        verbose_name='¿Cuál es su lotería seleccionada?',
        widget=widgets.RadioSelect)

    coin = models.IntegerField()

    def set_payoff(self):

        # determine the payoff of the user selection
        if self.coin in (1, 2, 3, 4, 5):
            self.payoff = Constants.loto_pay[self.loteria][0]
            #self.payoff = c(10)
        else:
            self.payoff = Constants.loto_pay[self.loteria][1]
            #self.payoff = c(100)

