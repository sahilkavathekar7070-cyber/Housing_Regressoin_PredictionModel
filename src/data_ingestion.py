import pandas as pd
# Data Ingestion
def data_ingestion():
  '''
    * Title : Composite Cement Strength Prediction Model

    * Shape of Dataset : (1030, 10)

    * Dataset : Concrete_Data - Concrete_Data.csv

    * Independant Columns :['square_feet', 'bedrooms', 'bathrooms', 'age_years',
        'distance_to_city_center', 'garage_spaces', 'crime_rate_index',
        'school_rating', 'lot_size_sqft', 'renovation_year', 'hoa_fee_monthly']

    * Dependent Column :['price']
  '''
  df = pd.read_csv(r'C:\Housing_Regressoin_PredictionModel\data\housing_regression_dataset.csv')
  return df