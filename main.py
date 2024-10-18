from tarefas import (
    adiciona_tarefa, listagem_tarefas,
    marcar_concluida, exibir_por_categoria,
    valida_prioridade
)
from utilidades import filtrar_tarefas_por_prioridade

def mostra_a_linha():
    print("------------------------------------")

mostra_a_linha()
print("--- Gerenciador de Tarefas ---")
mostra_a_linha()

def menu():
    tarefas = []

    while True:
        print("1. Adicionar tarefa")
        print("2. Listar as tarefas")
        print("3. Filtrar tarefas por prioridade")
        print("4. Marcar Tarefa como Concluída")
        print("5. Exibir por Categoria")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            while True:
                prioridade = input("Prioridade: (Urgencia,Alta,Média,Baixa): ").lower()
                if valida_prioridade(prioridade): # Essa porra me confundiu de categoria pra prioridade kkkkk
                    break # Caso for válida saíra do loop.
            categoria = input("Categoria da tarefa: ")
            adiciona_tarefa(tarefas, nome, descricao, prioridade, categoria)
        
        elif escolha == "2":
            listagem_tarefas(tarefas)

        elif escolha == "3":
            prioridade = input("Filtragem por prioridades (Urgencia,Alta,Média,Baixa): ").lower()
            if valida_prioridade(prioridade):
                filtrar_tarefas_por_prioridade(tarefas, prioridade)
        
        elif escolha == "4":
            try:
                indice = int(input("Numero da tarefa para concluir: ")) - 1
                marcar_concluida(tarefas, indice)
            except ValueError:
                print("Entrada invalida! Digite um numero válido!")
        
        elif escolha == "5":
            categoria = input("Digite a categoria desejada: ")
            exibir_por_categoria(tarefas, categoria)

        elif escolha == "6":
            print("Encerrando o programa!")
            break
        
        else:
            print("Opção inválida ou não foi digitado! Tente novamente!")

if __name__ == "__main__":
    menu()