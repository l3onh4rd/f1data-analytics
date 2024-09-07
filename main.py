from DataExtractor import DataExtractor

data_extractor = DataExtractor()
df = data_extractor.get_df_from_csv('./data/f1db-circuits.csv')

print(df)