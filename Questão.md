## Esse arquivo possui todas as funções relacionadas a reprodução dos cromossomos:
```python
import numpy as np
from random import randint
from Binary import Binary
from Cromossomo import Cromossomo

def getFilhos(pais, taxa_crossover, taxa_mutacao, lim_inf, lim_sup, func_obj, num_bits):
    validated = False
    while not(validated):
        g_1, g_2 = get_GenotipoFilhos(pais, taxa_crossover, taxa_mutacao)
        validated = isGenotipoValido(g_1, g_2, lim_inf, lim_sup)
    binary = Binary()
    cromo_1 = Cromossomo(binary.binToDec(g_1), func_obj, num_bits)
    cromo_2 = Cromossomo(binary.binToDec(g_2), func_obj, num_bits)
    return cromo_1, cromo_2
    
                     
def crossOverOnePoint(c_1, c_2, taxa_crossover):

    f_1 = c_1
    f_2 = c_2


    return f_1, f_2
    
def mutacao(filho, taxa_mutacao):    
    f_mutado = ''
    for g in filho:
        if np.random.rand()<= taxa_mutacao:
            if g == '0':
                f_mutado = f_mutado + '1'
            else:
                f_mutado = f_mutado + '0'
        else:
            f_mutado = f_mutado + g
    return f_mutado

    
def get_GenotipoFilhos(pais, taxa_crossover, taxa_mutacao):
    c_1 = pais[0].genotipo
    c_2 = pais[1].genotipo
    f_1, f_2 = crossOverOnePoint(c_1, c_2, taxa_crossover)
    f_1_mutado = mutacao(f_1, taxa_mutacao)
    f_2_mutado = mutacao(f_2, taxa_mutacao)
    return f_1_mutado, f_2_mutado            
    

def isGenotipoValido(g_1, g_2, lim_inf, lim_sup):
    binary = Binary()    
    return ((binary.binToDec(g_1) >= lim_inf) & (binary.binToDec(g_1) <= lim_sup)) & ((binary.binToDec(g_2) >= lim_inf) & (binary.binToDec(g_2) <= lim_sup))

```

### Uma das funções está incompleta. Identifique essa função e termine a sua implementação para que o código funcione corretamente.
