

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importar los datos
df = pd.read_csv('medical_examination.csv')

# Agregar una columna de sobrepeso (IMC)
df['height'] = df['height'] / 100  # Convertir altura a metros
df['overweight'] = (df['weight'] / (df['height'] ** 2)) > 25  # IMC > 25 es sobrepeso
df['overweight'] = df['overweight'].astype(int)  # Convertir booleanos a 0 y 1

# Normalizar colesterol y glucosa (1 si es mayor que 1, 0 si es 1)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Función para crear el gráfico categórico
def draw_cat_plot():
    # Transformar el DataFrame usando pd.melt
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'alco', 'overweight', 'smoke', 'active'], 
        var_name='variable', value_name='value'
    )

    # Agrupar y reformatear los datos
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Renombrar columna
    # df_cat.rename(columns={'value': 'status'}, inplace=True)

    # Crear el gráfico categórico
    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar').fig
    # fig.set_axis_labels('Variable', 'Total')
    # fig.set_titles('Cardio = {col_name}')
    # fig.legend.set_title('Status')

    # Guardar la figura
    fig.savefig('catplot.png')
    return fig

draw_cat_plot()

# Función para crear el mapa de calor
def draw_heat_map():
    # Filtrar datos para limpiar datos incorrectos y valores atípicos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Presión diastólica no puede ser mayor que la sistólica
        (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) &  # Filtrar altura
        (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))    # Filtrar peso
    ]

    # Calcular matriz de correlación
    corr = df_heat.corr()

    # Crear una máscara para la parte superior del heatmap
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Crear el heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt='.1f', linewidths=0.5, ax=ax)

    # Guardar la figura
    fig.savefig('heatmap.png')

    return fig

draw_heat_map()

