from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'datos'
    players_per_group = None
    num_rounds = 1
    field_args = dict(
          choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal, blank=True, initial=1
        # choices=[[1, 'Completamente en desacuerdo'], [2, 'Parcialmente en desacuerdo'],
        #          [3, 'Ligeramente en desacuerdo'], [4, 'Ni acuerdo ni en desacuerdo'],
        #          [5, 'Ligeramente de acuerdo'], [6, 'Parcialmente de acuerdo'],
        #          [7, 'Completamente de acuerdo']], widget=widgets.RadioSelect, blank=True, initial=1
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        verbose_name='¿Cuál es tu edad?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Hombre', 'Mujer'],
        verbose_name='¿Cuál es tu género?',
        widget=widgets.RadioSelect)

    education = models.StringField(
        choices=['Secundaria completa', 'Universidad (pregrado)', 'Postgrado'],
        verbose_name='¿Cuál es tu nivel de educación formal alcanzado?',
        widget=widgets.RadioSelect)
    Q1 = models.IntegerField(label="Extrovertido, entusiasta", **Constants.field_args)
    Q2 = models.IntegerField(label="Crítico, conflictivo", **Constants.field_args)
    Q3 = models.IntegerField(label="Confiable, auto-disciplinado", **Constants.field_args)
    Q4 = models.IntegerField(label="Ansioso, fácil de enojar", **Constants.field_args)
    Q5 = models.IntegerField(label="Crítico, conflictivo", **Constants.field_args)
    Q6 = models.IntegerField(label="Abierto a nuevas experiencias", **Constants.field_args)
    Q7 = models.IntegerField(label="Reservado, tranquilo", **Constants.field_args)
    Q8 = models.IntegerField(label="Simpático, amable", **Constants.field_args)
    Q9 = models.IntegerField(label="Desorganizado, descuidado", **Constants.field_args)
    Q10 = models.IntegerField(label="Convencional, poco creativo", **Constants.field_args)