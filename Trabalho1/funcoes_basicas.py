import numpy as np
import matplotlib.pyplot as plt

def encontrar_intervalo(f, ponto_inicial=0, passo=1.5, max_iter=100):
    """
    Busca um intervalo [a, b] para o método da bisseção, priorizando
    a busca por raízes positivas.
    """
    # 1. Tenta encontrar um intervalo positivo
    a = ponto_inicial
    b = ponto_inicial + passo
    for _ in range(max_iter):
        if np.sign(f(a)) * np.sign(f(b)) < 0:
            return a, b
        
        # Expande o intervalo para a direita
        a = b
        b += passo

    # 2. Se a busca positiva falhar, tenta no intervalo negativo
    a = ponto_inicial
    b = ponto_inicial - passo
    for _ in range(max_iter):
        if np.sign(f(a)) * np.sign(f(b)) < 0:
            return a, b
        
        # Expande o intervalo para a esquerda
        a = b
        b -= passo

    print("Não foi possível encontrar um intervalo com sinais opostos dentro do limite de iterações.")
    return None, None

################################################################################################################################
    
def metodo_bisseccao(f, a, b, tol=1e-6, max_iter=100):
    """
    Implementação do Método da Bisseção.

    Args:
        f (function): A função f(x).
        a (float): O limite inferior do intervalo.
        b (float): O limite superior do intervalo.
        tol (float): A tolerância para a raiz.
        max_iter (int): O número máximo de iterações.

    Returns:
        float: A raiz aproximada.
        list: Uma lista dos pontos médios calculados em cada iteração.
    """
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        print("O método da bisseção pode não funcionar. A função deve ter sinais opostos nos extremos do intervalo.")
        return None, []

    # Lista para armazenar os pontos médios para visualização
    pontos_medios = []
    
    for i in range(max_iter):
        c = (a + b) / 2.0
        pontos_medios.append(c)
        
        # Se a raiz for encontrada dentro da tolerância
        if np.abs(f(c)) < tol:
            print(f"Raiz encontrada em {c} após {i+1} iterações.")
            return c, pontos_medios
        
        # Atualiza o intervalo
        if np.sign(f(c)) * np.sign(f(a)) < 0:
            b = c
        else:
            a = c
            
    print(f"O método não convergiu após {max_iter} iterações. A última aproximação foi {c}")
    return c, pontos_medios

################################################################################################################################

def falsa_posicao(f, a, b, tol = 1e-6, max_iter = 100):
    # verifica a existência de algum zero no intervalo [a,b], ou seja, se f(a)*f(b)>=0, não há zeros no intervalo
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        print("Não existe zero nesse intervalo [a, b]")
        return None, []
    
    pontos_medios = []
    
    for i in range(max_iter):
        # "estabelece" o xi para a iteração
        xi=(a*f(b)-b*f(a))/(f(b)-f(a))
        # adiciona xi à lista dos números verificados
        pontos_medios.append(xi)
        # Se a raiz for encontrada dentro da tolerância
        if np.abs(f(xi)) < tol:
            print(f"Raiz encontrada em {xi} após {i+1} iterações.")
            return xi, pontos_medios
        
        # Atualiza o intervalo
        if np.sign(f(xi))* np.sign(f(a)) < 0:
            b = xi
        else:
            a = xi
            
    print(f"O método não convergiu após {max_iter} iterações. A última aproximação foi {xi}")
    return xi, pontos_medios

################################################################################################################################

def newton_raphson(f, df, x0, tol = 1e-6, max_iter = 100):
    # inicia a lista de valores com x0
    x_values = [x0]
        
    for i in range(max_iter):
        # verifica se a derivada é próxima de 0, para evitar uma possível divisão por 0
        if np.abs(df(x0)) < 1e-12:
            print(f"Divisão muito próxima de 0. A última aproximação foi {x0}")
            return x0, x_values
        
        # atualiza o valor de xplus1
        xPlus1 = x0-f(x0)/df(x0)
        # adiciona o valor de xk+1 à lista
        x_values.append(xPlus1)

        # se o valor encontrado está abaixo da tolerância
        if np.abs(f(xPlus1)) < tol:
            print(f"Raiz encontrada em {xPlus1} após {i+1} iterações.")
            return xPlus1, x_values

        # atualiza x0
        x0 = xPlus1
        
    # caso não tenha sido encontrado um valor dentro da tolerância
    print(f"O método não convergiu após {max_iter} iterações. A última aproximação foi {xPlus1}")
    return xPlus1, x_values
