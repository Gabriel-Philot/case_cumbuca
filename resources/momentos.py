import seaborn as sns
import matplotlib.pyplot as plt
import random


def momento(amostra, k, central=False):
    # Verifica se a amostra é vazia
    if len(amostra) == 0:
        raise ValueError("Amostra vazia!")
    
    n = len(amostra)
    media = sum(amostra) / n
    
    # Calcula o k-ésimo momento amostral
    if not central:
        soma = sum([(valor - media) ** k for valor in amostra])
        return round(soma / n, 2)
    
    # Calcula o k-ésimo momento central
    else:
        soma = sum([(valor - media) ** k for valor in amostra])
        variancia = sum([(valor - media) ** 2 for valor in amostra]) / n
        return round(soma / n if k % 2 == 0 else soma / n / variancia ** (k/2), 2)
    



def gerar_amostra(n, a, b):
    amostra = []
    for i in range(n):
        valor = random.uniform(a, b)
        amostra.append(valor)
    return amostra

def gerar_amostra_normalizada(n, a, b):
    amostra = []
    for i in range(n):
        valor = random.uniform(a, b)
        valor_norm = (valor - a) / (b - a)
        amostra.append(valor_norm)
    return amostra


def plot_moment(amostra, momento):
    plt.figure(figsize=(12, 8))
    sns.histplot(x=amostra, bins='auto', element='step')
    plt.axvline(momento, color='red', label=f'{momento}-ésimo momento')
    plt.legend()
    plt.xlabel('Frequência')
    plt.ylabel('Valor')
    plt.title('Distribuição da amostra')
    plt.show()