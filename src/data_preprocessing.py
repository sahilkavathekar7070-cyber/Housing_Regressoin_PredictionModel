# Step 2 : Data preprocessing and cleaning
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split

def data_preprocessing(df):
  '''
  Step 1  : Feature engineering and Feature selection

  Step 2 : Split the data into independent and dependent columns i.e X and y.

  Step 3 : Split the data into seen and unseen data i.e train and test data.

  Step 4 : Scaling / Normalizing data(Standard scaler, min max scaler, robust scaler)

  Step 5 : Return the seen and unseen data from the function
  '''

  # Step 1 : Feature Engineering and selection

  df['Price_per_sqft'] = df['price']/df['square_feet']

  # Step 2 : Split data into independent and denpendent Columns i.e X and y
  target_col = 'price'
  X = df.drop(columns = [target_col])
  y = df[target_col]

  # Step 3 : Split the data into seen and unseen data i.e train and test data

  X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                    test_size = 0.3,
                                                    random_state= 1)
  # Step 4 : Scaling and Normalizing data

  sc = RobustScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  # Step 5 : Return the seen and unseen data from the function
  return X_train,X_test,y_train,y_test
