import pandas as pd

class DataExtractor:
    def __init__(self) -> None:
        pass
    
    def get_df_from_csv(self, path_to_csv):
        print('Trying to read... ', path_to_csv)
        return pd.read_csv(path_to_csv)