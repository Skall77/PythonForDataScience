from S1E9 import Character, Stark

try:
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print("---")
    print(Ned.__doc__)
    print("---")
    print(Ned.__init__.__doc__)
    print("---")
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    John = Character("John")
except Exception as e:
    print(f"Error: {e}")
