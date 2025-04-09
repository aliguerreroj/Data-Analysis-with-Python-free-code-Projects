import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Datos reales',alpha=0.5)


    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Con la pendiente y la intersección, puedes predecir el nivel del mar para cualquier año futuro usando la
    X_prediction_all = np.arange(df['Year'].min(),2051)
    y_prediction_all =slope_all * X_prediction_all + intercept_all
    plt.plot(X_prediction_all,y_prediction_all,color='green',label="line go through the year 2050")


    # filtrar datos desde 2000
    df_recent = df[df['Year'] >= 2000] 
    slope_recent, intercept_recent,_,_,_ = linregress(df_recent['Year'],df_recent['CSIRO Adjusted Sea Level'])
    X_recent_all =np.arange(2000,2051)
    y_recent_all =slope_recent * X_recent_all + intercept_recent
    plt.plot(X_recent_all,y_recent_all,color='red',label="line from year 2000 through the most recent year")




    # Etiquetas y título
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # # Mostrar gráfico
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()
