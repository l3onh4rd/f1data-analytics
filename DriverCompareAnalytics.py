from DataExtractor import DataExtractor
from plot.driver_compare_plot import gen_driver_compare_plot

class DriverCompareAnalytics():
    def __init__(self, season, driver1, driver2):
        self.__driver1 = driver1
        self.__driver2 = driver2
        self.__year = season
        data_extractor = DataExtractor()
        # read raw csv data
        self.__season_driver_data = data_extractor.get_df_from_csv('./data/f1db-races-driver-standings.csv')

    def set_driver1(self, driver):
        self.__driver1 = driver
    
    def set_driver2(self, driver):
        self.__driver2 = driver

    def set_drivers_to_compare(self, driver1, driver2):
        self.set_driver1(driver1)
        self.set_driver2(driver2)
    
    def get_driver_compare_data(self):
        # drop unnecessary columns
        season_driver_points = self.__season_driver_data.drop(columns=['raceId', 'positionDisplayOrder', 'positionNumber', 'positionText', 'positionsGained']) 
        # filter for requested drivers ans season
        season_driver1_points = season_driver_points[(season_driver_points['year'] == self.__year) & (season_driver_points['driverId'] == self.__driver1)]['points'].tolist()
        season_driver2_points = season_driver_points[(season_driver_points['year'] == self.__year) & (season_driver_points['driverId'] == self.__driver2)]['points'].tolist()

        if len(season_driver1_points) != len(season_driver2_points):
            return [1], [5]

        x = list(range(1, len(season_driver1_points) + 1))

        gained_points = []
        pre_round_points_driver1 = 0
        pre_round_points_driver2 = 0
        for driver1_point, driver2_point in zip(season_driver1_points, season_driver2_points):
            current_compare_points_driver1 = driver1_point - pre_round_points_driver1
            current_compare_points_driver2 = driver2_point - pre_round_points_driver2
            gained_points += [current_compare_points_driver1 - current_compare_points_driver2]
            pre_round_points_driver1 = driver1_point
            pre_round_points_driver2 = driver2_point
        
        return x, gained_points
    
    def generate_chart(self):
        x, y = self.get_driver_compare_data()
        return gen_driver_compare_plot(x, y, self.__driver1, self.__driver2)