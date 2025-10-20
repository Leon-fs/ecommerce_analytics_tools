def clean_data(df):
    """Cleans the input DataFrame by handling missing values and duplicates."""
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Fill missing values with the mean for numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    
    # Fill missing values with the mode for categorical columns
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

def normalize_data(df):
    """Normalizes numerical columns in the DataFrame."""
    from sklearn.preprocessing import MinMaxScaler
    
    scaler = MinMaxScaler()
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df

def preprocess_data(df):
    """Preprocesses the input DataFrame by cleaning and normalizing it."""
    df = clean_data(df)
    df = normalize_data(df)
    return df