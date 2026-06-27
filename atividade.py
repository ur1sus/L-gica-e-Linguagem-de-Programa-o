tarefas = ["estudar", "treinar", "entregar trabalho"]

def f1(x):
    for i in x:
        print(i)

def coisa(x):
    return len(x)

def calc(x):
    if len(x) == 0:
        return "vazio"
    return x[0]

print("lista:")
f1(tarefas)
print("qtd:", coisa(tarefas))
print("primeira:", calc(tarefas))

--------------------------------------------
# Exibe todas as tarefas da lista
def f1(x):
    for i in x:
        print(i)

# Retorna a quantidade de tarefas
def coisa(x):
    return len(x)

# Retorna a primeira tarefa da lista.
# Se a lista estiver vazia, retorna "vazio".
def calc(x):
    if len(x) == 0:
        return "vazio"
    return x[0]
-----------------------------------------------
tarefas = ["estudar", "treinar", "entregar trabalho"]

def exibir_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print(tarefa)

def contar_tarefas(lista_tarefas):
    return len(lista_tarefas)

def obter_primeira_tarefa(lista_tarefas):
    if len(lista_tarefas) == 0:
        return "vazio"
    return lista_tarefas[0]

print("lista:")
exibir_tarefas(tarefas)
print("quantidade:", contar_tarefas(tarefas))
print("primeira tarefa:", obter_primeira_tarefa(tarefas))
-------------------------------------------------

