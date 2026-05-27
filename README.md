# Algoritmos Gulosos — Implementação e Avaliação

Este projeto apresenta implementações clássicas de algoritmos gulosos aplicados a problemas de grafos ponderados.

Os algoritmos desenvolvidos foram:

* Kruskal — Árvore Geradora Mínima (AGM)
* Prim — Árvore Geradora Mínima (AGM)
* Dijkstra — Caminho Mínimo

Todos os algoritmos foram implementados em Python, com foco em:

* Clareza didática;
* Fidelidade ao pseudocódigo clássico;
* Medição de desempenho;
* Leitura automatizada das instâncias;
* Geração de relatórios de saída.

---

# O que são Algoritmos Gulosos?

Algoritmos gulosos (Greedy Algorithms) são estratégias de resolução de problemas que tomam, a cada etapa, a melhor decisão local possível, esperando que essa escolha leve à solução ótima global.

Em problemas de grafos, essa abordagem é amplamente utilizada para:

* Encontrar Árvores Geradoras Mínimas;
* Encontrar Caminhos Mínimos;
* Reduzir custos acumulados;
* Construir soluções incrementais eficientes.

As implementações deste projeto seguem exatamente essa filosofia:

* Kruskal escolhe sempre a aresta mais barata disponível;
* Prim escolhe sempre o vértice mais barato para expandir a árvore;
* Dijkstra escolhe sempre o próximo vértice com menor custo acumulado.

---

# Estrutura do Projeto

```text
.
│   README.md
│
├── instancias/
│   ├── dij10.txt
│   ├── dij20.txt
│   ├── dij40.txt
│   └── dij50.txt
│
└── src/
    ├── dijkstra.py
    ├── kruskal.py
    └── prim.py
```

---

# Formato das Instâncias

Os algoritmos esperam arquivos `.txt` contendo grafos ponderados representados por matriz triangular superior.

Exemplo simplificado:

```text
4
1 3 4
2 5
6
```

Onde:

* A primeira linha representa o número de vértices `|V|`;
* As demais linhas representam os pesos das arestas do grafo.

Os scripts convertem automaticamente essa estrutura para:

* Lista de arestas (Kruskal);
* Matriz de adjacência simétrica (Prim e Dijkstra).

---

# 1. Algoritmo de Kruskal (`kruskal.py`)

## Objetivo

Encontrar a Árvore Geradora Mínima (AGM) de um grafo conectado ponderado.

---

## Estratégia Gulosa

O algoritmo:

1. Ordena todas as arestas por peso crescente;
2. Seleciona a aresta de menor custo disponível;
3. Adiciona a aresta somente se ela não formar ciclo;
4. Repete até formar a AGM.

---

## Estruturas Utilizadas

### Union-Find (Conjuntos Disjuntos)

A implementação utiliza:

* Compressão de Caminho;
* União por Rank.

Essas heurísticas reduzem drasticamente o custo das operações de união e busca.

---

## Complexidade

```text
O(A log A)
```

Onde:

* `A` = número de arestas;
* `V` = número de vértices.

A complexidade é dominada pela ordenação das arestas.

---

## Arquivo Gerado

Após a execução:

```text
resultado_kruskal.txt
```

---

# 2. Algoritmo de Prim (`prim.py`)

## Objetivo

Encontrar a Árvore Geradora Mínima expandindo um subgrafo a partir de um vértice raiz.

---

## Estratégia Gulosa

O algoritmo:

1. Começa no vértice `0`;
2. Mantém uma árvore parcial;
3. Seleciona sempre a aresta de menor peso que conecta a árvore a um vértice externo;
4. Expande a árvore até conectar todos os vértices.

---

## Estruturas Utilizadas

* Matriz de adjacência simétrica;
* Vetor de chaves (`chave`);
* Vetor de predecessores (`pai`);
* Vetor booleano simulando fila de prioridade (`em_Q`).

---

## Complexidade

```text
O(V²)
```

A implementação utiliza busca linear para encontrar o próximo vértice mínimo.

Essa abordagem é adequada para grafos densos.

---

## Arquivo Gerado

Após a execução:

```text
resultado_prim.txt
```

---

# 3. Algoritmo de Dijkstra (`dijkstra.py`)

## Objetivo

Encontrar o caminho mínimo entre o vértice origem e o vértice destino em grafos com pesos não negativos.

---

## Estratégia Gulosa

O algoritmo:

1. Inicializa a origem no vértice `0`;
2. Considera como destino o último vértice `(V - 1)`;
3. Seleciona sempre o vértice com menor custo acumulado;
4. Relaxa as arestas adjacentes;
5. Atualiza os menores caminhos encontrados.

---

## Estruturas Utilizadas

* Matriz de adjacência;
* Vetor de distâncias (`chave`);
* Vetor de predecessores (`pai`);
* Vetor booleano simulando fila de prioridade (`em_Q`).

---

## Complexidade

```text
O(V²)
```

A implementação utiliza busca linear no vetor de prioridades.

---

## Arquivo Gerado

Após a execução:

```text
resultado_dijkstra.txt
```

---

# Como Executar os Algoritmos

## 1. Clonar o Repositório

```bash
git clone https://github.com/evertonidpb/complexidade_algoritmos_gulosos.git
```

---

## 2. Entrar na Pasta

```bash
cd seu-repositorio
```

---

## 3. (Opcional) Criar Ambiente Virtual

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Preparação das Instâncias

Crie uma pasta chamada:

```text
instancias/
```

E coloque dentro dela os arquivos:

```text
dij10.txt
dij20.txt
dij40.txt
dij50.txt
```

Os scripts procuram automaticamente as instâncias nos diretórios:

* `instancias/`
* `../instancias/`
* diretório atual (`.`)

---

# Execução dos Testes

## Executar Kruskal

```bash
python kruskal.py
```

---

## Executar Prim

```bash
python prim.py
```

---

## Executar Dijkstra

```bash
python dijkstra.py
```

---

# O que será exibido na execução?

Cada algoritmo:

* Carrega automaticamente as instâncias;
* Executa os cálculos;
* Mede o tempo de execução;
* Exibe os resultados no terminal;
* Gera um arquivo `.txt` com o relatório.

Exemplo de saída:

```text
Instância: dij20.txt | Vértices (|V|): 20 | Custo AGM: 15238 | Tempo: 0.1532 ms
```

---

# Critérios de Validação

Os valores obtidos devem coincidir com os resultados esperados abaixo.

| Instância   | Vértices | AGM (Kruskal/Prim) | Caminho Mínimo (Dijkstra) |
| ----------- | -------: | -----------------: | ------------------------: |
| `dij10.txt` |       10 |               7072 |                      5183 |
| `dij20.txt` |       20 |              15238 |                      3190 |
| `dij40.txt` |       40 |              26615 |                      8928 |
| `dij50.txt` |       50 |              30424 |                      6764 |

---

# Observações Importantes

* Todos os grafos utilizados são ponderados;
* O algoritmo de Dijkstra pressupõe pesos não negativos;
* Prim e Kruskal devem gerar exatamente o mesmo custo de AGM;
* Os tempos de execução podem variar conforme o hardware utilizado;
* Os algoritmos foram implementados sem bibliotecas externas de grafos.

---

# Orientações para Avaliação

Para validar os algoritmos, recomenda-se:

1. Verificar se os arquivos de instância estão na pasta correta;
2. Executar cada script individualmente;
3. Comparar os custos gerados com a tabela oficial;
4. Confirmar a geração automática dos arquivos:

   * `resultado_kruskal.txt`
   * `resultado_prim.txt`
   * `resultado_dijkstra.txt`
5. Observar se o algoritmo executa sem erros para todas as instâncias.

---

# Considerações Finais

Os algoritmos implementados representam soluções clássicas da teoria dos grafos utilizando estratégias gulosas eficientes e amplamente utilizadas em Ciência da Computação.

O projeto demonstra:

* Manipulação de grafos;
* Estruturas clássicas de otimização;
* Uso de heurísticas eficientes;
* Análise de complexidade;
* Validação experimental de desempenho.
