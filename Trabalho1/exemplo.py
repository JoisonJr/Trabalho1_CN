import numpy as np
import matplotlib.pyplot as plt
# importa todas as funções de funcoes_basicas
from funcoes_basicas import *

# A função f(x) para a qual queremos encontrar o zero
def f(x):
    return x**3 - 5*x**2 + 8*x - 4

def df(x):
    return 3*x**2 - 10*x + 8

# Definir os parâmetros
tolerancia = 1e-6
max_iteracoes = 100

"""
# Usar a nova função para definir os valores de 'a' e 'b'
a, b = encontrar_intervalo(f, ponto_inicial=1, passo=0.5)

# --- Execução e Visualização ---
if a is not None and b is not None:
    print(f"Intervalo inicial encontrado: [{a}, {b}]")
    raiz, pontos_medios = falsa_posicao(f, a, b, tol=tolerancia, max_iter=max_iteracoes)

    if raiz is not None:
        # Gerar pontos para plotar a curva da função
        x_vals = np.linspace(a - 0.5, b + 0.5, 400)
        y_vals = f(x_vals)

        plt.figure(figsize=(12, 15))
        plt.plot(x_vals, y_vals, label='f(x) = $x^3 - 3$', color='blue')
        
        # Adicionar a linha do eixo x (onde f(x) = 0)
        plt.axhline(0, color='black', linestyle='--')
        
        # Plotar os pontos de cada iteração para mostrar a convergência
        plt.plot(pontos_medios, [f(p) for p in pontos_medios],  
                 'ro', label='Iterações do Método')
        
        # Marcar a raiz encontrada
        plt.plot(raiz, f(raiz), 'go', markersize=10, label='Raiz Encontrada')

        plt.title('Falsa posição', fontsize=16)
        plt.xlabel('Eixo X')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.show()
"""

raiz, iteracoes = newton_raphson(f, df, 3, tol=tolerancia, max_iter=max_iteracoes)

if raiz is not None:
    # Gerar pontos para plotar a curva da função
    x_vals = np.linspace(min(iteracoes) - .5, max(iteracoes) + .5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(12, 15))
    plt.plot(x_vals, y_vals, label='f(x) = $x^3 - 3$', color='blue')
    
    # Adicionar a linha do eixo x (onde f(x) = 0)
    plt.axhline(0, color='black', linestyle='--')
    
    # Plotar os pontos de cada iteração para mostrar a convergência
    plt.plot(iteracoes, [f(p) for p in iteracoes],  
                'ro', label='Iterações do Método')
    
    # Marcar a raiz encontrada
    plt.plot(raiz, f(raiz), 'go', markersize=10, label='Raiz Encontrada')

    plt.title('Falsa posição', fontsize=16)
    plt.xlabel('Eixo X')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
