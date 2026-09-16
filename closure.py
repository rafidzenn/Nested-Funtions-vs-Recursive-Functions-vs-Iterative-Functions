# closure.py

def create_counter():
    """
    This is the outer function. It establishes a local variable 'count'.
    """
    count = 0  # This variable is protected from the global scope

    def increment():
        """
        This is the inner function (the closure). 
        It 'remembers' and modifies the 'count' variable from the outer scope.
        """
        nonlocal count # Required in Python to modify an outer variable
        count += 1
        return count

    # We return the function itself, not the result of the function
    return increment 

# --- Testing the Closure ---

# Create two completely separate counter instances
counter_a = create_counter()
counter_b = create_counter()

# counter_a remembers its own internal state
print(f"Counter A: {counter_a()}") # Output: 1
print(f"Counter A: {counter_a()}") # Output: 2

# counter_b maintains a completely separate, isolated state
print(f"Counter B: {counter_b()}") # Output: 1
print(f"Counter A: {counter_a()}") # Output: 3
