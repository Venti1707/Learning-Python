# The match keyword is used to perform different actions based on different conditions
# It can be used to match many if else statements
# The general syntax is as follows:
"""
match (expression):
    case a | b if condition1:
        code to be executed
    case a | b if condition2:
        code to be executed
    ...
    case _:
        code to be executed
"""
# The pipe (|) character is used as an or operator to check for more than one value in a single case
# The underscore (_) character is used as the default case and will always match
# As such, it is advisable to use it as the last case
# The if statement is used as a check based on another condition

a = 5
b = 4
match a:
    case 1 | 2 | 3 | 4 | 5 if (b == 4):
        print("Weekday in April")
    case 6 | 7 if (b == 4):
        print("Weekend in April")
    case 1 | 2 | 3 | 4 | 5 if (b == 5):
        print("Weekday in May")
    case 6 | 7 if (b == 4):
        print("Weekend in May")