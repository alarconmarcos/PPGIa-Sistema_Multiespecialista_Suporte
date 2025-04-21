
import random

class GeradorDeTarefa(object):

    def __init__(self, mesa_bancada):
        self.Bancada = mesa_bancada

    def funcionamento_normal(self):
        return 'Verificou que o computador está funcionando perfeitamente!'

    def conectar_alimentacao(self):
        return 'Ligou o computador na tomada!'

    def fonte_queimada(self):
        return 'Trocou a fonte de energia porque estava queimada!'

    def circuito_de_alimentacao(self):
        return 'Diagnosticou que o circuito de alimentação da placa mãe estava estava com problema e encaminhou ao eletricista!'
    
    def fonte_com_problema(self):
        return 'Encaminhou a fonte de energia para a assistência porque estava com problema!'

    def checar_processador_e_memoria_ram(self):
        return 'Trocou a pasta térmica e passou borracha na memória ram e resolveu!'
    
    def problema_na_placa_mae(self):
        return 'Trocou a placa mãe porque estava com problema!'
    
    def hd_ou_ssd_desconectado_ou_com_defeito(self):
        return 'Conectou o cabo do HD que estava mal conectado!'
    
    def ajustar_boot(self):
        return 'Ajustou o boot do computador para inicializar pelo HD!'
    
    def substituir_hd_ou_ssd(self):
        return 'Substituiu o HD por um novo!'
    
    def imagem_so_corrompida(self):
        return 'Reinstalou o sistema operacional porque a imagem estava corrompida!'
    
   
    def adicionaTarefa(self):
        self.Bancada.adicionaTarefa('funcionamento_normal', self.funcionamento_normal())
        self.Bancada.adicionaTarefa('conectar_alimentacao', self.conectar_alimentacao())
        self.Bancada.adicionaTarefa('fonte_queimada', self.fonte_queimada())
        self.Bancada.adicionaTarefa('circuito_de_alimentacao', self.circuito_de_alimentacao())
        self.Bancada.adicionaTarefa('fonte_com_problema', self.fonte_com_problema())
        self.Bancada.adicionaTarefa('checar_processador_e_memoria_ram', self.checar_processador_e_memoria_ram())
        self.Bancada.adicionaTarefa('problema_na_placa_mae', self.problema_na_placa_mae())
        self.Bancada.adicionaTarefa('hd_ou_ssd_desconectado_ou_com_defeito', self.hd_ou_ssd_desconectado_ou_com_defeito())
        self.Bancada.adicionaTarefa('ajustar_boot', self.ajustar_boot())
        self.Bancada.adicionaTarefa('substituir_hd_ou_ssd', self.substituir_hd_ou_ssd())
        self.Bancada.adicionaTarefa('imagem_so_corrompida', self.imagem_so_corrompida())
    