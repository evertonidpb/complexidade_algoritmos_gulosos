# kruskal.py
import os
import math
import time

class ConjuntosDisjuntos:
    """Estrutura Union-Find com União por Rank e Compressão de Caminho"""
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def make_set(self, u):
        self.pai[u] = u
        self.rank[u] = 0

    def find_set(self, u):
        if u != self.pai[u]:
            self.pai[u] = self.find_set(self.pai[u])  # Compressão de caminho
        return self.pai[u]

    def union(self, u, v):
        raiz_u = self.find_set(u)
        raiz_v = self.find_set(v)
        if raiz_u != raiz_v:
            if self.rank[raiz_u] > self.rank[raiz_v]:
                self.pai[raiz_v] = raiz_u
            else:
                self.pai[raiz_u] = raiz_v
                if self.rank[raiz_u] == self.rank[raiz_v]:
                    self.rank[raiz_v] += 1

def m_kruskal(n, arestas):
    """Executa o algoritmo de Kruskal e retorna o custo total da AGM"""
    A = []
    custo_total = 0
    
    subconjuntos = ConjuntosDisjuntos(n)
    for u in range(n):
        subconjuntos.make_set(u)
        
    # Ordenação gulosa das arestas pelo peso: O(M log M)
    arestas_ordenadas = sorted(arestas, key=lambda item: item[0])
    
    for peso, u, v in arestas_ordenadas:
        if subconjuntos.find_set(u) != subconjuntos.find_set(v):
            A.append((u, v))
            custo_total += peso
            subconjuntos.union(u, v)
            if len(A) == n - 1:  # Otimização: AGM de grafo conexo possui n-1 arestas
                break
                
    return custo_total

def carregar_instancia_kruskal(caminho_arquivo):
    """Lê o triângulo superior e converte diretamente em uma lista de arestas"""
    with open(caminho_arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f.read().splitlines() if linha.strip()]
        
    n = int(linhas[0].split()[0])
    arestas = []
    
    idx_linha = 1
    for i in range(n - 1):
        valores = [float(x) for x in linhas[idx_linha].split()]
        for idx_coluna, peso in enumerate(valores):
            j = i + 1 + idx_coluna
            arestas.append((peso, i, j))
        idx_linha += 1
        
    return n, arestas

if __name__ == '__main__':
    arquivos_teste = ['dij10.txt', 'dij20.txt', 'dij40.txt', 'dij50.txt']
    
    print("=" * 60)
    print("  TESTE DE DESEMPENHO ISOLADO: ALGORITMO DE KRUSKAL")
    print("=" * 60)
    
    # Busca inteligente do diretório de instâncias
    diretorios_pesquisa = ['instancias', '../instancias', '.']
    
    for nome_arq in arquivos_teste:
        caminho = None
        for d in diretorios_pesquisa:
            teste_caminho = os.path.join(d, nome_arq)
            if os.path.exists(teste_caminho):
                caminho = teste_caminho
                break
                
        if not caminho:
            print(f"Arquivo {nome_arq} não encontrado nas pastas de busca.")
            continue
            
        n, lista_arestas = carregar_instancia_kruskal(caminho)
        
        # Medição de tempo e desempenho
        inicio = time.perf_counter()
        custo_agm = m_kruskal(n, lista_arestas)
        fim = time.perf_counter()
        
        tempo_ms = (fim - inicio) * 1000
        
        print(f"Instância: {nome_arq:10} | Vértices: {n:3} | Custo AGM: {int(custo_agm):5} | Tempo: {tempo_ms:.4f} ms")
    print("=" * 60)