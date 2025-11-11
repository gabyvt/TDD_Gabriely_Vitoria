class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        if not titulo:
            raise ValueError("O título não pode ser vazio.")
        if any(t["titulo"] == titulo for t in self.tarefas):
            raise ValueError("Já existe uma tarefa com esse título.")
        tarefa = {"titulo": titulo, "descricao": descricao, "status": "pendente"}
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["status"] = "concluída"
                return
        raise ValueError("Tarefa não encontrada.")
    
    def remover_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa["titulo"] == titulo:
                self.tarefas.remove(tarefa)
                return
        raise ValueError("Tarefa não encontrada.")


