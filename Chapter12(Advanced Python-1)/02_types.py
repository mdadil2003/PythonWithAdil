# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

# Variable type hints

age: int = 25
# Function type hints
def greeting(name: str) -> str: # Function that takes a string and returns a string
    return f"Hello, {name}!"

print(greeting("Adil"))

from typing import List, Tuple # Importing List and Tuple for type hints
def process_data(data: List[Tuple[int, str]]) -> List[str]:
    processed = [f"ID: {item[0]}, Name: {item[1]}" for item in data] # Processing a list of tuples and returning a list of strings
    return processed
data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
processed = process_data(data) 
for item in processed:
    print(item)
    