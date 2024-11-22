prices = [7,1,2,1,3]

# loop through p and find the max delta from i onwards 

min_price = float('inf')
max_p = 0

for p in prices:
    if p < min_price:
        min_price = p
    
    profit = p - min_price 

    if profit > max_p:
        max_p = profit
    
print(max_p)