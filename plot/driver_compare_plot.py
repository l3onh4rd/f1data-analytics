import warnings
import matplotlib.pyplot as plt

def gen_driver_compare_plot(x, y, driver1, driver2):
    plt.clf()
    colors = ['green' if y >= 0 else 'red' for y in y]
    plt.bar(x, y, color=colors)
    # for y_values, team in zip(y, teams):

    #     color = TEAM_COLOR_DICT[team] if team in TEAM_COLOR_DICT else 'black'

    #     plt.plot(x, y_values, label=team, color=color)
    common(driver1, driver2)
    plt.ylabel('Lossed/Gained Points', fontsize=20)
    plt.subplots_adjust(bottom=.15, left=.15)
    fig = plt.gcf()
    plt.savefig(f'export/driver_compare_{driver1}_to_{driver2}.pdf')
    plt.close()
    return fig

def common(driver1, driver2):
    plt.xlabel('Race', fontsize=14)
    plt.title(f'Gain/Loss of points of {driver1} compared to {driver2}', y=1.05, fontsize=14)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.ticklabel_format(style='plain', axis='y')
