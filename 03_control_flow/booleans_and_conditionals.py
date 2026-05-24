"""
Python Booleans and Conditionals
ml-engineering-core / 03_control_flow
"""

# -- 1. sign() function -- if/elif/else logic ---------------------------------

def sign(x):
    """Return 1 if x is positive, -1 if negative, 0 if zero.

    >>> sign(5)
    1
    >>> sign(-3)
    -1
    >>> sign(0)
    0
    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

print(sign(10))    # 1
print(sign(-7))    # -1
print(sign(0))     # 0


# -- 2. Conditional string logic ----------------------------------------------

def to_smash(total_candies):
    """Return leftover candies after distributing evenly between 3 friends.
    Uses conditional to handle singular vs plural grammar.

    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)    # Splitting 91 candies
to_smash(1)     # Splitting 1 candy


# -- 3. Boolean operator precedence -- the bug --------------------------------

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    """Bug: 'and' binds tighter than 'or' -- parentheses fix operator order."""
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Bug case: no umbrella, no rain, no hood, not workday -- should return True
# (no rain means prepared) but returns False without umbrella
have_umbrella = False
rain_level    = 0.0
have_hood     = False
is_workday    = False

print(prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday))


# -- 4. Concise boolean return ------------------------------------------------

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    """Boolean expression returns directly -- no if/else needed."""
    return number < 0

print(concise_is_negative(-5))   # True
print(concise_is_negative(3))    # False


# -- 5. Boolean combinations --------------------------------------------------

def wants_all_toppings(ketchup, mustard, onion):
    """All three must be True."""
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """All three must be False."""
    return not ketchup and not mustard and not onion

def exactly_one_sauce(ketchup, mustard, onion):
    """XOR pattern -- one or the other, not both."""
    return (ketchup or mustard) and not (ketchup and mustard)

print(wants_all_toppings(True, True, True))      # True
print(wants_plain_hotdog(False, False, False))   # True
print(exactly_one_sauce(True, False, False))     # True
print(exactly_one_sauce(True, True, False))      # False


# -- 6. int(bool) trick -------------------------------------------------------

def exactly_one_topping(ketchup, mustard, onion):
    """int(True) = 1, int(False) = 0 -- sum must equal 1.
    This pattern appears in one-hot encoding logic in ML.
    """
    return int(ketchup) + int(mustard) + int(onion) == 1

print(exactly_one_topping(True, False, False))   # True
print(exactly_one_topping(True, True, False))    # False


# -- 7. ML context -- conditional logic in model evaluation -------------------

def evaluate_model(accuracy, threshold=0.80):
    """Return deployment decision based on accuracy threshold."""
    if accuracy >= threshold:
        return "deploy"
    elif accuracy >= threshold - 0.10:
        return "retrain"
    else:
        return "discard"

print(evaluate_model(0.92))   # deploy
print(evaluate_model(0.74))   # retrain
print(evaluate_model(0.55))   # discard
