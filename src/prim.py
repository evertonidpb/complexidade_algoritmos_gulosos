# prim.py
import os
import time

def m_prim(V, matriz_adj, raiz=0):
    """
    - chave[u]: Guarda o peso da aresta mais barata para conectar 'u' à árvore.
    - pai[u]: Guarda o vértice predecessor de 'u' na estrutura da árvore.
    - em_Q: Vetor booleano que simula a Fila de Prioridades Q (True = pertence a Q).

    """
    # 1. Inicialização
    chave = [float('inf')] * V
    pai = [None] * V
    
    # 2. Configura o gatilho da Raiz r 
    chave[raiz] = 0
    
    # 3. Construção da Fila de Prioridades Q 
    # True indica que o vértice ainda está na fila (do lado de fora da árvore)
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
                
        # Se não encontrar nenhum vértice alcançável, interrompe (grafo desconexo)
        if u == -1:
            break
            
        # Vértice 'u' sai da fila Q e passa a integrar a árvore
        em_Q[u] = False
        
        # 6. Varredura da Vizinhança Adj[u]
        for v in range(V):
            peso_aresta = matriz_adj[u][v]
            
            # Se houver conexão real (peso válido) e não for um loop para si mesmo
            if peso_aresta != float('inf') and u != v:
                
                # 7. Regra de Corte Gulosa
                # Se 'v' ainda estiver fora da árvore (na fila) e a nova rota for mais barata
                if em_Q[v] and peso_aresta < chave[v]:
                    # Atualiza as estruturas de controle 
                    pai[v] = u
                    chave[v] = peso_aresta
                    
    # O custo total da árvore é a soma exata das chaves acumuladas de quem foi conectado
    custo_total = sum(chave[i] for i in range(V) if chave[i] != float('inf'))
    return custo_total

def carregar_instancia_prim(caminho_arquivo):
    """
     Converte a matriz triangular superior do arquivo de texto
      em uma matriz de adjacência completa simétrica V x V.
    """
    with open(caminho_arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f.read().splitlines() if linha.strip()]
        
    V = int(linhas[0].split()[0]) # Captura a ordem do grafo |V|
    
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
    linhas_saida.append("  EXECUÇÃO E VALIDAÇÃO ISOLADA: ALGORITMO DE PRIM")
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
            
        # Carrega os dados mapeados para a matriz simétrica
        V, matriz_adj = carregar_instancia_prim(caminho)
        
        # Medição de tempo precisa de CPU
        inicio = time.perf_counter()
        custo_agm = m_prim(V, matriz_adj, raiz=0) # Raiz padrão iniciada em 0
        fim = time.perf_counter()
        
        tempo_ms = (fim - inicio) * 1000
        
        # Formatação idêntica dos dados obtidos
        linha_res = f"Instância: {nome_arq:10} | Vértices (|V|): {V:3} | Custo AGM: {int(custo_agm):5} | Tempo: {tempo_ms:.4f} ms"
        print(linha_res)
        linhas_saida.append(linha_res)
        
    linhas_saida.append(decoracao)
    print(decoracao)
    
    # Gravando a saída num arquivo de texto
    with open("resultado_prim.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(linhas_saida) + "\n")
        
    print("\n[LOG] Execução finalizada com sucesso!")
    print("[LOG] O arquivo contendo os resultados foi gerado em: 'resultado_prim.txt'")