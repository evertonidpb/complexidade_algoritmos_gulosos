# 🧠 Algoritmos Implementados

## 1. Algoritmo de Kruskal (`kruskal.py`)

### Objetivo
Encontrar a Árvore Geradora Mínima (AGM) de um grafo conectado ponderado.

### Abordagem
Estratégia gulosa baseada em arestas. O algoritmo ordena todas as arestas do grafo por peso crescente e as adiciona na árvore uma a uma, desde que não formem ciclos.

### Estrutura de Suporte
Utiliza uma implementação eficiente de **Conjuntos Disjuntos (Union-Find)** com as heurísticas de:
- União por Rank
- Compressão de Caminho

### Complexidade Assintótica
\[
O(m \log n)
\]

Onde:
- \(m\) = número de arestas
- \(n\) = número de vértices

A complexidade é dominada pelo custo da ordenação das arestas.

---

## 2. Algoritmo de Prim (`prim.py`)

### Objetivo
Encontrar a Árvore Geradora Mínima (AGM) expandindo um subgrafo a partir de um nó raiz.

### Abordagem
Estratégia gulosa baseada em vértices.

O algoritmo:
1. Começa em um nó inicial arbitrário (definido como `0`)
2. Em cada iteração, conecta à árvore existente o vértice externo mais próximo através da aresta de menor peso

### Estrutura de Suporte
- Matriz de adjacência reconstruída simetricamente
- Vetor de chaves de corte para priorização

### Complexidade Assintótica
\[
O(n^2)
\]

Implementação clássica com busca linear pelo mínimo, ideal para os grafos densos presentes nas instâncias.

---

## 3. Algoritmo de Dijkstra (`dijkstra.py`)

### Objetivo
Encontrar o Caminho Mínimo entre um nó origem e todos os demais nós do grafo (com pesos não-negativos).

### Abordagem
Estratégia gulosa baseada em relaxamento de arestas.

O algoritmo:
- Rastreia a menor distância acumulada desde a origem
- Considera a origem fixada no nó `0`
- Utiliza como destino final o último nó (`n - 1`)

### Complexidade Assintótica
\[
O(n^2)
\]

Utilizando busca em vetor.

---

# 🚀 Como Configurar e Executar

## 1. Clonar o Repositório e Configurar Ambiente

Abra o terminal e execute os comandos abaixo:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Entre na pasta do projeto
cd seu-repositorio

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/macOS:
source venv/bin/activate

```

### Nota Importante:
Certifique-se de baixar e colocar os arquivos de instância (dij10.txt, dij20.txt, etc.) dentro de uma pasta chamada instancias/ localizada na raiz do diretório do projeto.

# Execução dos Scripts

Cada arquivo possui sua própria lógica de leitura e execução de benchmarks, permitindo testes independentes.

```bash
# Testar o desempenho do algoritmo de Kruskal
python kruskal.py

# Testar o desempenho do algoritmo de Prim
python prim.py

# Testar o desempenho do algoritmo de Dijkstra
python dijkstra.py

```

# Tabela de Validação de Resultados
Ao executar os scripts, os custos impressos no console devem corresponder exatamente aos valores do gabarito oficial (resultados.txt).

```text

| Instância de Teste | Vértices (n) | Custo da AGM (Kruskal e Prim) | Custo do Caminho Mínimo (Dijkstra) |
| ------------------ | -----------: | ----------------------------: | ---------------------------------: |
| `dij10.txt`        |           10 |                          7072 |                               5183 |
| `dij20.txt`        |           20 |                         15238 |                               3190 |
| `dij40.txt`        |           40 |                         26615 |                               8928 |
| `dij50.txt`        |           50 |                         30424 |                               6764 |

```