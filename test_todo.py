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

