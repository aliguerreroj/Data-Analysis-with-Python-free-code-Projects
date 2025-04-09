"""
Las filas del conjunto de datos representan pacientes y las columnas representan información como medidas corporales, resultados de diversos análisis de sangre y estilos de vida. 
Utilizará el conjunto de datos para explorar la relación entre las enfermedades cardíacas, las medidas corporales, los marcadores sanguíneos y los estilos de vida.

Nombre del archivo: medical_examination.csv

Instrucciones
Cree un gráfico similar a examples/Figure_1.png, donde mostramos los recuentos de resultados positivos y negativos para las variables 
colesterol, glucosa, alcohol, actividad física y tabaquismo para pacientes con cardio=1 y cardio=0 en diferentes paneles.

Para cada número del archivo medical_data_visualizer.py, agregue el código del número de instrucción asociado a continuación.

Importe los datos de medical_examination.csv y asígnelos a la variable df.
Agregue una columna de sobrepeso a los datos. Para determinar si una persona tiene sobrepeso, primero calcule su IMC dividiendo su peso en kilogramos por el cuadrado de su altura en metros. 
Si ese valor es > 25, la persona tiene sobrepeso. Utilice el valor 0 para NO tener sobrepeso y el valor 1 para sobrepeso.

Normalice los datos estableciendo que 0 siempre sea bueno y 1 siempre malo. Si el valor de colesterol o glucosa es 1, establezca el valor en 0. 
Si el valor es mayor que 1, establezca el valor en 1.

Dibuje el gráfico categórico en la función draw_cat_plot.
Cree un DataFrame para el gráfico cat usando pd.melt con los valores de colesterol, glucosa, tabaquismo, alcohol, actividad física y sobrepeso en la variable df_cat.
Agrupe y reformatee los datos en df_cat para dividirlos por cardio. Muestre los recuentos de cada característica. 
Deberá cambiar el nombre de una de las columnas para que el gráfico cat funcione correctamente.

Convierta los datos a formato largo y cree un gráfico que muestre los recuentos de valores de las características categóricas utilizando el siguiente método proporcionado por la biblioteca seaborn import: sns.catplot().
Obtenga la figura para la salida y almacénela en la variable fig. No modifique las dos líneas siguientes.
Dibuje el mapa de calor con la función draw_heat_map.

Limpie los datos de la variable df_heat filtrando los siguientes segmentos de pacientes que representan datos incorrectos:
La presión diastólica es mayor que la sistólica (Mantenga los datos correctos con (df['ap_lo'] <= df['ap_hi']))
La estatura es menor que el percentil 2,5 (Mantenga los datos correctos con (df['height'] >= df['height'].quantile(0.025)))
La estatura es mayor que el percentil 97,5
El peso es menor que el percentil 2,5
El peso es mayor que el percentil 97,5
Calcule la matriz de correlación y almacénela en la variable corr.
Genere una máscara para el triángulo superior y almacénela en la variable mask.
Configure la figura de matplotlib. Grafique la matriz de correlación utilizando el método proporcionado por la biblioteca seaborn import: sns.heatmap().
No modifique las dos líneas siguientes.
Desarrollo
Escriba su código en medical_data_visualizer.py. Para desarrollo, puede usar main.py para probar su código.

Pruebas
Las pruebas unitarias de este proyecto se encuentran en test_module.py. Importamos las pruebas de test_module.py a main.py para su comodidad.
"""



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = None

# 2
df['overweight'] = None

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
