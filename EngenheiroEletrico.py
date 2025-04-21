
import random
from AbstractEspecialista import AbstractEspecialista

# Engenheiro Elétrico 'é-um' AbstractEspecialista
class EngenheiroEletrico(AbstractEspecialista):

    def eh_ativado(self):
        if 'circuito_de_alimentacao' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        elif 'problema_na_placa_mae' in self.Bancada.estadoCompartilhado['problemas']: 
            return True
        else: 
            return False

    @property
    def expertise(self):
        p = None
        if 'circuito_de_alimentacao' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('circuito_de_alimentacao')
            return ['circuito_de_alimentacao', p]
        elif 'problema_na_placa_mae' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaTarefa('problema_na_placa_mae')
            return ['problema_na_placa_mae', p]


    @property
    def progresso(self):
        return random.randint(20, 120)


    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
