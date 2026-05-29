"""
Python — Working with External Libraries
ml-engineering-core / 06_external_libraries
"""

# -- 1. Matplotlib — modifying graph objects ----------------------------------

# Key insight: graph objects have methods just like any other Python object.
# dir(graph) and help(graph) are how you discover them.
# Same pattern used when working with sklearn estimators, keras models, etc.

# prettify_graph example (requires matplotlib + jimmy_slots in Kaggle env)
#
# def prettify_graph(graph):
#     graph.set_title("Results of 500 slot machine pulls")
#     graph.set_ylim(bottom=0)
#     graph.set_ylabel("Balance")


# -- 2. Variable shadowing bug -- naming discipline ---------------------------

# Bug: using 'i' for both outer (integer) and inner (string) loop variables.
# The inner loop overwrites 'i', breaking the outer loop's index.
# Fix: use descriptive names -- idx for index, item for items.

def best_items(racers):
    """Return dict mapping items to first-place pickup counts.

    Engineering note: variable shadowing is a silent bug -- no error thrown,
    wrong results returned. Descriptive loop variable names prevent this.

    This pattern (counting occurrences across nested structures) appears in
    feature frequency analysis and token counting in NLP pipelines.
    """
    winner_item_counts = {}
    for idx in range(len(racers)):
        racer = racers[idx]
        if racer['finish'] == 1:
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1
        if racer['name'] is None:
            print("WARNING: Unknown racer on iteration {}/{}".format(
                idx + 1, len(racers)))
    return winner_item_counts

sample = [
    {'name': 'Peach',  'items': ['green shell', 'banana'], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell'],            'finish': 1},
    {'name': None,     'items': ['mushroom'],               'finish': 2},
    {'name': 'Toad',   'items': ['green shell', 'mushroom'],'finish': 1},
]
print(best_items(sample))
# {'green shell': 2, 'mushroom': 1}


# -- 3. Blackjack hand evaluator -- conditional logic + ace handling ----------

def hand_total(hand):
    """Calculate the optimal total for a blackjack hand.

    Aces counted as 11 first, then reduced to 1 if total exceeds 21.
    This greedy approach maximizes hand value without busting.

    ML parallel: this kind of conditional value assignment appears in
    reward shaping for reinforcement learning agents.
    """
    total = 0
    aces  = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces  += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and aces > 0:
        total -= 10
        aces  -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """Return True if hand_1 beats hand_2.

    Rules:
    - hand_1 total must not exceed 21
    - hand_1 total must exceed hand_2 total, OR hand_2 must be bust

    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total1 = hand_total(hand_1)
    total2 = hand_total(hand_2)

    if total1 > 21:
        return False
    if total2 > 21:
        return True
    return total1 > total2

print(blackjack_hand_greater_than(['K'], ['3', '4']))        # True
print(blackjack_hand_greater_than(['K'], ['10']))             # False
print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))   # False
print(blackjack_hand_greater_than(['A', 'A', '9'], ['K']))   # True  (21 vs 10)


# -- 4. Import patterns -- what ML code actually looks like -------------------

# Standard ML import block -- every project starts with this
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report

# Why aliases matter:
# np, pd, plt are universal conventions -- any ML engineer reads them instantly.
# Using full names (numpy.array) in ML code marks you as unfamiliar with the ecosystem.

print("Python course complete.")
print("Foundation ready for: NumPy, pandas, scikit-learn.")
