from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    # only display instruction in round 1
    def is_displayed(self):
        return self.subsession.round_number == 1


class LotoGame(Page):

    form_model = 'player'
    form_fields = ['loteria']

    def before_next_page(self):
        self.player.set_payoff()


# ******************************************************************************************************************** #
# *** CLASS RESULTS *** #
# ******************************************************************************************************************** #
class Results(Page):
    def vars_for_template(self):
        return {'low': Constants.loto_pay[self.player.loteria][0], 'high': Constants.loto_pay[self.player.loteria][1],
                }


class TotalResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        return {
            'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            #'paying_round': self.session.vars['paying_round'],
            'player_in_all_rounds': self.player.in_all_rounds(),
        }

page_sequence = [
    Instructions, LotoGame, Results, TotalResults
]

