
import seaborn as sns
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy import distance


def porcentagem_de_valores_nulos(dados, coluna=None):
    if coluna is None:
        # Retorna a porcentagem de valores nulos em todas as colunas
        nulos_total = dados.isna().sum().sum()
        total_valores = dados.size
        return (nulos_total / total_valores) * 100
    else:
        # Retorna a porcentagem de valores nulos em uma coluna específica
        nulos_coluna = dados[coluna].isna().sum()
        total_valores = dados[coluna].size
        return (nulos_coluna / total_valores) * 100


def pareto(df,col_valor):
    """
    Calcula o Pareto de um DataFrame com base nas colunas de nome e valor.

    Parâmetros:
        - df (pandas.DataFrame): DataFrame a ser analisado.
        - col_valor (str): nome da coluna com os valores dos itens.

    Retorno:
        pandas.DataFrame: DataFrame filtrado com os principais nomes que representam 80% do total dos valores.
    """
    # Ordena o DataFrame em ordem decrescente pelos valores
    df = df.sort_values(by=col_valor, ascending=False)

    # Calcula o total dos valores
    total = df[col_valor].sum()

    # Calcula a porcentagem cumulativa dos valores
    df['cumulative_perc'] = round(100 * df[col_valor].cumsum() / total,2)

    # Filtra apenas os itens que representam 80% do total dos valores
    filtro = df['cumulative_perc'] <= 83
    df_filtrado = df.loc[filtro].reset_index(drop=True)

    return df_filtrado



def plot_pareto(df, x_col, y_col, cumulative_col):
    """
    Plota o gráfico de Pareto para um DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame a ser plotado.
    x_col (str): Nome da coluna para o eixo x.
    y_col (str): Nome da coluna para o eixo y.
    cumulative_col (str): Nome da coluna para a porcentagem cumulativa.

    Returns:
    matplotlib.pyplot.Figure: Gráfico de Pareto.
    """

    # Cria o gráfico de barras e a linha para a porcentagem cumulativa
    fig, ax1 = plt.subplots(figsize=(20, 8))
    ax1.bar(df[x_col], df[y_col], color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.set_xlabel(x_col)
    ax1.set_ylabel(y_col, color='tab:blue')
    
    ax2 = ax1.twinx()
    ax2.plot(df[x_col], df[cumulative_col], color='tab:red', marker='o')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    ax2.set_ylabel('Porcentagem Cumulativa', color='tab:red')
    
    # Define o título do gráfico
    plt.title('Gráfico de Pareto')
    
    return fig



def limites_cidade(localizacao, raio_km):
    """
    Obtém as coordenadas do retângulo que circunscreve uma cidade ou endereço fornecido,
    com base em um raio especificado em quilômetros.

    Parâmetros:
        - localizacao (str): Cidade ou endereço desejado.
        - raio_km (float): Raio em quilômetros.

    Retorna:
        Tupla com os valores mínimos e máximos das latitudes e longitudes, respectivamente.
    """
    # Define um nome personalizado para a aplicação
    geolocator = Nominatim(user_agent="minha-aplicacao")
    # Obtém as coordenadas da cidade ou endereço fornecido
    local = geolocator.geocode(localizacao)
    lat = local.latitude
    lon = local.longitude
    # Calcula as coordenadas do retângulo que circunscreve a cidade
    km_per_degree_lat = distance.distance((lat, lon), (lat + 1, lon)).km
    km_per_degree_lon = distance.distance((lat, lon), (lat, lon + 1)).km
    north = lat + (raio_km / km_per_degree_lat)
    south = lat - (raio_km / km_per_degree_lat)
    east = lon + (raio_km / km_per_degree_lon)
    west = lon - (raio_km / km_per_degree_lon)
    # Retorna os valores mínimos e máximos das latitudes e longitudes
    return (south, north, west, east)