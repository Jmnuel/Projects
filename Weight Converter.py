
weight = int(input("Weight: "))

print("""
      Enter "K" if Kilogram
      Enter "L" if Pounds
""")

unit = input("(L)lbs or (K)kgs: ")

if unit.upper() == "L":
    w = weight * 0.45
    print(f"You are {w} kilos")
elif unit.upper() == "K": 
    w = weight // 0.45
    print(f"Your are {w} pounds")
