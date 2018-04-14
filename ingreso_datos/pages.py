from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class datos_personales(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender', 'education']


class soft_skills(Page):
    form_model = 'player'
    form_fields = ['Q1',
                   'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']



page_sequence = [
    datos_personales, soft_skills
]
