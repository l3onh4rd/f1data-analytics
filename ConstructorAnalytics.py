from DataExtractor import DataExtractor
from plot import con_points_plot

class ConstructorAnalytics:
    def __init__(self, year):
        self.__year = year

    def set_year(self, year):
        self.__year = year

    def get_constructor_standings_data(self):
        data_extractor = DataExtractor()
        # read raw csv data
        season_constructor_points = data_extractor.get_df_from_csv('./data/f1db-races-constructor-standings.csv')
        # drop unnecessary columns
        season_constructor_points = season_constructor_points.drop(columns=['raceId', 'positionNumber', 'positionText', 'engineManufacturerId', 'positionsGained']) 
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
        for team in teams:
            y += [season_constructor_points[season_constructor_points['constructorId'] == team]['points'].to_list()]

        return x, y, teams
    
    def generate_chart(self):
        x, y, teams = self.get_constructor_standings_data()
        return con_points_plot.gen_con_points_plot(x, y, teams, self.__year)