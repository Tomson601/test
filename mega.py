import math
from typing import Union

class MathProgram:
    """Zaawansowany program do matematyki"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Dodawanie"""

        """Pierwiastek kwadratowy"""
        if x < 0:
            raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej!")
        result = math.sqrt(x)
        self.history.append(f"√{x} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Silnia"""
        if n < 0:
            raise ValueError("Silnia dla liczby ujemnej nie istnieje!")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
    
    def gcd(self, a: int, b: int) -> int:
        """Największy wspólny dzielnik"""
        result = math.gcd(a, b)
        self.history.append(f"NWD({a}, {b}) = {result}")
        return result
    
    def lcm(self, a: int, b: int) -> int:
        """Najmniejsza wspólna wielokrotność"""
        result = (a * b) // math.gcd(a, b)
        self.history.append(f"NWW({a}, {b}) = {result}")
        return result
    
    def fibonacci(self, n: int) -> list:
        """Ciąg Fibonacciego"""
        if n < 1:
            raise ValueError("n musi być większe od 0!")
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])
        self.history.append(f"Fibonacciego({n}) = {seq[:n]}")
        return seq[:n]
    
    def is_prime(self, n: int) -> bool:
        """Sprawdzenie czy liczba jest pierwsza"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        result = True
        self.history.append(f"Czy {n} jest liczbą pierwszą? {result}")
        return result
    
    def derivative_polynomial(self, coefficients: list) -> list:
        """Pochodna wielomianu"""
        if len(coefficients) <= 1:
            return [0]
        derivative = [coefficients[i] * (len(coefficients) - 1 - i) 
                     for i in range(len(coefficients) - 1)]
        self.history.append(f"Pochodna: {derivative}")
        return derivative
    
    def show_history(self):
        """Wyświetla historię obliczeń"""
        print("\n=== Historia obliczeń ===")
        for operation in self.history:
            print(operation)
    
    def clear_history(self):
        """Czyści historię"""
        self.history = []


def main():
    """Demonstracja programu"""
    calc = MathProgram()
    
    print("🎓 === MEGA FAJ program do MATEMATYKI === 🎓\n")
    
    # Podstawowe operacje
    print("Podstawowe operacje:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    
    # Potęgowanie i pierwiastek
    print(f"\n2^8 = {calc.power(2, 8)}")
    print(f"√144 = {calc.sqrt(144)}")
    
    # Silnia
    print(f"\n5! = {calc.factorial(5)}")
    
    # NWD i NWW
    print(f"NWD(48, 18) = {calc.gcd(48, 18)}")
    print(f"NWW(12, 8) = {calc.lcm(12, 8)}")
    
    # Liczby pierwsze
    print(f"\nCzy 17 jest liczbą pierwszą? {calc.is_prime(17)}")
    print(f"Czy 20 jest liczbą pierwszą? {calc.is_prime(20)}")
    
    # Ciąg Fibonacciego
    print(f"\nCiąg Fibonacciego (10 wyrazów): {calc.fibonacci(10)}")
    
    # Historia
    calc.show_history()


if __name__ == "__main__":
    main()
