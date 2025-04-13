def predict_demand(sales_history, window_size=3):
    # Simple moving average using sliding window
    if len(sales_history) < window_size:
        return sum(sales_history) // len(sales_history)
    
    demand = []
    for i in range(len(sales_history) - window_size + 1):
        window = sales_history[i:i+window_size]
        demand.append(sum(window) // window_size)
    return demand[-1]  # Predict next demand
