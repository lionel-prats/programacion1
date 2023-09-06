# def funcion_de_ejemplo(valor_sin_iva = 100, iva = 21):
#     """ 
#     Indicar que hace
#     Que parametros recibe
#     Que devuelve 
#     """
#     resultado = valor_sin_iva * (1 + (iva / 100))
#     return resultado 

def calcula_precio_con_iva(valor_sin_iva:float = 100, iva:float = 21) -> float:
    """ 
    Calcula el precio con IVA a partir de un precio dado\n 
    Recibe 'precio' (defecto 100) e 'iva' (defecto 21)\n 
    Retorna el precio IVA incluído
    """
    resultado = valor_sin_iva * (1 + (iva / 100))
    return resultado 

print( calcula_precio_con_iva( iva = 50 ) )