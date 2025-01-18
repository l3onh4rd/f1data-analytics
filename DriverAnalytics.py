from DataExtractor import DataExtractor
from Standings import Standings
from plot import driver_points_plot

class DriverAnalytics(Standings):
    def __init__(self, year):
        self.__year = year

    def set_year(self, year):
        self.__year = year
    
    def get_driver_standings_data(self):
        data_extractor = DataExtractor()
        # read raw csv data
        season_driver_points = data_extractor.get_df_from_csv('./data/f1db-races-driver-standings.csv')
        # drop unnecessary columns
        season_driver_points = season_driver_points.drop(columns=['raceId', 'positionDisplayOrder', 'positionNumber', 'positionText', 'positionsGained']) 
        # filter for requested year
        season_driver_points = season_driver_points[season_driver_points['year'] == self.__year]
        # number of races
        rounds = season_driver_points['round'].max()
        # generate x values depending on number of races
        x = list(range(1, rounds + 1))
        # get a list of the teams for the constructors championchip
        drivers = season_driver_points[season_driver_points['round'] == 1]['driverId'].to_list()

        # generating y values (points for each team after each race)
        y = []
        for driver in drivers:
            y += [season_driver_points[season_driver_points['driverId'] == driver]['points'].to_list()]

        return x, y, drivers
    
    def generate_chart(self):
        x, y, drivers = self.get_driver_standings_data()
        return driver_points_plot.gen_driver_points_plot(x, y, drivers, self.__year)