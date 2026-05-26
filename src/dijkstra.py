# dijkstra.py
import os
import time

def m_dijkstra(V, matriz_adj, origem=0, destino=None):
    """
    Executa o algoritmo de Dijkstra para Caminho Mínimo.
    
    - chave[u]: Guarda o custo ACUMULADO mais barato para chegar a 'u' partindo da origem.
    - pai[u]: Guarda o vértice predecessor de 'u' no menor caminho.
    - em_Q: Vetor booleano que simula a Fila de Prioridades Q (True = pertence a Q).
    """
    if destino is None:
        destino = V - 1 # Conforme a Atividade 2, o destino é sempre o último vértice
        
    # 1. Inicialização
    chave = [float('inf')] * V
    pai = [None] * V
    
    # 2. Configura o gatilho da Origem (s)
    chave[origem] = 0
    
    # 3. Construção da Fila de Prioridades Q 
    em_Q = [True] * V
    
    # 4. Laço principal de captura
    for _ in range(V):
        
        # 5. Operação u = EXTRACT_MIN(Q)
        u = -1
        min_chave = float('inf')
        for i in range(V):
            if em_Q[i] and chave[i] < min_chave:
                min_chave = chave[i]
                u = i
                
        # Se não encontrar nenhum vértice alcançável (ou todos restantes são inatingíveis), interrompe
        if u == -1 or min_chave == float('inf'):
            break
            
        # Vértice 'u' sai da fila Q: sua menor distância definitiva foi encontrada!
        em_Q[u] = False
        
        #  Se o vértice que acabamos de "fechar" é o nosso destino,
        # não precisamos calcular o resto do grafo. O caminho mínimo até ele já está garantido.
        if u == destino:
            break
        
        # 6. Varredura da Vizinhança Adj[u]
        for v in range(V):
            peso_aresta = matriz_adj[u][v]
            
            # Se houver conexão real (peso válido) e não for um loop para si mesmo
            if peso_aresta != float('inf') and u != v:
                
                # 7. Regra:
                # O custo para chegar em 'v' passando por 'u' é o que foi gasto até 'u' + o peso da aresta
                custo_acumulado = chave[u] + peso_aresta
                
                # Se 'v' ainda estiver na fila e essa nova rota ACUMULADA for mais barata:
                if em_Q[v] and custo_acumulado < chave[v]:
                    # Atualiza as estruturas de controle 
                    pai[v] = u
                    chave[v] = custo_acumulado
                    
    # Retorna apenas o custo do caminho mínimo até o vértice de destino solicitado
    return chave[destino]

def carregar_instancia_dijkstra(caminho_arquivo):
    """
     Converte a matriz triangular superior do arquivo de texto
      em uma matriz de adjacência completa simétrica V x V.
    """
    with open(caminho_arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f.read().splitlines() if linha.strip()]
        
    V = int(linhas[0].split()[0]) 
    
    # Inicializa uma matriz preenchida com infinito
    matriz_adj = [[float('inf')] * V for _ in range(V)]
    
    idx_linha = 1
    for i in range(V - 1):
        valores = [float(x) for x in linhas[idx_linha].split()]
        for idx_coluna, peso in enumerate(valores):
            j = i + 1 + idx_coluna 
            matriz_adj[i][j] = peso
            matriz_adj[j][i] = peso 
        idx_linha += 1
        
    return V, matriz_adj

if __name__ == '__main__':
    arquivos_teste = ['dij10.txt', 'dij20.txt', 'dij40.txt', 'dij50.txt']
    diretorios_pesquisa = ['instancias', '../instancias', '.']
    
    linhas_saida = []
    
    # Cabeçalho de saída dos Resultados
    decoracao = "=" * 65
    linhas_saida.append(decoracao)
    linhas_saida.append("  EXECUÇÃO E VALIDAÇÃO ISOLADA: ALGORITMO DE DIJKSTRA")
    linhas_saida.append(decoracao)
    
    for l in linhas_saida:
        print(l)
        
    for nome_arq in arquivos_teste:
        caminho = None
        for d in diretorios_pesquisa:
            teste_caminho = os.path.join(d, nome_arq)
            if os.path.exists(teste_caminho):
                caminho = teste_caminho
                break
                
        if not caminho:
            msg_erro = f"Arquivo {nome_arq} não localizado nos diretórios padrão."
            print(msg_erro)
            linhas_saida.append(msg_erro)
            continue
            
        # Carrega os dados mapeados p/ a matriz simétrica
        V, matriz_adj = carregar_instancia_dijkstra(caminho)
        
        # O enunciado pede a origem em 0 e destino em V - 1
        origem = 0
        destino = V - 1
        
        # Medição de tempo de CPU
        inicio = time.perf_counter()
        custo_caminho = m_dijkstra(V, matriz_adj, origem=origem, destino=destino)
        fim = time.perf_counter()
        
        tempo_ms = (fim - inicio) * 1000
        
        # Formatação idêntica dos dados obtidos
        linha_res = f"Instância: {nome_arq:10} | Percurso: {origem}->{destino:<2} | Custo Caminho: {int(custo_caminho):5} | Tempo: {tempo_ms:.4f} ms"
        print(linha_res)
        linhas_saida.append(linha_res)
        
    linhas_saida.append(decoracao)
    print(decoracao)
    
    # Gravando a saída num arquivo de texto
    with open("resultado_dijkstra.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(linhas_saida) + "\n")
        
    print("\n[LOG] Execução finalizada com sucesso!")
    print("[LOG] O arquivo contendo os resultados foi gerado em: 'resultado_dijkstra.txt'")