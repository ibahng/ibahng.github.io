import sys, os
HOME = os.getenv('HOME', '/Users/ingyubahng')
sys.path.append(f"{HOME}/Workspaces/pyutils")
import markets # type: ignore

test = markets.yfdata(
        ticker = 'CL=F',
        start = '2020-01-01',
        end = '2020-12-01',
        interval = '1d',
        )

print(type(test.table))
test.plot(
        count = '2',
        labels = 'm'
        )
