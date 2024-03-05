"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.

Function: Reusable piece/block of code
Most functions can take different inputs and return different outputs

Reasons for functions:
Modularity: single large or complex mechanism can broken down into manageable pieces

Reusability: DONT REPEAT YOURSELF (DRY)

Maintainability: clear organization, easier to diagnose problems
Functions should do ONE thing
Single source of truth
Don't define functions within other functions

Debugging: automatically unit test functions

Abstraction: "information hiding"
"""

cat_name = "Tuna"
cat_age = 14

def greet(name: str, age: int) -> str:
    """
    Prints a greeting message to the console
    Args:
        name(str) : The name of the greeted thing
        age(int): The age of the greeted thing
    Returns:
        String greeting message
    """
    return f"Hello, {name}! You are {age} years old"

def math_operation(operand1: int, operand2: int, operation: str) -> float:
    """
    Return the result of a specified math operation with two operands.
    Args:
        operand1(int): First operand
        operand2(int): Second operand
        operation(str): Operation that will be performed
    Returns:
        Floating point value of operation outcome
    Raises:
        ValueError: "Invalid Operation" when operation is not '+' or '-'
    """

    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation")

    return result

try:
    result = math_operation(10, 27,  operation = "+")
    print(result)
except ValueError as ve: 
    print(ve)
except Exception:
    print("Something went wrong")

print(math_operation.__doc__)