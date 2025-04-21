

# Controla o acesso de cada especialista ao quadro-negro para pegar uma tarefa da
# lista 'instancias-de-problemas', chama cada especialista a contribuir e
# adiciona o resultado/contribuição na lista de contribuições do quadro-negro.
class Controlador(object):

    def __init__(self, mesa_bancada, GeradorDeTarefa, limite = 120):
        self.Bancada = mesa_bancada
        self.GeradorDeTarefa = GeradorDeTarefa
        self.limite = limite    # limite para interrompter o fanção loop

    # def loop(self):
    #     while self.Bancada.estadoCompartilhado['progresso'] < self.limite:
    #         self.GeradorDeTarefa.adicionaTarefa()   # gera e adiciona tarefas no quadro-negro
    #         self.Bancada.mostraTarefas()        # mostra a lista de tarefas a resolver
    #         for especialista in self.Bancada.especialistas:
    #             if especialista.eh_ativado:         # testa se o especialista está ativo
    #                 especialista.contribui()        # chama o especialista a contribuir.
    #     # retorna todas as contribuições postadas no quadro-negro pelos especialistas.
    #     return self.Bancada.estadoCompartilhado['contribuicoes']

    def loop(self):
        while self.Bancada.estadoCompartilhado['progresso'] < self.limite:
            self.GeradorDeTarefa.adicionaTarefa()
       #     self.Bancada.mostraTarefas()
            for especialista in self.Bancada.especialistas:
                if especialista.eh_ativado:
                    especialista.contribui()
        return self.Bancada.estadoCompartilhado['contribuicoes']
