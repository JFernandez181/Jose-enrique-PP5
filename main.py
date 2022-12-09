"""
Jose Enrique Fernandez
22-0330
Refinando Código
En este programa refinariamos el codigo para mejor calidad.
"""

def precios():
    """ Devuelve una lista de costos del archivo gift_costs.txt"""
    with open('gift_costs.txt', 'r', encoding='UTF-8') as archivo:
        precios_regalos = list(archivo)
    precios_regalos = [int(c) for c in precios_regalos]  
    archivo.close()  
    return precios_regalos


def total(precios_regalos):
    """ Suma los precios de la lista de costos para conseguir un total"""
    total_price = 0
    for cost in precios_regalos:
        if cost > 1000:
            total_price += cost * 1.16  
        else:
            total_price += cost  

    return total_price


def main():
    """Función principal que llama ambas funciones e imprime el total"""
    print(total(precios()))

main()