import sys, os
HOME = os.getenv('HOME', '/Users/ingyubahng')
sys.path.append(f"{HOME}/Workspaces/pyutils")
import markets # type: ignore

FRED_API_KEY = os.getenv('FRED_API_KEY', 'error')
if FRED_API_KEY == "error":
    print('FRED api key error')

test = markets.yfdata(
        ticker = 'CL=F',
        start = '2024-01-01',
        end = '2026-06-03',
        interval = '1d',
        )

test.plot(
        count = '8',
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


print("done")

# print(type(test.table))
