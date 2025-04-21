
import random
from AbstractEspecialista import AbstractEspecialista

# Estagiário 'é-um' AbstractEspecialista
class Estagiario(AbstractEspecialista):

    @property
    def eh_ativado(self):
        if 'ajustar_boot' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        elif 'fonte_queimada' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    @property
    def expertise(self):
        
        p = None
        if 'ajustar_boot' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('ajustar_boot')
            return ['ajustar_boot', p]
        elif 'fonte_queimada' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('fonte_queimada')
            return ['fonte_queimada', p]
    
    
    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)

