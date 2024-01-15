from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5

try:
    v3 / 0
except Exception as e:
    print(f"Error: {e}")

try:
    v4 = calculator(5)
except Exception as e:
    print(f"Error: {e}")

try:
    v5 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, "5.0"])
except Exception as e:
    print(f"Error: {e}")

try:
    v2 + "5"
except Exception as e:
    print(f"Error: {e}")
