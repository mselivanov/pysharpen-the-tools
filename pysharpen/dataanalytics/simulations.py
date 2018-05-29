from random import choices, sample, shuffle, expovariate, gauss
from collections import Counter
from statistics import median, mean, stdev

# Roulette simulation
# 18 red slots, 18 black slots, 2 green slots
sixwheelspins = Counter(choices(["red", "black", "green"],
                                weights=[18, 18, 2], k=6))
print(sixwheelspins)

deck = Counter(tens=16, low=36)
deal = sample(list(deck.elements()), 52)
print(Counter(deal[20:]))

# 5 or more heads from 7 spins of a biased coins
population = ["heads", "tails"]
weights = [6, 4]
cummulative_weights = [0.6, 1.0]
trial = lambda: choices(population, cum_weights=cummulative_weights,
                        k=7).count("heads") >= 5
num_of_trials = 100000
print(sum([trial() for _ in range(num_of_trials)]) / num_of_trials)

# If we take a median from 5 element sample, how likely will it fall within
# 2nd and 3rd quartile
n = 100000
trial = lambda: n // 4 < median(sample(range(n), 5)) <= 3*n // 4
print(sum(trial() for i in range(100000)) / 100000)

# Timings
timings = [1.13, 2.08, 7.09, 8.12, 5.67, 7.98, 7.06, 8.99, 9.01]
## Build a 90% confidence interval
def bootstrap(data):
    return choices(data, k=len(data))

print(f"Population mean: {mean(timings)}")
print(f"Resampling mean: {mean(bootstrap(timings))}")
n = 10000
means = sorted([mean(bootstrap(timings)) for _ in range(n)])
print(f"Mean of means: {mean(means)}")
print(f"Observed mean: {mean(timings)}")
print(f"Falls into 90% confidence interval: {means[500] < mean(timings) < means[-500]}")

# P-values
# Check if change was due to drug or to chance
drug = [9.1, 10.6, 9.0, 8.41, 6.90, 7.11, 8.90, 7.89, 10.1]
placebo = [9.1, 6.6, 10.0, 6.41, 6.90, 8.11, 6.90, 9.89, 9.1]
print(f"Drug mean: {mean(drug)}. Mean placebo: {mean(placebo)}")
obs_diff = mean(drug) - mean(placebo)
print(f"Observed difference: {obs_diff}")
# Null hypothesis: there is no difference between drug and placebo
# Do a permutation test
combined = drug + placebo
drug_len = len(drug)
# if we reshuffle (permute, relabel)
# is the new mean has the same difference
def trial():
    shuffle(combined)
    drug = combined[:drug_len]
    placebo = combined[drug_len:]
    new_obs_diff = mean(drug) - mean(placebo)
    return new_obs_diff >= obs_diff
n = 10000
print(f"P-value: {sum(trial() for _ in range(n))/n}")

# Single server queue
average_arrival_interval = 5.6
average_service_time = 4.6
stdev_service_time = 0.5

num_waiting = 0.0 
arrivals = []
starts = []
arrival = service_end = 0.0
for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        arrival += expovariate(1.0 / average_arrival_interval)
        arrivals.append(arrival)
    else:
        num_waiting -= 1
        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)
        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for start, arrival in zip(starts, arrivals)]
print(f"Mean wait: {mean(waits):.1f}. Stdev wait: {stdev(waits):.1f}.")
print(f"Median wait: {median(waits):.1f}. Max wait: {max(waits):.1f}.")
