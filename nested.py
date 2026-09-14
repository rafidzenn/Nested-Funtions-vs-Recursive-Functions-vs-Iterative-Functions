def outer_function(text):
    # This is a nested function
    def inner_helper():
        print(f"Helper processed: {text}") # Can access 'text' from parent scope
        
    inner_helper() # Called inside the parent
