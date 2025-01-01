import warnings
import matplotlib.pyplot as plt

from utils import TEAM_COLOR_DICT
warnings.filterwarnings('ignore')

def gen_con_points_plot(x, y, teams, year):
    plt.clf()
    for y_values, team in zip(y, teams):
        plt.plot(x, y_values, label=team, color=TEAM_COLOR_DICT[team])
    common(year)
    plt.ylabel('Points', fontsize=20)
    plt.subplots_adjust(bottom=.15, left=.15)
    fig = plt.gcf()
    plt.savefig(f'export/con_points_{year}.pdf')
    plt.close()
    return fig

def common(year):
    plt.xlabel('Race', fontsize=14)
    plt.title(f'Constructor Standings {year}', y=1.05, fontsize=14)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.ticklabel_format(style='plain', axis='y')
    plt.gca().set_yticklabels(['{:,.0f}'.format(x).replace(',','.') for x in plt.gca().get_yticks()])
