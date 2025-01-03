import kagglehub

# Download latest versionsource kaggle_env/bin/activate
path = kagglehub.dataset_download("suddharshan/retail-price-optimization")

print("Path to dataset files:", path)

import shutil

# Specify the source file and destination folder
source_file = "/Users/karthikeyanmahendran/.cache/kagglehub/datasets/suddharshan/retail-price-optimization/versions/2/retail_price.csv"
destination_folder = "/Users/karthikeyanmahendran/Documents/2. Learning/price_optimization/data/raw/"

# Copy the file to the destination folder
shutil.copy(source_file, destination_folder)

print(f"File copied from {source_file} to {destination_folder}")
