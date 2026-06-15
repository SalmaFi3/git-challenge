# calculator.py
# Fonctionnalité générée avec l'aide de Claude (Anthropic)
# Revue et validée par Salma

def add(a, b):
    """Additionne deux nombres."""
    return a + b

def subtract(a, b):
    """Soustrait b de a."""
    return a - b

def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b

def divide(a, b):
    """Divise a par b. Lève une erreur si b == 0."""
    if b == 0:
        raise ValueError("Division par zéro impossible.")
    return a / b

# Tests simples
if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 × 6 = {multiply(5, 6)}")
    print(f"15 ÷ 3 = {divide(15, 3)}")