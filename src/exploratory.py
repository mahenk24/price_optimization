import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_overview(df):
    """
    Provides an overview of the dataset.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    
    Prints:
    - Basic information about the dataframe (data types, non-null counts).
    - Number of missing values for each column.
    - First few rows of the dataframe.
    """
    print("Data Overview:")
    print("\nBasic Information:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nFirst few rows:")
    print(df.head())

def summary_statistics(df):
    """
    Provides summary statistics for numeric columns in the dataframe.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    
    Prints:
    - Summary statistics for all numeric columns (mean, std, min, max, etc.).
    """
    print("Summary Statistics:")
    print(df.describe())

def numeric_distribution(df):
    """
    Plots the distribution of numeric columns in the dataframe.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    
    This function creates histograms with kernel density estimation (KDE) for each numeric column
    to visualize the distribution of the data.
    """
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f'Distribution of {col}')
        plt.show()

def correlation_heatmap(df):
    """
    Generates a heatmap of the correlation matrix for numeric columns (int and float).
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    
    This function visualizes the correlation between numeric variables in the dataset.
    The heatmap uses a color gradient to show the strength of the correlation.
    """
    # Select only numeric columns (int and float)
    numeric_df = df.select_dtypes(include=['number'])

    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()


def category_summary(df, category_col):
    """
    Provides category-wise summary statistics for a specified categorical column.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    category_col (str): The name of the categorical column to group by (e.g., 'product_category_name').
    
    Prints:
    - Aggregated statistics (mean and sum) for `qty`, `total_price`, `freight_price`, `unit_price`, 
      `product_score`, and `product_weight_g` for each category in the specified column.
    """
    print(f"Category-wise Summary for {category_col}:")
    category_groups = df.groupby(category_col).agg({
        'qty': ['mean', 'sum'],
        'total_price': ['mean', 'sum'],
        'freight_price': ['mean', 'sum'],
        'unit_price': ['mean'],
        'product_score': ['mean'],
        'product_weight_g': ['mean'],
    })
    print(category_groups)

def time_based_analysis(df):
    """
    Analyzes sales and quantity trends over time.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    
    This function aggregates the data by `month_year`, and then plots the total sales (`total_price`) 
    and total quantity sold (`qty`) over time. The trends are shown as line plots.
    """
    # Convert 'month_year' column to datetime format assuming the format is 'dd-mm-yyyy'
    df['month_year'] = pd.to_datetime(df['month_year'], format='%d-%m-%Y')
    
    # Optionally, extract the month and year to group by month-year
    df['month_year'] = df['month_year'].dt.to_period('M')
    
    # Convert the 'month_year' to timestamp for plotting (this step is necessary for compatibility with Matplotlib)
    df['month_year'] = df['month_year'].dt.to_timestamp()

    # Plot total sales and quantity sold over time
    plt.figure(figsize=(12, 6))
    monthly_sales = df.groupby('month_year').agg({'total_price': 'sum', 'qty': 'sum'}).reset_index()
    sns.lineplot(data=monthly_sales, x='month_year', y='total_price', label='Total Sales', color='blue')
    sns.lineplot(data=monthly_sales, x='month_year', y='qty', label='Quantity Sold', color='red')
    plt.title('Total Sales and Quantity Sold Over Time')
    plt.xlabel('Month-Year')
    plt.ylabel('Value')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()


def weekday_weekend_analysis(df):
    """
    Compares sales data for weekdays vs weekends.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe to analyze.
    
    This function groups the data by the `weekday` and `weekend` columns, then compares the total 
    sales and quantity sold for weekdays and weekends using bar plots.
    """
    # Grouping by weekday/weekend
    weekday_sales = df.groupby('weekday').agg({'total_price': 'sum', 'qty': 'sum'}).reset_index()
    weekend_sales = df.groupby('weekend').agg({'total_price': 'sum', 'qty': 'sum'}).reset_index()

    # Plotting comparisons
    plt.figure(figsize=(12, 6))
    sns.barplot(data=weekday_sales, x='weekday', y='total_price', color='blue', label='Weekday Sales')
    sns.barplot(data=weekend_sales, x='weekend', y='total_price', color='orange', label='Weekend Sales')
    plt.title('Sales Comparison: Weekday vs Weekend')
    plt.xlabel('Weekday/Weekend')
    plt.ylabel('Total Sales')
    plt.legend()
    plt.show()
