
import random
from Estagiario import Estagiario

### Tecnico 'é-um' Estagiario
class Tecnico(Estagiario):


    # # Testa se a especialidade do 'Atendente' está presente na lista de problemas a serem resolvidos
    @property
    def eh_ativado(self):
        if 'hd_ou_ssd_desconectado_ou_com_defeito' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        elif 'substituir_hd_ou_ssd' in self.Bancada.estadoCompartilhado['problemas']: 
            return True
        elif 'checar_processador_e_memoria_ram' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        else: 
            return False
                                                                    
    # implementação da expertise do 'Atendente'; como ele realiza sua tarefa
    @property
    def expertise(self):
        p = None
        if 'hd_ou_ssd_desconectado_ou_com_defeito' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('hd_ou_ssd_desconectado_ou_com_defeito')
            return ['hd_ou_ssd_desconectado_ou_com_defeito', p]
        elif 'substituir_hd_ou_ssd' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('substituir_hd_ou_ssd')
            return ['substituir_hd_ou_ssd', p]
        elif 'checar_processador_e_memoria_ram' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('checar_processador_e_memoria_ram')
            return ['checar_processador_e_memoria_ram', p]

    
    

    # # Quanto a realização da tarefa so Atendente contribui com o avanço geral da solução do problema.
    # @property
    # def progresso(self):
    #     return random.randint(20, 50)
    
    ### função que implementar a contribuição do 'Tecnico'.
    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
