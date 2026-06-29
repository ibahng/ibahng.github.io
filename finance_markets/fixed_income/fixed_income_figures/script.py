import sys, os
HOME = os.getenv('HOME', '/Users/ingyubahng')
sys.path.append(f"{HOME}/Workspaces/pyutils")
import markets # type: ignore

FRED_API_KEY = os.getenv('FRED_API_KEY', 'error')
if FRED_API_KEY == "error":
    print('FRED api key error')

main = markets.freddata(
        code = 'FEDFUNDS',
        start = '2010-01-01',
        end = '2026-05-01',
        )

# main = markets.yfdata(
#         ticker = '^TYX',
#         start = '2012-01-01',
#         end = '2014-12-01',
#         interval = '1d',
#         )

main.plot(
        count = '2',
        labels = 'y'
        )
