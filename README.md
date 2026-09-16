# Nested-Funtions-vs-Recursive-Functions-vs-Iterative-Functions
The inner function clean_name() is hidden from the rest of your program. It only exists and can only be called inside the outer function. But a recursive funtion is a function that calls itself. Last but certainly not the least, Iterative Functions. Instead of calling itself, it uses standard loops (for or while) to do repetitive work 


1. Pure Functions vs. Impure Functions (Side Effects)
This concept is critical for understanding modern software reliability and testing.

Pure Functions: A pure function always returns the exact same output if given the exact same input. It operates like a strict mathematical formula and never alters any data outside of itself.Impure Functions: An impure function interacts with the outside world. It might modify a global variable, change a database record, or read the current system time. These external changes are called side effects.

2. High-Order Functions vs. Callback Functions
This explains how modern languages treat functions as flexible, first-class citizens.

Higher-Order Functions: Instead of just accepting numbers or strings as inputs, a higher-order function is a function that accepts another function as an argument, or returns a function as its output.Callback Functions: A callback is the actual function passed into another function to be executed later. It is commonly used in asynchronous programming, telling the system: "Go do this heavy task, and when you are finished, run this callback function."


4. ## 4. Closures (The Evolution of Nested Functions)
If you understand nested functions, closures are the next step up. They are a fundamental concept for managing state and data privacy in modern software architecture.

**What is a Closure?** 
A closure is a nested (inner) function that "remembers" the variables and data from its outer function's scope, **even after the outer function has finished executing.** 

**Why are they important?**
* **State Management:** They allow a function to maintain a persistent state across multiple calls without relying on global variables. 
* **Data Privacy (Encapsulation):** Variables hidden inside the outer function cannot be modified directly from the outside world. They can only be interacted with through the inner function.
* **Function Factories:** When designing backend API endpoints or setting up custom state logic, you can use closures to dynamically generate specific, customized functions on the fly.


3. Object-Oriented Programming (OOP) vs. Functional Programming (FP)
This shifts the focus from individual functions to overarching programming paradigms (how you organize your entire codebase).

Object-Oriented Programming: This approach organizes code around objects that combine data (attributes) and behavior (methods) together. It models the program after real-world things.Functional Programming: This approach avoids combining data and behavior. Instead, it treats code as a sequence of pure mathematical evaluations and emphasizes immutable data (data that cannot be changed after it is created).
