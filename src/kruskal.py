import os
import math
import time

class ConjuntosDisjuntos:
    """
    Funções princpais para garantir a propriedade acíclica da AGM (Árvore Geradora Mínima):
    
    - MAKE-SET: Inicializa o conjunto unitário.
    - FIND-SET: Identifica o representante do conjunto (com compressão de caminho).
    - UNION: Une dois subconjuntos distintos baseado em suas alturas (União por Rank).
    
    """
    def __init__(self, tamanho_V):
        # Complexidade de espaço: O(V) - Aloca espaço para os arranjos de pais e ranks
        self.pai = list(range(tamanho_V))
        self.rank = [0] * tamanho_V

    def make_set(self, u):
        # Complexidade: O(1) - Define o próprio vértice como o líder de seu conjunto isolado
        self.pai[u] = u
        self.rank[u] = 0

    def find_set(self, u):
        # Complexidade: O(alpha(V)) - Quase constante devido à heurística de Compressão de Caminho
        if u != self.pai[u]:
            self.pai[u] = self.find_set(self.pai[u]) # Recursão inteligente que encurta a árvore
        return self.pai[u]

    def union(self, u, v):
        # Complexidade: O(alpha(V)) - Conecta duas árvores pendurando a menor na maior (heurística de Rank)
        raiz_u = self.find_set(u)
        raiz_v = self.find_set(v)
        if raiz_u != raiz_v:
            if self.rank[raiz_u] > self.rank[raiz_v]:
                self.pai[raiz_v] = raiz_u
            else:
                self.pai[raiz_u] = raiz_v
                if self.rank[raiz_u] == self.rank[raiz_v]:
                    self.rank[raiz_v] += 1

def m_kruskal(V, A):
    """
    Executa o algoritmo de Kruskal, onde:
    - V: Representa o número de vértices |V|);
    - A: Conjunto de arestas/arcos do grafo;
    
    Complexidade Geral do Algoritmo: O(A log A) ou O(A log V)
    Dominada quase inteiramente pelo processo de ordenação das arestas.
    """
    AGM = [] # Arranjo que guardará as arestas selecionadas p/ formar a árvore
    custo_total = 0
    
    # 1. Inicialização: Cada vértice começa c/ seu próprio conjunto disjunto isolado.
    # Complexidade: O(V)
    subconjuntos = ConjuntosDisjuntos(V)
    for u in range(V):
        subconjuntos.make_set(u)
        
    # 2. Ordenação das arestas em ordem não decrescente de peso.
    # Complexidade: O(A log A)
    arestas_ordenadas = sorted(A, key=lambda item: item[0])
    
    # 3. Processamento das arestas e teste de ciclo
    # Complexidade: O(A * alpha(V)) onde alpha é a inversa de Ackermann (com crescimento desprezível)
    for peso, u, v in arestas_ordenadas:
        # Se os representantes de 'u' e 'v' forem diferentes, a aresta não fecha ciclo, então pode adicionar!
        if subconjuntos.find_set(u) != subconjuntos.find_set(v):
            AGM.append((u, v))
            custo_total += peso
            subconjuntos.union(u, v) # Une as componentes na estrutura Union-Find
            
            # Otimização: Uma árvore geradora sobre V nós possui exatamente V - 1 arestas.
            # Se atingirmos essa quantidade, podemos interromper o laço mais cedo.
            if len(AGM) == V - 1:
                break
                
    return custo_total

def carregar_instancia_kruskal(caminho_arquivo):
    """
    Processador da matriz triangular superior.
    Garante que a topologia seja mapeada p/ lista limpa de arestas sem duplicidade.
    """
    with open(caminho_arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f.read().splitlines() if linha.strip()]
        
    V = int(linhas[0].split()[0]) # Captura a ordem do grafo |V| definida na primeira linha
    A = [] # Lista estruturada no formato [(peso, u, v), ...]
    
    idx_linha = 1
    for i in range(V - 1):
        valores = [float(x) for x in linhas[idx_linha].split()]
        for idx_coluna, peso in enumerate(valores):
            j = i + 1 + idx_coluna # precisa para recuperar o índice correto da coluna
            A.append((peso, i, j))
        idx_linha += 1
        
    return V, A

if __name__ == '__main__':
    arquivos_teste = ['dij10.txt', 'dij20.txt', 'dij40.txt', 'dij50.txt']
    diretorios_pesquisa = ['instancias', '../instancias', '.']
    
    linhas_saida = []
    
    # Montagem da apresentação de resultados
    decoracao = "=" * 65
    linhas_saida.append(decoracao)
    linhas_saida.append("  EXECUÇÃO E VALIDAÇÃO ISOLADA: ALGORITMO DE KRUSKAL")
    linhas_saida.append(decoracao)
    
    # Imprime o cabeçalho inicial direto no prompt
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
            
        V, conjunto_A = carregar_instancia_kruskal(caminho)
        
        # Medição de tempo de CPU 
        inicio = time.perf_counter()
        custo_agm = m_kruskal(V, conjunto_A)
        fim = time.perf_counter()
        
        tempo_ms = (fim - inicio) * 1000
        
        # Formatação dos Resultados:
        linha_res = f"Instância: {nome_arq:10} | Vértices (|V|): {V:3} | Custo AGM: {int(custo_agm):5} | Tempo: {tempo_ms:.4f} ms"
        print(linha_res)
        linhas_saida.append(linha_res)
        
    linhas_saida.append(decoracao)
    print(decoracao)
    
    # Gravando a saída num arquivo de texto
    with open("resultado_kruskal.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(linhas_saida) + "\n")
        
    print("\n[LOG] Execução finalizada com sucesso!")
    print("[LOG] O arquivo contendo os resultados foi gerado em: 'resultado_kruskal.txt'")