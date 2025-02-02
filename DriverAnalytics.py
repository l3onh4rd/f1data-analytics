from DataExtractor import DataExtractor
from Standings import Standings
from plot import driver_points_plot

class DriverAnalytics(Standings):
    def __init__(self, year):
        self.__year = year
        data_extractor = DataExtractor()
        # read raw csv data
        self.__season_driver_data = data_extractor.get_df_from_csv('./data/f1db-races-driver-standings.csv')

    def set_year(self, year):
        self.__year = year
    
    def get_driver_standings_data(self):
        # drop unnecessary columns
        season_driver_points = self.__season_driver_data.drop(columns=['raceId', 'positionDisplayOrder', 'positionNumber', 'positionText', 'positionsGained']) 
        # filter for requested year
        season_driver_points = season_driver_points[season_driver_points['year'] == self.__year]
        # number of races
        rounds = season_driver_points['round'].max()
        # generate x values depending on number of races
        x = list(range(1, rounds + 1))
        # get a list of the drivers for the drivers championchip
        drivers = season_driver_points['driverId'].unique().tolist()
        
        # generating y values (points for each driver after each race)
        y = []
        for idx, _ in enumerate(drivers):
            y.append([])

        # avoid empty slots in data and provide None values if so
        for race in x:
            for idx, driver in enumerate(drivers):
                point = season_driver_points[(season_driver_points['driverId'] == driver) & (season_driver_points['round'] == race)]['points']
                if len(point) == 0:
                    y[idx].append(None)
                else:
                    y[idx].append(season_driver_points[(season_driver_points['driverId'] == driver) & (season_driver_points['round'] == race)]['points'].to_list()[0])

        return x, y, drivers
    
    def generate_chart(self):
        x, y, drivers = self.get_driver_standings_data()
        return driver_points_plot.gen_driver_points_plot(x, y, drivers, self.__year)