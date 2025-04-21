
class Bancada(object):

    def __init__(self):
        self.especialistas = []
        self.estadoCompartilhado = {'problemas' : ['funcionamento_normal','conectar_alimentacao','fonte_queimada','circuito_de_alimentacao','fonte_com_problema','checar_processador_e_memoria_ram','problema_na_placa_mae','hd_ou_ssd_desconectado_ou_com_defeito','ajustar_boot','imagem_so_corrompida','substituir_hd_ou_ssd'],
                                    'instancias-de-problemas' : {'funcionamento_normal' : [],
                                                                 'conectar_alimentacao' : [],
                                                                 'fonte_queimada' : [],
                                                                 'circuito_de_alimentacao' : [],
                                                                 'fonte_com_problema' : [],
                                                                 'checar_processador_e_memoria_ram' : [],
                                                                 'problema_na_placa_mae' : [],
                                                                 'hd_ou_ssd_desconectado_ou_com_defeito' : [],
                                                                 'ajustar_boot' : [],
                                                                 'substituir_hd_ou_ssd' : [],
                                                                 'imagem_so_corrompida' : []},
                                    'contribuicoes' : [],
                                    'progresso' : 0}

    def adicionaEspecialista(self, especialista):
        self.especialistas.append(especialista)

    def adicionaContribuicao(self, contribuicao):
        self.estadoCompartilhado['contribuicoes'] += contribuicao

    def atualizaProgresso(self, progresso):
        self.estadoCompartilhado['progresso'] += progresso

    def adicionaTarefa(self, tarefa, paramentros):
        self.estadoCompartilhado['instancias-de-problemas'][tarefa] = paramentros

    def pegaTarefa(self, tarefa):
        return self.estadoCompartilhado['instancias-de-problemas'][tarefa]

    def mostraTarefas(self):
        print('instancias-de-problemas',self.estadoCompartilhado['instancias-de-problemas'])
