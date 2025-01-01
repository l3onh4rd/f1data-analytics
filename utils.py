import datetime

TEAM_COLORS = ['#F67F00', '#DE0016', '#4272C9', '#5AF4D2', '#3A9970', '#2A90CC', '#B6BABD', '#6E93FF', '#74C5FF', '#4AE900']
COLOR_MCLAREN = '#F67F00'
COLOR_FERRARI = '#DE0016'
COLOR_REDBULL = '#4272C9'
COLOR_MERCEDES = '#5AF4D2'
COLOR_ASTONMARTIN = '#3A9970'
COLOR_ALPINE = '#2A90CC'
COLOR_HAAS = '#B6BABD'
COLOR_RB = '#6E93FF'
COLOR_WILLIAMS = '#74C5FF'
COLOR_SAUBER = '#4AE900'

TEAM_COLOR_DICT = {
    'mclaren': COLOR_MCLAREN,
    'red-bull': COLOR_REDBULL,
    'ferrari': COLOR_FERRARI,
    'mercedes': COLOR_MERCEDES,
    'aston-martin': COLOR_ASTONMARTIN,
    'alpine': COLOR_ALPINE,
    'haas': COLOR_HAAS,
    'rb': COLOR_RB,
    'williams': COLOR_WILLIAMS,
    'kick-sauber': COLOR_SAUBER
}

def get_current_date_and_time():
    return datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')