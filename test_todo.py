import pytest
from src.todo import ToDoList

def test_adicionar_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Estudar Python", "Ler sobre TDD")
    tarefas = todo.listar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"
    
def test_concluir_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Estudar", "Python básico")
    todo.concluir_tarefa("Estudar")
    assert todo.listar_tarefas()[0]["status"] == "concluída"
    
def test_remover_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Dormir", "descansar bem")
    todo.remover_tarefa("Dormir")
    assert len(todo.listar_tarefas()) == 0
    
def test_editar_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Ler livro", "Capítulo 1")
    todo.editar_tarefa("Ler livro", "Capítulo 2")
    tarefas = todo.listar_tarefas()
    assert tarefas[0]["descricao"] == "Capítulo 2"
    
def editar_tarefa(self, titulo, nova_descricao):
    for tarefa in self.tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["descricao"] = nova_descricao
            return
    raise ValueError("Tarefa não encontrada.")

def test_filtrar_tarefas_por_status():
    todo = ToDoList()
    todo.adicionar_tarefa("Tarefa 1", "desc 1")
    todo.adicionar_tarefa("Tarefa 2", "desc 2")
    todo.concluir_tarefa("Tarefa 1")

    concluidas = todo.filtrar_tarefas("concluída")
    pendentes = todo.filtrar_tarefas("pendente")

    assert len(concluidas) == 1
    assert len(pendentes) == 1
    assert concluidas[0]["titulo"] == "Tarefa 1"

