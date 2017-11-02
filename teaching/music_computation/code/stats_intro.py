# == Simulation and basis statistics in Python ==

# Original code [here](stats_intro.py).

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
# Import [secret.py](secret.py) which contains the `success_rate`
# for instiating `FlipSim` in the examples below
import secret
import scipy.stats as st

# === Simulation of Bernoulli trials ===

class FlipSim(object):
    """Class for simulating Bernoulli trials"""
    def __init__(self, success_rate):
        self.success_rate = success_rate
        self.trials = []

    def get_success_rate(self):
        return self.success_rate

    def flip(self):
        """Returns the result of a single 'flip'"""
        if random.random() <= self.success_rate:
            return True
        else:
            return False

    def flips(self, num_flips):
        """Returns a list of a single trial of `num_flips` flips"""
        return [self.flip() for i in range(num_flips)]

    def flip_trials(self, flips_per_trial, num_trials):
        """Returns a list of `num_trials` trials of `flips_per_trials` each"""
        self.trials = [self.flips(flips_per_trial) for i in range(num_trials)]
        return self.trials

# === Is it fair or loaded simulated coin? ===

sim = FlipSim(secret.value)
# 10,000 trials of 1,000 flips each. Experiment with different combinations
# of `flips_per_trial` and `num_trials`.
trials = sim.flip_trials(1000, 10000)

# Descriptive stats
means = [np.mean(trial) for trial in trials]
mean = np.mean(means)
sigma = np.std(means)

# Results should be similar to:  
# `The mean is 0.5300304`  
# `The standard deviation is 0.0157946977128`  

print('The mean is', mean)
print('The standard deviation is', sigma)

# `68% of the values lie between 0.514235702287 and 0.545825097713`  
# `95% of the values lie between 0.498441004574 and 0.561619795426`  
# `99.7% of the values lie between 0.482646306861 and 0.577414493139`
# Thus, on the basis of this particular simulation we can say with 95%
# confidence that `secret.value` lies between 0.498 and 0.562.

print('68% of the values lie between', mean - sigma, 'and', mean + sigma)
print('95% of the values lie between', mean - 2*sigma, 'and', mean + 2*sigma)
print('99.7% of the values lie between', mean - 3*sigma, 'and', mean + 3*sigma)

# === Plot the simulation ===

# `numpy.linspace` returns evenly spaced numbers over a specified interval.
# In this case the range of x is defined by the mean plus/minus three
# standard deviations.
x = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
# Create a histogram of the means
plt.hist(means, bins = 200)
# Draw the _probability distribution function_ (pdf) of the normal distribuation
# with mean `secret.value` and standard deviation of `sigma` within the range
# of `x`.
plt.plot(x, 10 * mlab.normpdf(x, secret.value, sigma))
# Show the plot
plt.show()

# === Using `scipy.stats` ===

# Create three different Bernoulli trials of 1,000 flips each with different
# success rates
x1 = FlipSim(0.5).flips(1000)
x2 = FlipSim(0.52).flips(1000)
x3 = FlipSim(0.57).flips(1000)

# Use Independent Two-Sampled T-test to test the Null Hypothesis that the
# means of two independent samples are the same.
# Results should be similar though not identical to:
# `Ttest_indResult(statistic=0.53653387639428951, pvalue=0.59164936190673534)`
# Null hypothesis is not rejected
print(st.ttest_ind(x1, x2))
# `Ttest_indResult(statistic=-1.2543243107046314, pvalue=0.20987087051240788)`
# Null hypothesis is rejected
print(st.ttest_ind(x1, x3))

# Use ANOVA to test the Null Hypothesis that the means of more than two
# independent samples are all the same.
# Results should be similar to:  
# `F_onewayResult(statistic=9.1459470595680799, pvalue=0.0001096574199724701)`
# Null Hypothesis is rejected
print(st.f_oneway(x1, x2, x3))
