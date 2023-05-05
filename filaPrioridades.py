import heapq
from collections import deque

fila_prioridades = []
fila_em_preparo = deque()

def adicionar_grupo():
    nome = input("Digite o nome da reserva: ")
    qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
    tempo_preparo = int(input("Digite o tempo de preparo: "))
    if len(fila_prioridades) == tam_fila:
        print("A fila está lotada!")
    else:
        heapq.heappush(fila_prioridades, (qtd_pessoas, tempo_preparo, nome))
        print("Grupo adicionado com sucesso!")

def mostrar_proximo_grupo():
    if len(fila_prioridades) > 0:
        grupo = fila_prioridades[0]
        print("Próximo grupo aguardando: ", grupo)
    else:
        print("Não há grupos aguardando!")

def preparar_proxima_refeicao():
    if len(fila_prioridades) > 0:
        grupo = heapq.heappop(fila_prioridades)
        fila_em_preparo.append(grupo)
        print("Grupo", grupo[2], "está sendo preparado. Tempo estimado de espera:", grupo[1], "minutos.")
    else:
        print("Não há grupos para preparar!")

def entregar_refeicao():
    if len(fila_em_preparo) > 0:
        grupo = fila_em_preparo.popleft()
        print("Grupo", grupo[2], "sua refeição está pronta!")
    else:
        print("Não há refeições para entregar!")

opcao = 0
tam_fila = 0

while opcao != 6:
    print("\nEscolha uma opção:")
    print("1 - Definir tamanho da fila com prioridades")
    print("2 - Adicionar novo grupo na fila com prioridades")
    print("3 - Mostrar próximo grupo aguardando")
    print("4 - Preparar próxima refeição")
    print("5 - Entregar refeição")
    print("6 - Sair")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        tam_fila = int(input("Digite o tamanho da fila com prioridades: "))
    elif opcao == 2:
        adicionar_grupo()
    elif opcao == 3:
        mostrar_proximo_grupo()
    elif opcao == 4:
        preparar_proxima_refeicao()
    elif opcao == 5:
        entregar_refeicao()
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida!")
