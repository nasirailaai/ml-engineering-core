"""
Python Loops and List Comprehensions
ml-engineering-core / 04_loops_and_comprehensions
"""

# -- 1. Bug fix -- return placement in loops ----------------------------------

def has_lucky_number(nums):
    """Return True if any number in the list is divisible by 7.

    Common bug: returning False inside the loop exits on the first
    non-lucky number. Fix: return False only after the full loop completes.

    >>> has_lucky_number([1, 2, 3, 7])
    True
    >>> has_lucky_number([1, 2, 3])
    False
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

print(has_lucky_number([14, 3, 9]))   # True
print(has_lucky_number([1, 2, 3]))    # False


# -- 2. List comprehension -- elementwise comparison --------------------------

def elementwise_greater_than(L, thresh):
    """Return a boolean list where each element is True if L[i] > thresh.

    This is exactly how NumPy masking works:
    arr > 0.5 returns a boolean array of the same shape.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [x > thresh for x in L]

print(elementwise_greater_than([1, 2, 3, 4], 2))   # [False, False, True, True]

# ML context: filtering predictions above a confidence threshold
predictions = [0.3, 0.7, 0.55, 0.9, 0.1]
threshold   = 0.5
confident   = elementwise_greater_than(predictions, threshold)
print(confident)   # [False, True, True, True, False]


# -- 3. Consecutive comparison -- sliding window pattern ----------------------

def menu_is_boring(meals):
    """Return True if the same meal was served two days in a row.

    Engineering note: comparing adjacent elements in a sequence is a
    sliding window of size 2. Same pattern used in time-series anomaly
    detection and sequence labeling tasks.

    >>> menu_is_boring(['rice', 'pasta', 'pasta'])
    True
    >>> menu_is_boring(['rice', 'pasta', 'salad'])
    False
    """
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False

print(menu_is_boring(['rice', 'pasta', 'pasta']))   # True
print(menu_is_boring(['rice', 'pasta', 'salad']))   # False


# -- 4. Monte Carlo estimation ------------------------------------------------

import random

def simulate_slot_machine():
    """Simplified slot machine for practice -- returns 0 most of the time."""
    return random.choices([0, 1, 5, 10], weights=[0.8, 0.1, 0.07, 0.03])[0]

def estimate_average_payout(n_runs):
    """Estimate average net profit over n_runs plays. Each play costs 1.

    Monte Carlo method: simulate many times, average the results.
    Same principle used in RL environment evaluation and model uncertainty
    estimation via dropout at inference time.
    """
    total = sum(simulate_slot_machine() - 1 for _ in range(n_runs))
    return total / n_runs

print(f"Estimated avg payout (1000 runs): {estimate_average_payout(1000):.4f}")


# -- 5. ML context -- list comprehensions in data pipelines -------------------

# Normalize a list of values to [0, 1]
raw_scores = [45, 78, 23, 90, 55, 67]
min_val    = min(raw_scores)
max_val    = max(raw_scores)

normalized = [(x - min_val) / (max_val - min_val) for x in raw_scores]
print([round(n, 3) for n in normalized])

# Filter samples above mean
mean   = sum(raw_scores) / len(raw_scores)
above  = [x for x in raw_scores if x > mean]
print(f"Above mean: {above}")

# Enumerate pattern -- common in training loops
for epoch, score in enumerate(raw_scores, start=1):
    print(f"Epoch {epoch}: score = {score}")
