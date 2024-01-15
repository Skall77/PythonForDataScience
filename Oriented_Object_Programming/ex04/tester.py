from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)

print("---")

try:
    calculator.dotproduct(a, 5)
except Exception as e:
    print(f"Error: {e}")

try:
    c = [5, 10]
    calculator.dotproduct(a, c)
except Exception as e:
    print(f"Error: {e}")

try:
    d = [5, 10, "2"]
    calculator.dotproduct(a, d)
except Exception as e:
    print(f"Error: {e}")
