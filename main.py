import sys

from report.report import generate_report
from report.season_report import generate_season_report

CMD_ARGUMENTS = sys.argv[1:]

# check main mode to be 'season'
if 'season' in CMD_ARGUMENTS and CMD_ARGUMENTS[0] == 'season' and len(CMD_ARGUMENTS) == 2:
    # main mode is 'season'
    season_year = int(CMD_ARGUMENTS[1])
    # validate year
    if season_year < 2026:
        generate_season_report(season_year)
else:
    # start report generation
    generate_report()
