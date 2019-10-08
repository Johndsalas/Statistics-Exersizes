from pydataset import data
from scipy import stats

mpg = data('mpg')

x = mpg.displ
y = mpg.cty

p = stats.pearsonr(x, y)

p