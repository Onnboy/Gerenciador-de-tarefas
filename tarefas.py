def valida_prioridade(prioridade):
    """Válida se a prioridade informada é válida"""
    prioridades_validas = {"Urgencia", "Alta", "Média", "Baixa"}
    return prioridade in prioridades_validas

def adiciona_tarefa(tarefas, nome, descricao, prioridade, categoria):
    """Adiciona uma nova tarefa a lista"""
    tarefa = {
        "Nome": nome,
        "Descrição": descricao,
        "Prioridade": prioridade,
        "Categoria": categoria,
        "Concluida": False
    }
    tarefas.append(tarefa)
    print(f"A tarefa '{nome}' inserida com sucesso!")

def listagem_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa foi encontrada!")
        return

    for i, tarefa in enumerate(tarefas, 1):
        status = "✔️" if tarefa['Concluida'] else "❌"
        print(f"{i}. {tarefa['Nome']} [{tarefa['Prioridade']}] - {status}")

def marcar_concluida(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['Concluida'] = True
        print(f"Tarefa '{tarefas[indice]['Nome']} | marcada como concluida!")
    else:
        print("Indice inválido!")

def exibir_por_categoria(tarefas, categoria):
    """Exibe tarefas de uma categoria em especifico"""
    filtradas = [t for t in tarefas if t['Categoria'].lower() == categoria.lower()]
    if not filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
    else:
        listagem_tarefas(filtradas)