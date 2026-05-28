"""
Python Strings and Dictionaries
ml-engineering-core / 05_strings_and_dicts
"""

# -- 0. String length mental model --------------------------------------------

print("=== String Length Tests ===")

a = ""          # empty string
b = "it's ok"   # apostrophe counts
c = 'it\'s ok'  # escaped quote, same as b
d = """hey"""   # triple quotes, still 3 chars
e = '\n'        # newline is ONE character

print(len(a))   # 0
print(len(b))   # 7
print(len(c))   # 7
print(len(d))   # 3
print(len(e))   # 1


# -- 1. String validation -- zip code -----------------------------------------

def is_valid_zip(zip_code):
    """Return True if zip_code is exactly 5 digits.

    isdigit() returns False for floats, negatives, spaces.
    len() check ensures exactly 5 characters.

    ML context: same validation pattern used in data cleaning pipelines
    before feeding string features into a model.

    >>> is_valid_zip('12345')
    True
    >>> is_valid_zip('1234')
    False
    >>> is_valid_zip('1234a')
    False
    """
    return zip_code.isdigit() and len(zip_code) == 5

print(is_valid_zip('12345'))    # True
print(is_valid_zip('1234'))     # False
print(is_valid_zip('abcde'))    # False
print(is_valid_zip('123 45'))   # False


# -- 2. Text search -- whole word matching ------------------------------------

def word_search(doc_list, keyword):
    """Return indices of documents containing keyword as a standalone word.

    Handles: case insensitivity, periods, commas.
    Does not match partial words (casino != casinoville).

    ML context: same preprocessing steps used in NLP pipelines --
    lowercasing, punctuation removal, tokenization.

    >>> doc_list = ["The Learn Python Challenge Casino.", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    [0]
    """
    result = []
    for i, doc in enumerate(doc_list):
        words = doc.lower().replace('.', '').replace(',', '').split()
        if keyword.lower() in words:
            result.append(i)
    return result

doc_list = [
    "The Learn Python Challenge Casino.",
    "They bought a car",
    "Casinoville"
]
print(word_search(doc_list, 'casino'))   # [0]
print(word_search(doc_list, 'they'))     # [1]


# -- 3. Dictionary comprehension -- multi keyword search ----------------------

def multi_word_search(doc_list, keywords):
    """Return dict mapping each keyword to list of matching document indices.

    Uses word_search() to avoid repeating logic.
    Dictionary comprehension keeps it concise.

    ML context: building an inverted index -- the foundation of search engines
    and document retrieval systems.

    >>> multi_word_search(doc_list, ['casino', 'they'])
    {'casino': [0, 1], 'they': [1]}
    """
    return {keyword: word_search(doc_list, keyword) for keyword in keywords}

doc_list2 = [
    "The Learn Python Challenge Casino.",
    "They bought a car and a casino",
    "Casinoville"
]
print(multi_word_search(doc_list2, ['casino', 'they']))
# {'casino': [0, 1], 'they': [1]}


# -- 4. ML context -- dicts as config objects ---------------------------------

print("\n=== ML Config Pattern ===")

model_config = {
    'model_name'   : 'baseline_v1',
    'learning_rate': 0.001,
    'batch_size'   : 32,
    'num_epochs'   : 100,
    'optimizer'    : 'adam',
    'dropout_rate' : 0.3,
}

for key, value in model_config.items():
    print(f"{key:15} : {value}")

# Updating a single hyperparameter
model_config['learning_rate'] = 0.0005
print(f"\nUpdated LR: {model_config['learning_rate']}")

# Checking if key exists before accessing
if 'dropout_rate' in model_config:
    print(f"Dropout: {model_config['dropout_rate']}")
