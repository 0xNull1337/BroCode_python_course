# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one conditions must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is sunny")