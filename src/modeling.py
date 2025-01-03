import pandas as pd
import statsmodels.api as sm
import yaml
from sklearn.preprocessing import LabelEncoder

def read_parameters(file_path):
    """
    Reads the model parameters from the parameters.yaml file.
    
    Parameters:
    file_path (str): Path to the parameters.yaml file.
    
    Returns:
    dict: A dictionary containing the parameters.
    """
    with open(file_path, 'r') as file:
        params = yaml.safe_load(file)
    return params

def price_elasticity_model(df, params_file):
    """
    Develops an econometric model to estimate price elasticity of a product.
    Uses price and product category as an interaction term.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe containing sales and pricing data.
    params_file (str): Path to the YAML file containing the model parameters.
    
    Returns:
    statsmodels.regression.linear_model.RegressionResultsWrapper: The fitted model.
    """
    # Read parameters from the parameter.yaml file
    params = read_parameters(params_file)
    
    # Label encode the product category column
    le = LabelEncoder()
    df['category_encoded'] = le.fit_transform(df['product_category_name'])
    
    # Define the interaction term using unit_price and category encoding
    df['interaction'] = df['unit_price'] * df['category_encoded']
    
    # Define dependent and independent variables
    X = df[[params['price_column'], 'interaction', 'category_encoded']]
    y = df[params['quantity_column']]
    
    # Add constant to the model
    X = sm.add_constant(X)
    
    # Fit the model
    model = sm.OLS(y, X)
    results = model.fit()
    
    # Output the summary of the model
    print(results.summary())
    
    return results
