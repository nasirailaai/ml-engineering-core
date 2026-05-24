"""
Python Functions — Core Concepts
ml-engineering-core / 02_functions_and_scope
"""

# ── 1. Basic Function with Docstring ─────────────────────────────────────────

def round_to_two_places(num):
    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)

print(round_to_two_places(3.14159))   # 3.14
print(round_to_two_places(2.71828))   # 2.72


# ── 2. Negative ndigits — round() behavior ───────────────────────────────────

print("\n=== Negative ndigits ===")

print(round(1234.567, -1))    # 1230.0  — round to nearest 10
print(round(1234.567, -2))    # 1200.0  — round to nearest 100
print(round(1234.567, -3))    # 1000.0  — round to nearest 1000

# ML use case: rounding epoch counts or dataset sizes to nearest hundred
total_samples = 9876
rounded = round(total_samples, -2)
print(f"Rounded dataset size: {rounded}")   # 9900


# ── 3. Default Arguments — Optional Parameters ───────────────────────────────

print("\n=== Default Arguments ===")

def to_smash(total_candies, num_friends=3):
    """Return leftover candies after equal distribution.

    Default assumes 3 friends. Pass num_friends to override.

    >>> to_smash(91)
    1
    >>> to_smash(91, 4)
    3
    """
    return total_candies % num_friends

print(to_smash(91))        # 1  — 3 friends default
print(to_smash(91, 4))     # 3  — 4 friends
print(to_smash(100, 6))    # 4  — 6 friends

# ML parallel: default hyperparameters
def train_model(epochs=10, learning_rate=0.001, batch_size=32):
    """Simulate model training config with default hyperparameters."""
    print(f"Epochs: {epochs} | LR: {learning_rate} | Batch: {batch_size}")

train_model()                        # all defaults
train_model(epochs=50)               # override one
train_model(50, 0.01, 64)            # override all


# ── 4. Bug Fixes — Reading Error Messages ────────────────────────────────────

print("\n=== Bug Fixes ===")

# Bug 1: typo in function name (ruound → round_to_two_places)
print(round_to_two_places(9.9999))   # 10.0

# Bug 2: abs() applied to wrong scope
x = -10
y = 5
smallest_abs = min(abs(x), abs(y))   # abs() on each value separately
print(f"Smallest absolute value: {smallest_abs}")   # 5

# Bug 3: return statement indentation fixed
def f(x):
    y = abs(x)
    return y       # must be inside function body

print(f(5))    # 5
print(f(-8))   # 8


# ── 5. ML Context — Functions as Pipeline Steps ──────────────────────────────

print("\n=== ML Pipeline Functions ===")

def normalize(value, min_val, max_val):
    """Min-max normalization — scales value to [0, 1] range."""
    return (value - min_val) / (max_val - min_val)

def batch_count(total_samples, batch_size=32):
    """Return number of complete batches and leftover samples."""
    complete = total_samples // batch_size
    leftover = total_samples % batch_size
    return complete, leftover

print(normalize(75, 0, 100))          # 0.75
batches, remainder = batch_count(1000)
print(f"Batches: {batches}, Remainder: {remainder}")
