# Exercises

import numpy as np
import pandas as pd

# How likely is it that you roll doubles when rolling two dice?


def roll_dice(tirals):

    count = 0

    denominator = trials

    success = 0

    while count < trials:

        die1 = np.random.choice([1,2,3,4,5,6])

        die2 = np.random.choice([1,2,3,4,5,6])

        if die1 == die2:

            success += 1

        count += 1

    return success/denominator

trials = 10_000

roll_dice(trials)

# If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?

n_trials = nrows = 10_000
n_coins = ncols = 8

rolls = np.random.choice([0, 1], n_trials * n_dice).reshape(nrows, ncols)

rolls

((rolls.sum(axis=1) > 3).astype(int)).sum()/n_trials

# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards 
# I drive past both have data science students on them?

n_trials = nrows = 10_000
n_billboards = ncols = 2

rolls = np.random.choice([0, 1, 1, 1], n_trials * n_billboards).reshape(nrows, ncols)

rolls

((rolls.sum(axis=1) == 0).astype(int)).sum()/n_trials

# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, 
# how likely is it that I will be able to buy some poptarts on Friday afternoon?
trials = rows = 10_000

samples = cols = 5

mu, sigma = 3, 1.5

bought = np.random.normal(mu,sigma,trials * samples).reshape(rows, cols)

(((17 - bought.sum(axis=1)) > 0).astype(int).sum())/trials
# Compare Heights
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?

trials = rows = 10_000

samples = cols = 1

mum, sigmam = 178, 8
muf, sigmaf = 170, 6

male_hight = np.random.normal(mum,sigmam,trials * samples).reshape(rows, cols)

female_hight = np.random.normal(muf,sigmaf,trials * samples).reshape(rows, cols)

(female_hight.sum(axis=1) > male_hight.sum(axis=1)).astype(int).sum()

/trials

# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
# What is the probability that we observe an installation issue within the first 150 students that download