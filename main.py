from DataExtractor import DataExtractor
from plot import con_points_plot
from report.report import generate_report

# get a chart of 2024 constructor points
data_extractor = DataExtractor()

season_2024_constructor_points = data_extractor.get_df_from_csv('./data/f1db-races-constructor-standings.csv')
season_2024_constructor_points = season_2024_constructor_points.drop(columns=['raceId', 'positionNumber', 'positionText', 'engineManufacturerId', 'positionsGained']) 
season_2024_constructor_points = season_2024_constructor_points[season_2024_constructor_points['year'] == 2024]


rounds = season_2024_constructor_points['round'].max()
teams = season_2024_constructor_points[season_2024_constructor_points['round'] == 1]['constructorId'].to_list()
x = list(range(1, rounds + 1))
y = []

for idx, team in enumerate(teams):
    y += [season_2024_constructor_points[season_2024_constructor_points['constructorId'] == team]['points'].to_list()]

print(y)

fig = con_points_plot.gen_con_points_plot(x, y, teams, '2024')
