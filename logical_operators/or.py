# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one conditions must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining: #if one condition is true the entire statement is true
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")