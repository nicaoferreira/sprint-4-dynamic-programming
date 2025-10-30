#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sprint 4 - Dynamic Programming DASA (FIAP)
# Programação Dinâmica aplicada ao controle de insumos em unidades de diagnóstico

# Integrantes:
# Dayana Ticona Quispe - RM 558023
# Luiz Felipe Motta da Silva - RM 559126
# Nicolas Lorenzo Ferreira da Silva - RM 557962
# Pedro Henrique Faim dos Santos - RM 557440
# Victoria Moura Miyamoto - RM 555474

import functools

dias = [1, 2, 3, 4, 5, 6, 7]
demanda = [5, 3, 6, 2, 4, 7, 3]
custo_reposicao = 2
custo_falta = 10
estoque_inicial = 5
capacidade_max = 10

def dp_recursivo(dia, estoque):
    if dia == len(dias):
        return 0
    menor_custo = float('inf')
    for reposicao in range(capacidade_max - estoque + 1):
        novo_estoque = estoque + reposicao - demanda[dia]
        if novo_estoque < 0:
            custo = custo_falta * abs(novo_estoque)
            novo_estoque = 0
        else:
            custo = custo_reposicao * reposicao
        total = custo + dp_recursivo(dia + 1, novo_estoque)
        menor_custo = min(menor_custo, total)
    return menor_custo

@functools.lru_cache(None)
def dp_memo(dia, estoque):
    if dia == len(dias):
        return 0
    menor_custo = float('inf')
    for reposicao in range(capacidade_max - estoque + 1):
        novo_estoque = estoque + reposicao - demanda[dia]
        if novo_estoque < 0:
            custo = custo_falta * abs(novo_estoque)
            novo_estoque = 0
        else:
            custo = custo_reposicao * reposicao
        total = custo + dp_memo(dia + 1, novo_estoque)
        menor_custo = min(menor_custo, total)
    return menor_custo


def dp_iterativa():
    n = len(dias)
    dp = [[float('inf')] * (capacidade_max + 1) for _ in range(n + 1)]
    for e in range(capacidade_max + 1):
        dp[n][e] = 0

    for dia in range(n - 1, -1, -1):
        for estoque in range(capacidade_max + 1):
            for reposicao in range(capacidade_max - estoque + 1):
                novo_estoque = estoque + reposicao - demanda[dia]
                if novo_estoque < 0:
                    custo = custo_falta * abs(novo_estoque)
                    novo_estoque = 0
                else:
                    custo = custo_reposicao * reposicao
                total = custo + dp[dia + 1][novo_estoque]
                dp[dia][estoque] = min(dp[dia][estoque], total)
    return dp[0][estoque_inicial]

if __name__ == "__main__":
    print("Resultado Recursivo:", dp_recursivo(0, estoque_inicial))
    print("Resultado Memoização:", dp_memo(0, estoque_inicial))
    print("Resultado Iterativo:", dp_iterativa())
