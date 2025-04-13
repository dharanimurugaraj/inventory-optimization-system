def optimize_restock(current_stock, predicted_demand, buffer=5):
    # Greedy logic: Restock only if stock < demand + buffer
    restock_qty = max(0, predicted_demand + buffer - current_stock)
    return restock_qty
