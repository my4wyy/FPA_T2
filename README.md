# Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elemento

## descrição do projeto

este projeto implementa o algoritmo de seleção simultânea do maior e do menor elemento (maxmin select) em python, utilizando a abordagem de divisão e conquista. o objetivo é reduzir o número de comparações necessárias em relação à abordagem ingênua, garantindo uma execução eficiente.

## explicação do algoritmo

1. o problema é dividido em subproblemas menores.
2. cada subproblema é resolvido recursivamente.
3. os resultados são combinados para determinar o maior e o menor elementos da sequência.
4. o número de comparações é minimizado em relação a uma abordagem iterativa simples.

## explicação do código

o código está implementado no arquivo `main.py` e segue a estrutura:

```python
# implementação do algoritmo maxmin select

def max_min_select(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    elif high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])
    
    mid = (low + high) // 2
    min1, max1 = max_min_select(arr, low, mid)
    min2, max2 = max_min_select(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

if __name__ == "__main__":
    arr = [3, 1, 5, 2, 9, 8, 6]
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    print(f"menor elemento: {min_val}, maior elemento: {max_val}")
```

### passo a passo do código

1. **caso base**: se o array contiver um único elemento, ele é retornado como máximo e mínimo.
2. **caso com dois elementos**: o menor e o maior são determinados diretamente.
3. **divisão e conquista**:
   - o array é dividido ao meio.
   - recursivamente, os menores e maiores são encontrados em cada metade.
   - os resultados são combinados, retornando o menor dos mínimos e o maior dos máximos.

## como executar o projeto

### requisitos
- python 3.x instalado

### passos para execução

1. clone este repositório:
   ```bash
   git clone <url_do_repositorio>
   ```
2. acesse a pasta do projeto:
   ```bash
   cd <nome_da_pasta>
   ```
3. execute o código:
   ```bash
   python main.py
   ```

## estrutura do projeto

```
<maxmin_select>/
│── readme.md  # documentação do projeto
│── assets/
│   └── grafo.png  # diagrama da divisão e combinação
│── src/
│   └── main.py  # implementação do algoritmo maxmin select
│   └── TestMaxMinSelect.py  # testes do algoritmo maxmin select
```

## relatório técnico

### complexidade assintótica - contagem de operações

- cada divisão reduz o tamanho do problema pela metade.
- para `n` elementos:
  - o número de comparações é reduzido em relação à abordagem ingênua (`2n - 2`).
  - o total de comparações segue `3n/2 - 2`, resultando em `o(n)`.
  
para `n` elementos:
- ao dividir a sequência em dois subproblemas, cada um com `n/2` elementos, realizamos `2t(n/2)` chamadas recursivas.
- cada nível da recursão realiza no máximo `2` comparações adicionais por chamada.
- ao combinar os resultados dos subproblemas, realizamos apenas `2` comparações para encontrar o menor dos mínimos e o maior dos máximos.
- o número total de comparações para `n` elementos é aproximadamente `3n/2 - 2`, confirmando a complexidade `o(n)`.

### complexidade assintótica - teorema mestre

a relação de recorrência do algoritmo é:

```
t(n) = 2t(n/2) + o(1)
```

1. identificamos os valores:
   - `a = 2`, `b = 2`, `f(n) = o(1)`.
2. calculamos `log_b a = log_2 2 = 1`.
3. pelo teorema mestre, com `f(n) = o(n^c)`, onde `c = 0`, e comparando com `n^p`, onde `p = 1`, temos que `c < p`.
4. pelo primeiro caso do teorema mestre (`f(n) = o(n^p)` com `p > c`), a solução assintótica é `o(n)`.

como a complexidade `o(n)` é obtida diretamente do primeiro caso do teorema mestre, concluímos que o algoritmo mantém eficiência linear na busca pelo maior e menor elementos.

## gráfico de fluxo de controle

*será adicionado posteriormente*

## conclusão

o algoritmo maxmin select é uma abordagem eficiente para encontrar o maior e o menor elemento simultaneamente em uma sequência de números. sua estratégia de divisão e conquista reduz o número de comparações necessárias, tornando-o mais eficiente que a abordagem ingênua. o uso do teorema mestre confirma sua complexidade `o(n)`, garantindo bom desempenho mesmo para entradas grandes. a implementação recursiva segue um modelo claro e estruturado, sendo de fácil compreensão e manutenção.
