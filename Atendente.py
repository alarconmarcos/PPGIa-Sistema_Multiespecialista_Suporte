
import random
from AbstractEspecialista import AbstractEspecialista

# Atendente 'é-um' AbstractEspecialista
class Atendente(AbstractEspecialista):

    # Testa se a especialidade do 'Atendente' está presente na lista de problemas a serem resolvidos
    @property
    def eh_ativado(self):
        if 'funcionamento_normal' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        elif 'conectar_alimentacao' in self.Bancada.estadoCompartilhado['problemas']: 
            return True
        else: 
            return False
    

    # implementação da expertise do 'Atendente'; como ele realiza sua tarefa
    @property
    def expertise(self):
        # Atribui mais de uma tarefa ao 'Atendente' para que ele possa realizar
        
        p = None
        if 'funcionamento_normal' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('funcionamento_normal')
            return ['funcionamento_normal', p]
        elif 'conectar_alimentacao' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('conectar_alimentacao')
            return ['conectar_alimentacao', p]
        

    # Quanto a realização da tarefa so Atendente contribui com o avanço geral da solução do problema.
    @property
    def progresso(self):
        return random.randint(1, 5)

    # Atualiza a bancada com a contribuição do 'Atendente'
    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
