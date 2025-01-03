import numpy as np
import pandas as pd
from scipy.optimize import linprog

def optimize_price(df, coeff_df, price_change_range=0.1):
    """
    Optimizes product prices to maximize quantity sold based on price elasticity.

    Parameters:
    df (pandas.DataFrame): The original product data containing product price and quantity sold.
    coeff_df (pandas.DataFrame): The coefficients DataFrame with price elasticity and other parameters.
    price_change_range (float): The allowed percentage change in price (e.g., 0.1 for ±10%).

    Returns:
    pandas.DataFrame: The optimized prices and the estimated quantities sold.
    """
    
    # Extract required data from the coefficients DataFrame
    elasticity_coeff = coeff_df[coeff_df['Coefficient'] == 'unit_price']['Value'].values[0]
    base_prices = df['unit_price'].values
    quantities_sold = df['qty'].values

    # Define the objective function (negative because linprog minimizes)
    # We want to maximize the quantity, so we minimize the negative quantity
    objective = -quantities_sold

    # Define the bounds for each price change (±10%)
    price_lower_bound = base_prices * (1 - price_change_range)
    price_upper_bound = base_prices * (1 + price_change_range)

    # Constraints: Prices must lie within the ±10% range
    bounds = [(low, high) for low, high in zip(price_lower_bound, price_upper_bound)]

    # The demand change based on the price change
    # ΔQ = Elasticity × (ΔP / P)
    # To account for the price change, we will calculate the new quantity sold after price adjustments
    # Formulate the change in quantity due to price change as a linear constraint
    # ΔQ = elasticity_coeff * ((new_price - old_price) / old_price)
    
    # Prepare the linear constraints for price change in terms of ΔQ
    demand_change_constraints = []
    for i, base_price in enumerate(base_prices):
        # Coefficient for price change constraint for each product
        demand_change_constraints.append([0 if j != i else elasticity_coeff for j in range(len(base_prices))])
    
    # Prepare the bounds for the linear programming
    # Each price change must result in an increase in quantity sold or be neutral
    quantity_bounds = [0] * len(base_prices)
    
    # Solve the optimization problem using linprog
    result = linprog(c=objective, A_ub=demand_change_constraints, b_ub=quantity_bounds, bounds=bounds, method='highs')

    # Get the optimized prices
    optimized_prices = result.x

    # Estimate the optimized quantities sold based on the optimized prices
    estimated_quantities = quantities_sold * (1 + elasticity_coeff * (optimized_prices - base_prices) / base_prices)

    # Return the results in a DataFrame
    optimized_df = pd.DataFrame({
        'product_id': df['product_id'],
        'optimized_price': optimized_prices,
        'estimated_quantity_sold': estimated_quantities
    })

    return optimized_df
