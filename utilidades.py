def filtrar_tarefas_por_prioridade(tarefas, prioridade):
    """Filtra e exibe tarefas por prioridade"""
    filtradas = [t for t in tarefas if t['Prioridade'].lower() == prioridade.lower()]
    if not filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada")
    else:
        for tarefa in filtradas:
            print(f"- {tarefa['Nome']} [{tarefa['Categoria']}]")