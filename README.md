# # 📝 Gerenciador de Tarefas

Um gerenciador de tarefas simples, feito em Python, que roda direto no terminal. Projeto desenvolvido durante meus estudos do curso de Python.

## ✨ Funcionalidades

- Adicionar novas tarefas (todas começam com o status "Pendente")
- Listar todas as tarefas cadastradas, com o número e o status de cada uma
- Marcar uma tarefa como concluída
- Remover uma tarefa
- Avisos para opção inválida, número de tarefa inexistente e lista vazia

## 🚀 Como executar

**Pré-requisito:** ter o [Python 3](https://www.python.org/downloads/) instalado.

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o programa:

```bash
python gerenciadorTarefas.py
```

> Se você renomear o arquivo, use o novo nome no comando.

## 💻 Exemplo de uso

```
Menu
      1. Adicionar tarefa
      2. Listar tarefas
      3. Concluir tarefa
      4. Remover tarefa
      5. Sair
Escolha uma opção: 1
Digite a tarefa: Estudar Python

Escolha uma opção: 2
1. Tarefa: Estudar Python
   Status: Pendente

Escolha uma opção: 3
Digite o número da tarefa a ser concluída: 1
Tarefa concluída com sucesso!
```

## 📚 Conceitos praticados

- Listas e dicionários (cada tarefa é um dicionário dentro de uma lista)
- Laço `while` para manter o menu em execução
- Laço `for` com `enumerate`
- Condicionais (`if`, `elif`, `else`)
- Entrada e saída de dados com `input` e `print`


## 🗺️ Melhorias futuras

- [ ] Tratar entradas inválidas com `try/except`
- [ ] Organizar o código em funções
- [ ] Salvar as tarefas em um arquivo
- [ ] Listar apenas as tarefas pendentes
- [ ] Editar o nome de uma tarefa

## 🔧 Limitações conhecidas

- O programa encerra com erro se o usuário digitar letras onde se espera um número.
- As tarefas ficam apenas na memória: ao fechar o programa, elas são perdidas.

## 👩‍💻 Autora

Feito por **Beatriz Fagundes Cardoso**.
[LinkedIn](https://www.linkedin.com/in/beatriz-fag/) · [GitHub](https://github.com/beatrizfag06)
