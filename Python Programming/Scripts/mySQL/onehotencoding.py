from sklearn.preprocessing import OneHotEncoder  
encoder = OneHotEncoder()  
encoded = encoder.fit_transform(df[['category_column']])  
