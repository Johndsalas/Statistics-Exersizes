import numpy as np
import pandas as pd
from scipy import stats

from scipy.stats import poisson
import matplotlib.pyplot as plt

# For the following problems, use python to simulate the problem and calculate an experimental probability, 
# then compare that to the theoretical probability.

# A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. 
# Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

mu = 2

trials = 10_000

plt.ylabel('Probability of car passing')
plt.xlabel('Number of cars')
plt.title('Probability Distribution Curve')
arr = []
rv = poisson(mu)
for num in range(0,40):
 arr.append(rv.pmf(num))
 
# print(rv.pmf(28))
prob = rv.pmf(28)
plt.grid(True)
plt.plot(arr, linewidth=2.0)
plt.plot([28], [prob], marker='o', markersize=6, color="red")



# What is the probability that no cars drive up in the noon hour?

mu = 2



# What is the probability that 3 or more cars come through the drive through?
# How likely is it that the drive through gets at least 1 car?



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

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. 
# Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?



# A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. 
# How likely is it that this many people or more click through?

# You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.

# What is the probability that at least one of your first 60 answers is correct?
# The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. 
# After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? 
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.