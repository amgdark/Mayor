# -*- coding: utf-8 -*-
from lettuce import step, world
import sys
sys.path.append('../')
from app.NumeroMayor import NumeroMayor

@step(u'Given: Que tengo los valores "([^"]*)" y "([^"]*)"')
def given_que_tengo_los_valores_group1_y_group2(step, num1, num2):
    numero = NumeroMayor()
    world.resultado = numero.obtiene_mayor(num1, num2)

@step(u'when: obtengo el mayor')
def when_obtengo_el_mayor(step):
    pass
@step(u'then: el resultado es "([^"]*)"')
def then_el_resultado_es_group1(step, esperado):
    assert world.resultado==esperado, 'No corresponde'