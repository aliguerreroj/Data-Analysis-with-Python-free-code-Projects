

import numpy as np

def calculate(lst:list) -> dict:
    
    if len(lst) != 9: 
        raise ValueError("List must contain nine numbers.")
    # list = [0,1,2,3,4,5,6,7,8]      
    matriz = np.array(lst).reshape(3,3)
    def calculate_matriz(func):
         return [
            func(matriz, axis=0).tolist(),   
            func(matriz, axis=1).tolist(),  
            func(matriz).item()             
        ]
            
    calculations = {
        'mean': calculate_matriz(np.mean),
        'variance': calculate_matriz(np.var),
        'standard deviation': calculate_matriz(np.std),
        'max': calculate_matriz(np.max),
        'min': calculate_matriz(np.min),
        'sum': calculate_matriz(np.sum)
    }
    return calculations

        


# list = [0,1,2,3,4,5,6,7,8]
# print(calculate(list))   
