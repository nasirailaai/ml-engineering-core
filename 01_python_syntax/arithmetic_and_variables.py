"""
Python Syntax — Arithmetic & Variables
ml-engineering-core / 01_python_syntax
"""

# ── 1. Arithmetic Operators ───────────────────────────────────────────────────

print("=== Arithmetic Operators ===")

print(2 + 3)    # Addition       → 5
print(10 - 4)   # Subtraction    → 6
print(3 * 7)    # Multiplication → 21
print(7 / 2)    # True division  → 3.5  (always float)
print(7 // 2)   # Floor division → 3    (drops decimal)
print(7 % 2)    # Modulo         → 1    (remainder)
print(2 ** 8)   # Exponentiation → 256

# ── 2. Operator Precedence ────────────────────────────────────────────────────

print("\n=== Precedence Tests ===")

print(2 + 3 * 4)       # 14  — multiplication runs first
print((2 + 3) * 4)     # 20  — parentheses override
print(2 ** 3 + 1)      # 9   — exponent runs first
print(2 ** (3 + 1))    # 16  — parentheses override

# ── 3. Variable Types ─────────────────────────────────────────────────────────

print("\n=== Variable Types ===")

learning_rate = 0.001       # float
num_epochs    = 100         # int
model_name    = "baseline"  # str
is_trained    = False       # bool

print(type(learning_rate))  # <class 'float'>
print(type(num_epochs))     # <class 'int'>
print(type(model_name))     # <class 'str'>
print(type(is_trained))     # <class 'bool'>

# ── 4. Real ML Context — Batch Calculation ────────────────────────────────────

print("\n=== Batch Calculation ===")

total_samples = 1000
batch_size    = 32

num_batches = total_samples // batch_size   # floor division → 31
leftover    = total_samples % batch_size    # remainder     → 8

print(f"Total samples : {total_samples}")
print(f"Batch size    : {batch_size}")
print(f"Full batches  : {num_batches}")
print(f"Leftover      : {leftover}")

# ── 5. Circle Area (Kaggle Q1 — clean version) ───────────────────────────────

print("\n=== Circle Area ===")

pi       = 3.14159
diameter = 3
radius   = diameter / 2
area     = pi * radius ** 2

print(f"Radius : {radius}")
print(f"Area   : {area:.4f}")

# ── 6. Variable Swap ──────────────────────────────────────────────────────────

print("\n=== Variable Swap ===")

a = [1, 2, 3]
b = [3, 2, 1]

a, b = b, a     # tuple unpacking — no temp variable needed

print(f"a = {a}")
print(f"b = {b}")

# ── 7. Candy Problem (Kaggle Q4 — clean version) ─────────────────────────────

print("\n=== Remainder Logic ===")

alice_candies = 121
bob_candies   = 77
carol_candies = 109

total    = alice_candies + bob_candies + carol_candies
to_smash = total % 3

print(f"Total candies : {total}")
print(f"To smash      : {to_smash}")
