import sys, os
HOME = os.getenv('HOME', '/Users/ingyubahng')
sys.path.append(f"{HOME}/Workspaces/pyutils")
import markets # type: ignore

FRED_API_KEY = os.getenv('FRED_API_KEY', 'error')
if FRED_API_KEY == "error":
    print('FRED api key error')

main = markets.yfdata(
        ticker = 'DX-Y.NYB',
        start = '1985-02-01',
        end = '1990-01-01',
        interval = '1d',
        )

main.plot(
        count = '2',
        labels = 'y'
        )

# fred = markets.freddata(
#         code = 'DFF',
#         start = '1975-01-01',
#         end = '1985-01-01',
#         )

# fred.plot(
#         count = '1',
#         labels = 'y',
#         ylabel = 'Rate'
#         )

# print(type(test.table))

