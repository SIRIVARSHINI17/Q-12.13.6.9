import numpy as np
from scipy.special import comb

# Probability of success and failure
p = 2/3  # Success
q = 1 - p  # Failure

# Total number of trials
n = 6

# Calculate the probabilities for k = 4, 5, and 6
pr_4 = comb(n, 4) * (p ** 4) * (q ** (n - 4))
pr_5 = comb(n, 5) * (p ** 5) * (q ** (n - 5))
pr_6 = comb(n, 6) * (p ** 6) * (q ** (n - 6))

# Sum up the probabilities to get the final probability of at least 4 successes
pr_at_4 = pr_4 + pr_5 + pr_6

print( pr_at_4)

