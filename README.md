# Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elemento

## Descrição do projeto

Este projeto implementa o algoritmo de seleção simultânea do maior e do menor elemento (maxmin select) em python, utilizando a abordagem de divisão e conquista. o objetivo é reduzir o número de comparações necessárias em relação à abordagem ingênua, garantindo uma execução eficiente.

## Explicação do algoritmo

1. O problema é dividido em subproblemas menores.
2. Cada subproblema é resolvido recursivamente.
3. Os resultados são combinados para determinar o maior e o menor elementos da sequência.
4. O número de comparações é minimizado em relação a uma abordagem iterativa simples.

## Explicação do código

O código está implementado no arquivo `main.py` e segue a estrutura:

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
    arr = [1, 7, 9, 2, 8, 4, 6, 5]
    minimum, maximum = maxmin_select(arr, 0, len(arr) - 1)
    print(f"menor elemento: {minimum}, maior elemento: {maximum}")
```

### Passo a passo do código

1. **Caso base**: Se o array contiver um único elemento, ele é retornado como máximo e mínimo.
2. **Caso com dois elementos**: O menor e o maior são determinados diretamente.
3. **Divisão e conquista**:
   - O array é dividido ao meio.
   - Recursivamente, os menores e maiores são encontrados em cada metade.
   - Os resultados são combinados, retornando o menor dos mínimos e o maior dos máximos.

## Como executar o projeto

### Requisitos
- python 3.x instalado

### Passos para execução

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

## Estrutura do projeto

```
<FPA_T2>/
│── readme.md  # documentação do projeto
│── assets/
│   └── diagrama.png  # diagrama da divisão e combinação
│── src/
│   └── main.py  # implementação do algoritmo maxmin select
│   └── TestMaxMinSelect.py  # testes do algoritmo maxmin select
```

## Relatório técnico

### Complexidade assintótica - contagem de operações

- Cada divisão reduz o tamanho do problema pela metade.
- Para `n` elementos:
  - O número de comparações é reduzido em relação à abordagem ingênua (`2n - 2`).
  - O total de comparações segue `3n/2 - 2`, resultando em `o(n)`.
  
Para `n` elementos:
- Ao dividir a sequência em dois subproblemas, cada um com `n/2` elementos, realizamos `2t(n/2)` chamadas recursivas.
- Cada nível da recursão realiza no máximo `2` comparações adicionais por chamada.
- Ao combinar os resultados dos subproblemas, realizamos apenas `2` comparações para encontrar o menor dos mínimos e o maior dos máximos.
- O número total de comparações para `n` elementos é aproximadamente `3n/2 - 2`, confirmando a complexidade `o(n)`.

### Complexidade assintótica - teorema mestre

A relação de recorrência do algoritmo é:

```
t(n) = 2t(n/2) + o(1)
```

1. Identificamos os valores:
   - `a = 2`, `b = 2`, `f(n) = o(1)`.
2. Calculamos `log_b a = log_2 2 = 1`.
3. Pelo teorema mestre, com `f(n) = o(n^c)`, onde `c = 0`, e comparando com `n^p`, onde `p = 1`, temos que `c < p`.
4. Pelo primeiro caso do teorema mestre (`f(n) = o(n^p)` com `p > c`), a solução assintótica é `o(n)`.

Como a complexidade `o(n)` é obtida diretamente do primeiro caso do teorema mestre, concluímos que o algoritmo mantém eficiência linear na busca pelo maior e menor elementos.

## Diagrama de divisão e combinação

![Diagrama da divisão e combinação](assets/diagrama.png)

## Conclusão

O algoritmo maxmin select é uma abordagem eficiente para encontrar o maior e o menor elemento simultaneamente em uma sequência de números. sua estratégia de divisão e conquista reduz o número de comparações necessárias, tornando-o mais eficiente que a abordagem ingênua. o uso do teorema mestre confirma sua complexidade `o(n)`, garantindo bom desempenho mesmo para entradas grandes. a implementação recursiva segue um modelo claro e estruturado, sendo de fácil compreensão e manutenção.
