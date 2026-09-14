def countdown(n):
    if n <= 0: # Base case
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1) # Recursive call
