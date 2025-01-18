import warnings
import matplotlib.pyplot as plt

from utils import DRIVER_COLOR_DICT
warnings.filterwarnings('ignore')

def gen_driver_points_plot(x, y, drivers, year):
    plt.clf()
    for y_values, driver in zip(y, drivers):

        color = DRIVER_COLOR_DICT[driver] if driver in DRIVER_COLOR_DICT else 'black'

        plt.plot(x, y_values, label=driver, color=color)
    common(year)
    plt.ylabel('Points', fontsize=20)
    plt.subplots_adjust(bottom=.15, left=.15)
    fig = plt.gcf()
    plt.savefig(f'export/driver_points_{year}.pdf')
    plt.close()
    return fig

def common(year):
    plt.xlabel('Race', fontsize=14)
    plt.title(f'Driver Standings {year}', y=1.05, fontsize=14)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.ticklabel_format(style='plain', axis='y')
    plt.gca().set_yticklabels(['{:,.0f}'.format(x).replace(',','.') for x in plt.gca().get_yticks()])
