
from time import sleep


def exit(): 
    print('Ok, saindo...')
    sleep(2)
    print('Programa encerrado!')

def listaTarefasUX(): 
    while True: 
        var_choice = input('Deseja utilizar a Lista de Tarefas? [S/N]: ')

        if var_choice.upper() == 'S': 
            lista_tarefas = []
            while True: 
                var_tarefas = input('Adicione uma tarefa: ')
                lista_tarefas.append(var_tarefas)

                var_continua = input('Deseja adicionar mais tarefas? [S/N]: ')

                if var_continua.upper() == 'N': 
                    break
            
            print('\n--- Lista de Tarefas ---')
            for idx, tarefa in enumerate(lista_tarefas, start=1):
                print(f'[{idx} - Tarefa]: {tarefa}')

            var_choice = input('Deseja remover alguma tarefa? [S/N]: ')

            if var_choice.upper() == 'S': 
                try:
                    idx_tarefa = int(input('Insira o número da tarefa que deseja remover: '))
                    if 1 <= idx_tarefa <= len(lista_tarefas):
                        tarefa_removida = lista_tarefas.pop(idx_tarefa - 1)
                        print(f'Tarefa "{tarefa_removida}" removida com sucesso')
                    else: 
                        print('Índice da tarefa inválido.')
                except ValueError:
                    print('Por favor, insira um número válido.')

            var_choice = input('Deseja continuar? [S/N]: ')
            if var_choice.upper() == 'N': 
                exit()
                break
        elif var_choice.upper() == 'N':
            exit()
            break
if __name__ == '__main__':
    listaTarefasUX()

