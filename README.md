# 📝 Gerenciador de Tarefas (To-Do List)

Este projeto foi desenvolvido como parte da prática de **Desenvolvimento Guiado por Testes (TDD – Test-Driven Development)**, com foco em criar um sistema simples e funcional para gerenciamento de tarefas pessoais.

---

## 🎯 Objetivo

O propósito do projeto é aplicar os princípios de TDD na implementação de uma aplicação que permita:

- Adicionar novas tarefas com título e descrição.
- Listar todas as tarefas registradas.
- Marcar tarefas como concluídas.
- Remover tarefas da lista.
- Garantir validações básicas, como:
  - Impedir títulos vazios.
  - Evitar tarefas duplicadas.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **Pytest** – para criação e execução dos testes automatizados.

---

## 🧩 Estrutura do Projeto

TDD_Gabriely_Vitoria-1/
│
├── src/
│ └── todo.py # Implementação da classe ToDoList
│
├── tests/
│ └── test_todo.py # Testes automatizados com Pytest
│
├── .gitignore
├── README.md
└── requirements.txt # (opcional) dependências do projeto

--- 

## 🧠 Conceitos Aplicados

- O projeto seguiu o ciclo clássico do TDD:

RED – Escrever um teste que inicialmente falha.
GREEN – Implementar o código mínimo necessário para o teste passar.
REFACTOR – Refatorar o código, mantendo todos os testes aprovados.

--- 

## 📚 Boas práticas aplicadas:

-Implementar o projeto em etapas pequenas, com commits frequentes.
-Cada funcionalidade começa por um teste falho.
-Todos os testes devem estar passando ao final.
-Documentar o projeto explicando:
-Qual projeto foi escolhido
-Ferramenta de teste utilizada
-Como executar os testes



