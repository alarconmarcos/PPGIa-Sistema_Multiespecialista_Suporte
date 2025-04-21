#!/usr/bin/env python

from Bancada import Bancada
from Controlador import Controlador
from GeradorDeTarefa import GeradorDeTarefa
from Atendente import Atendente
from Estagiario import Estagiario
from EngenheiroEletrico import EngenheiroEletrico
from Suporte import Suporte
from Tecnico import Tecnico

if __name__ == '__main__':

    mesa_bancada = Bancada()
    GeradorDeTarefa = GeradorDeTarefa(mesa_bancada)

    mesa_bancada.adicionaEspecialista( Atendente(mesa_bancada) )
    mesa_bancada.adicionaEspecialista( Estagiario(mesa_bancada) )
    mesa_bancada.adicionaEspecialista( EngenheiroEletrico(mesa_bancada) )

    mesa_bancada.adicionaEspecialista( Suporte(mesa_bancada) )
    mesa_bancada.adicionaEspecialista( Tecnico(mesa_bancada) )

    contribuicoes = Controlador(mesa_bancada, GeradorDeTarefa, 120).loop()

    for x in contribuicoes:
        print(x)
