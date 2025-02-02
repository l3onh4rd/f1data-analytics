from DataExtractor import DataExtractor
from Standings import Standings
from plot import con_points_plot

class ConstructorAnalytics(Standings):
    def __init__(self, year):
        self.__year = year
        data_extractor = DataExtractor()
        # read raw csv data
        self.__constructor_data = data_extractor.get_df_from_csv('./data/f1db-races-constructor-standings.csv')

    def set_year(self, year):
        self.__year = year
    
    def get_constructor_standings_data(self):
        # drop unnecessary columns
        season_constructor_points = self.__constructor_data.drop(columns=['raceId', 'positionNumber', 'positionText', 'engineManufacturerId', 'positionsGained']) 
        # filter for requested year
        season_constructor_points = season_constructor_points[season_constructor_points['year'] == self.__year]
        # number of races
        rounds = season_constructor_points['round'].max()
        # generate x values depending on number of races
        x = list(range(1, rounds + 1))
        # get a list of the teams for the constructors championchip
        teams = season_constructor_points[season_constructor_points['round'] == 1]['constructorId'].to_list()

        # generating y values (points for each team after each race)
        y = []
        for idx, _ in enumerate(teams):
            y.append([])

        # avoid empty slots in data and provide None values if so
        for race in x:
            for idx, driver in enumerate(teams):
                point = season_constructor_points[(season_constructor_points['constructorId'] == driver) & (season_constructor_points['round'] == race)]['points']
                if len(point) == 0:
                    y[idx].append(None)
                else:
                    y[idx].append(season_constructor_points[(season_constructor_points['constructorId'] == driver) & (season_constructor_points['round'] == race)]['points'].to_list()[0])

        return x, y, teams
    
    def generate_chart(self):
        x, y, teams = self.get_constructor_standings_data()
        return con_points_plot.gen_con_points_plot(x, y, teams, self.__year)