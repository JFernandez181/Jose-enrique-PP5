with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = [int(c) for c in gift_costs]  # convierte strings a int

total_price = 0
for cost in gift_costs:
    if cost > 1000:
        total_price += cost * 1.16  # agrega impuestos
    else:
        total_price += cost

print(total_price)