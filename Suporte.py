
import random
from Atendente import Atendente

# Atendente 'é-um' Atendente
class Suporte(Atendente):

    # Testa se a especialidade do 'Atendente' está presente na lista de problemas a serem resolvidos
    @property
    def eh_ativado(self):
        if 'fonte_com_problema' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        elif 'imagem_so_corrompida' in self.Bancada.estadoCompartilhado['problemas']: 
            return True
        else: 
            return False
                                                                    


    # implementação da expertise do 'Atendente'; como ele realiza sua tarefa
    @property
    def expertise(self):
        p = None
        if 'fonte_com_problema' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('fonte_com_problema')
            return ['fonte_com_problema', p]
        elif 'imagem_so_corrompida' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('imagem_so_corrompida')
            return ['imagem_so_corrompida', p]



    # Quanto a realização da tarefa so Atendente contribui com o avanço geral da solução do problema.
    @property
    def progresso(self):
        return random.randint(5, 10)
    
    
    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
