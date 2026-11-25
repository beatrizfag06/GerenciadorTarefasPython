tarefa = {}
lista_tarefas = []

while True:
    print('''Menu
          1. Adicionar tarefa
          2. Listar tarefas
          3. Concluir tarefa
          4. Remover tarefa
          5. Sair''')
    
    resposta = int(input('Escolha uma opção: '))
    
    if resposta == 1:
        tarefa['nome'] = input('Digite a tarefa: ')
        tarefa['status'] = 'Pendente'
        lista_tarefas.append(tarefa.copy())
        tarefa.clear()
    
    elif resposta == 2:
        if len(lista_tarefas) == 0:
            print('Nenhuma tarefa cadastrada.')
        else:
            for i, item in enumerate(lista_tarefas):
                print(f'{i+1}. Tarefa: {item["nome"]}\n   Status: {item["status"]}')
            
    
    elif resposta == 3:
        indice = int(input('Digite o número da tarefa a ser concluída: ')) -1
        if 0 <= indice < len(lista_tarefas):
            lista_tarefas[indice]['status'] = 'Concluído'
            print('Tarefa concluída com sucesso!')
        else:
            print('Tarefa não encontrada.')

    elif resposta == 4:
        indice = int(input('Digite o número da tarefa a ser removida: ')) -1
        
        if 0 <= indice < len(lista_tarefas):
            lista_tarefas.pop(indice)
            print('Tarefa removida com sucesso!')
        else:
            print('Tarefa não encontrada.')

    elif resposta == 5:
        break
    
    elif resposta not in [1, 2, 3, 4, 5]:
        print('Opção inválida. Tente novamente.')
        
print('Programa encerrado.')