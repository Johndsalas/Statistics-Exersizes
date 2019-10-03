import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm, binom
from scipy.stats import poisson
import matplotlib.pyplot as plt

# For the following problems, use python to simulate the problem and calculate an experimental probability, 
# then compare that to the theoretical probability.

# A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. 
# Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.




# A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars.
# What is the probability that no cars drive up in the noon hour?

mu = 2

stats.poisson(mu).pmf(0)


# What is the probability that 3 or more cars come through the drive through?

mu = 2

stats.poisson(mu).sf(3)

# How likely is it that the drive through gets at least 1 car?

mu = 2

stats.poisson(mu).sf(1)

# Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. 
# Calculate the following:
# What grade point average is required to be in the top 5% of the graduating class?

trials = cols = 10_000

samples =  rows = 100

mu, sigma = 3.0, .3

grades = np.random.normal(mu,sigma,trials * samples).reshape(rows, cols)

grades = pd.DataFrame(grades)

grades = grades.apply(lambda x: x.sort_values().values)

grades = grades.loc[[95]].mean(axis=0)

top_five_percent = grades.mean(axis=0)

top_five_percent

stats.norm(3,.3).isf(.05)

# What GPA constitutes the bottom 15% of the class?

trials = cols = 10_000

samples =  rows = 100

mu, sigma = 3.0, .3

grades = np.random.normal(mu,sigma,trials * samples).reshape(rows, cols)

grades = pd.DataFrame(grades)

grades = grades.apply(lambda x: x.sort_values().values)

grades = grades.loc[[14]].mean(axis=0)

bottom_fifteen_percent = grades.mean(axis=0)

bottom_fifteen_percent

stats.norm(3,.3).ppf(.15)

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. 
# Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

trials = cols = 10_000

samples = rows = 300

mu, sigma = 3.0, .3

grades = np.random.normal(mu,sigma,trials * samples).reshape(rows, cols)

grades = pd.DataFrame(grades)

grades = grades.apply(lambda x: x.sort_values().values)

lower_range = grades.loc[[60]].mean(axis=0)

lower_range_mean = lower_range.mean()

lower_range_mean

upper_range = grades.loc[[89]].mean(axis=0)

upper_range_mean = upper_range.mean()

upper_range_mean

print("The range is between " + str(lower_range_mean) + " and " + str(upper_range_mean))

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm, binom

dist = norm(mu,sigma)

lower = dist.ppf(.21)

upper = dist.ppf(.30)

print("The range is between " + str(lower) + " and " + str(upper))

# If I have a GPA of 3.5, what percentile am I in?

trials = rows = 10_000

samples = cols = 100

mu, sigma = 3.0, .3

grades = np.random.normal(mu,sigma,trials * samples).reshape(rows, cols)

grades = pd.DataFrame(grades)

(grades >= 3.5).sum(axis=1).mean()



mu, sigma = 3.0, .3

dist = norm(mu,sigma)

dist.cdf(3.5)

# A marketing website has an average click-through rate of 2%. 
# One day they observe 4326 visitors and 97 click-throughs. 
# How likely is it that this many people or more click through?
'''

mean click through rate = .02

observed 4326 visitors 

'''

n = 4326

prob = .02

dist = binom(n, prob)

dist.sf(97)



trials = rows = 10_000

samples = cols = 4326

data = np.random.uniform(1,101, samples * trials).reshape(rows,cols)

data = pd.DataFrame(data)

(((data < 3).sum(axis=1)) >= 97).sum() / trials

# You are working on some statistics homework consisting of 100 questions 
# where all of the answers are a probability rounded to the hundreths place. 
# Looking to save time, you put down random probabilities as the answer to each question.
# What is the probability that at least one of your first 60 answers is correct?

trials = rows = 50_000

samples =  cols = 60

answers = np.random.uniform(1,101, trials * samples).reshape(rows, cols)

answers = pd.DataFrame(answers)

((((answers < 2).sum(axis=1)) > 0).sum())/trials




import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm, binom
from scipy.stats import poisson
import matplotlib.pyplot as plt

binom = binom(60, .01)

binom.sf(0)


# The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, 
# about 90% of the 3 active cohorts of 22 students visit the break area. 
# How likely is it that the break area gets cleaned up each day? 
'''

total number of students = 3 cohorts * 22 students each

total studebts = 66

given a .9 chance that a given student visits the break area how many students will visit the break area on a given day?

students visiting break room on a given day = prob * total students = 66 * .9 = 59 rounding off decimal

'''

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm, binom
from scipy.stats import poisson
import matplotlib.pyplot as plt


n = 59

p = .03

dist = binom(n,p)

dist.sf(0)


trials = rows = 50_000

samples =  cols = 59

data = np.random.uniform(1,101, trials * samples).reshape(rows, cols)

data = pd.DataFrame(data)

(((data < 4).sum(axis=1)) > 0).sum() / trials


# How likely is it that it goes two days without getting cleaned up? 

n = 59

p = .03

dist = binom(n,p)

calc = dist.sf(0)

(1-calc)**2


trials = rows = 50_000

samples =  cols = 59

data = np.random.uniform(1,101, trials * samples).reshape(rows, cols)

data = pd.DataFrame(data)

exp = (((data < 4).sum(axis=1)) > 0).sum() / trials

(1-exp)**2

# All week?

n = 59

p = .03

dist = binom(n,p)

c = dist.sf(0)

(1-c)**7


trials = rows = 50_000

samples =  cols = 59

data = np.random.uniform(1,101, trials * samples).reshape(rows, cols)

data = pd.DataFrame(data)

exp = (((data < 4).sum(axis=1)) > 0).sum() / trials

(1-exp)**7




# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. 
# After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed 
# with a mean of 15 and standard deviation of 3. 
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food,
# what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? 
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.
'''
lunch = 1 hour

time left to eat = 15 min

time from order to recive = 10 min

maximum time in line = 60 min - 25 min == 

what are the odds that I spend less than 35 min waiting in line?

each person in line takes 2 min to order ==> 35/2 = total number of that can be in the line before I exceed maximum time

35/2 = 17 rounding off remainder

what is the probablity of 17 people or less being in line on a given day?

'''

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm, binom
from scipy.stats import poisson
import matplotlib.pyplot as plt


mu = 15

sigma = 3

binom = norm(mu,sigma)

binom.cdf(17)


trials = rows = 50_000

samples = cols = 1

mu = 15

sigma = 3

people = np.random.normal(mu,sigma,trials * samples)

(people <= 17).sum()/trials

# Connect to the employees database and find the average salary of current employees, along with the standard deviation. 
# Model the distribution of employees salaries with a normal distribution and answer the following questions:

from env import host, user, password

database = "employees"

def get_db_url(user,host,password,database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
    return url

url = get_db_url(user,host,password,database)

query = """ SELECT * FROM employees """

im = pd.read_sql(query, url)

im

# What percent of employees earn less than 60,000?
# What percent of employees earn more than 95,000?
# What percent of employees earn between 65,000 and 80,000?
# What do the top 5% of employees make?