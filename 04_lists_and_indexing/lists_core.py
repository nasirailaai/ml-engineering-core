"""
Python Lists — Indexing, Slicing, Mutation
ml-engineering-core / 03_control_flow
"""

# -- 1. Indexing -- safe access -----------------------------------------------

def select_second(L):
    """Return the second element of the list. Return None if it doesn't exist.

    >>> select_second([1, 2, 3])
    2
    >>> select_second([1])
    None
    """
    if len(L) < 2:
        return None
    return L[1]

print(select_second([10, 20, 30]))   # 20
print(select_second([10]))           # None
print(select_second([]))             # None


# -- 2. Nested list indexing --------------------------------------------------

def losing_team_captain(teams):
    """Return the captain (index 1) of the last team (index -1).

    In ML terms: accessing specific positions in nested data structures,
    same pattern used when indexing batches within a dataset.

    >>> losing_team_captain([['Coach A', 'Cap A'], ['Coach B', 'Cap B']])
    'Cap B'
    """
    return teams[-1][1]

teams = [
    ["Coach1", "Captain1", "Player1"],
    ["Coach2", "Captain2", "Player2"],
    ["Coach3", "Captain3", "Player3"],
]
print(losing_team_captain(teams))   # Captain3


# -- 3. In-place list mutation -- swap -----------------------------------------

def purple_shell(racers):
    """Swap first and last elements in-place using tuple unpacking.

    This same pattern appears in dataset shuffling -- swapping sample positions
    without creating a new list.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ['Luigi', 'Bowser', 'Mario']
    """
    racers[0], racers[-1] = racers[-1], racers[0]

racers = ["Mario", "Bowser", "Luigi", "Peach"]
purple_shell(racers)
print(racers)   # ['Peach', 'Bowser', 'Luigi', 'Mario']


# -- 4. List length -- mental model test --------------------------------------

a = [1, 2, 3]          # 3 elements
b = [1, [2, 3]]        # 2 elements -- nested list counts as one
c = []                 # 0 elements
d = [1, 2, 3][1:]      # slicing from index 1 -- 2 elements remain

lengths = [len(a), len(b), len(c), len(d)]
print(lengths)   # [3, 2, 0, 2]

# Key insight: a nested list is ONE element regardless of its contents
# This matters in ML when working with batched data -- shape != length


# -- 5. Positional logic -- fashionably late ----------------------------------

def fashionably_late(arrivals, name):
    """Return True if the person arrived after at least half the guests
    but was not the very last to arrive.

    Engineering note: this combines index lookup with a positional threshold --
    same logic used in ranking, percentile cutoffs, and top-k filtering.

    >>> party = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
    >>> fashionably_late(party, 'Mona')
    True
    >>> fashionably_late(party, 'Ford')
    False
    """
    position = arrivals.index(name)
    return position >= len(arrivals) / 2 and position != len(arrivals) - 1

party = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(party, 'Mona'))     # True
print(fashionably_late(party, 'Gilbert'))  # True
print(fashionably_late(party, 'Ford'))     # False
print(fashionably_late(party, 'Adela'))    # False


# -- 6. ML context -- list operations in data pipelines -----------------------

# Slicing -- train/test split pattern
dataset = list(range(100))
split    = int(len(dataset) * 0.8)

train = dataset[:split]    # first 80%
test  = dataset[split:]    # last 20%

print(f"Train size : {len(train)}")   # 80
print(f"Test size  : {len(test)}")    # 20

# Negative indexing -- last N samples
last_5 = dataset[-5:]
print(f"Last 5 samples: {last_5}")   # [95, 96, 97, 98, 99]
