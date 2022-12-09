"""
Jose Enrique Fernandez
22-0330
Refinando Código
En este programa refinariamos el codigo para mejor calidad.
"""


def precios():
    arc = open('gift_costs.txt', 'r')
    precios = list(arc)
    precios = [int(c) for c in precios]  
    arc.close()  
    return precios


def total(precios):
    total_price = 0
    for cost in precios:
        if cost > 1000:
            total_price += cost * 1.16  
        else:
            total_price += cost  

    return total_price


def main():
    print(total(precios()))
    

if __name__ == '_main_':
    main()